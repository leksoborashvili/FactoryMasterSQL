import json
import logging

import requests
import msal


class Authorization():
    
    def __init__(self):
        self.token = "invalid"
        self.config = {
                  "authority": "https://login.microsoftonline.com/04598e31-aaef-4e53-b9fa-b75ed0c41d18",
                  "client_id": "0236972f-7c1b-4c93-b994-2a40e814de6c",
                  "scope": [ "User.ReadBasic.All" ],
                  "endpoint": "https://graph.microsoft.com/v1.0/me/"
                  }
        self.app = msal.PublicClientApplication(
        self.config["client_id"], authority=self.config["authority"],
        # token_cache=...  # Default cache is in memory only.
                           # You can learn how to use SerializableTokenCache from
                           # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
        )

    def authorize(self, username, password, failedLogin):
        self.username = username
        result = None
        accounts = self.app.get_accounts(username = username)
        if accounts:
            logging.info("Account(s) exists in cache, probably with token too. Let's try.")
            result = self.app.acquire_token_silent(self.config["scope"], account=accounts[0])
        if not result:
            logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
            # See this page for constraints of Username Password Flow.
            # https://github.com/AzureAD/microsoft-authentication-library-for-python/wiki/Username-Password-Authentication
            result = self.app.acquire_token_by_username_password(
                username, password, scopes=self.config["scope"])
         
        if "access_token" in result:
            # Calling graph using the access token
            graph_data = requests.get(  # Use token to call downstream service
                self.config["endpoint"],
                headers={'Authorization': 'Bearer ' + result['access_token']},).json()
            print("Graph API call result: %s" % json.dumps(graph_data, indent=2))
            return "access_token"
        else:
            print(result.get("error"))
            failedLogin(result.get("error_description"))
            print(result.get("error_description"))
            #print(result.get("correlation_id"))  # You may need this when reporting a bug
            if 65001 in result.get("error_codes", []):  # Not mean to be coded programatically, but...
                # AAD requires user consent for U/P flow
                #TODO
                print("Visit this to consent:", self.app.get_authorization_request_url(self.config["scope"]))
                failedLogin(self.app.get_authorization_request_url(self.config["scope"]))
            return None

    def logout(self):
        accounts = self.app.get_accounts(username = self.username)
        print(accounts[0])
        if accounts:
            print("Account(s) exists in cache, probably with token too. Let's try.")
            result = self.app.acquire_token_silent(self.config["scope"], account=accounts[0])
            self.app.remove_account(account = accounts[0])




