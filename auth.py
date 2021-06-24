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

    def authorize(self, username, password, failedLogin):
        app = msal.PublicClientApplication(
        self.config["client_id"], authority=self.config["authority"],
        # token_cache=...  # Default cache is in memory only.
                           # You can learn how to use SerializableTokenCache from
                           # https://msal-python.rtfd.io/en/latest/#msal.SerializableTokenCache
        )
        result = None
        accounts = app.get_accounts(username = username)
        if accounts:
            logging.info("Account(s) exists in cache, probably with token too. Let's try.")
            result = app.acquire_token_silent(self.config["scope"], account=accounts[0])
        if not result:
            logging.info("No suitable token exists in cache. Let's get a new one from AAD.")
            # See this page for constraints of Username Password Flow.
            # https://github.com/AzureAD/microsoft-authentication-library-for-python/wiki/Username-Password-Authentication
            result = app.acquire_token_by_username_password(
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
                print("Visit this to consent:", app.get_authorization_request_url(self.config["scope"]))
                failedLogin(app.get_authorization_request_url(self.config["scope"]))
            return None





