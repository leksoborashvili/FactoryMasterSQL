import pyodbc
import io
from PIL import  Image, ImageTk


class DB:

    def __init__(self):
        server = 'factorydataserver.database.windows.net'
        database = 'DataBase1'
        username = 'Kpursell'
        password = 'F@ct0ry315'
        driver= '{SQL Server}'
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
            self.con = conn
            
        #self.con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\LeksoBorashvili\source\repos\test\test\masterData.accdb;')
        self.cursor = self.con.cursor()

    def createObject(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""INSERT INTO MasterDataTable (BrandName, ProductStyle, ProductFlavor)
                            VALUES(?,?,?) """, brandName, productStyle, productFlavor)
        self.cursor.commit()


    def selectMarketing(self, brandName, productStyle, productFlavor):
        try:
            self.cursor.execute("""SELECT Format, FoodServiceBulkPack, EachUPC,
                EachWeight, EachUOM, QtyPerInner, InnerPackUPC, InnerWeight, InnerUOM, QtyPerCase, CaseUPC, CaseWeightLbs, CaseUOM,
                QtyCasesperPallet, CaseGTIN, Description, Description2, FrontImage, RearImage, Layflat, Perishable,
                IsMultiPack, IsVarietyPack, IsDisplayShipper, PalletUPC, PalletWeightLbs, PalletUOM, PalletTie, PalletHigh
                FROM MasterDataTable 
                WHERE BrandName = ? 
                AND ProductStyle = ? 
                AND ProductFlavor = ? """,
            brandName, productStyle, productFlavor)
            marketingData = self.cursor.fetchone()
            return marketingData
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            data = []
            for i in range (0,100):
                data.append("None")
            return data
    
    def insertIntoMarketing(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE MasterDataTable SET Format = ?, FoodServiceBulkPack = ?, EachUPC = ?,
            EachWeight = ?, EachUOM = ?, QtyPerInner = ?, InnerPackUPC = ?, InnerWeight = ?,
            InnerUOM = ?, QtyPerCase = ?, CaseUPC = ?, CaseWeightLbs = ?, CaseUOM = ?,
            QtyCasesperPallet = ?, CaseGTIN = ?, Description = ?, Description2 = ?,
            FrontImage = ?, RearImage = ?, Layflat = ?, Perishable = ?,
            IsMultiPack = ?, IsVarietyPack = ?, IsDisplayShipper = ?, PalletUPC = ?, PalletWeightLbs = ?, PalletUOM = ?,
            PalletTie = ?, PalletHigh = ? 
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?)) """, conv_list)
        self.con.commit()

    
    def selectSupplyPlanning(self, brandName, productStyle, productFlavor):
        try:
            self.cursor.execute("""SELECT  
                MinOrderCases, Warehouse, PalletPickPriority, FreightClass, NMFC, Manufacturer
                FROM MasterDataTable
                WHERE BrandName = ?
                AND ProductStyle = ? 
                AND ProductFlavor = ? """, 
            brandName, productStyle, productFlavor)
            return self.cursor.fetchone()
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            data = []
            for i in range (0,100):
                data.append("None")
            return data

    def insertIntoSupplyPlanning(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE MasterDataTable SET MinOrderCases = ?, Warehouse = ?,
            PalletPickPriority = ?, FreightClass = ?, NMFC = ?, Manufacturer = ? 
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?)) """, conv_list)
        self.con.commit()


    def selectSales(self, brandName, productStyle, productFlavor):
        try:
            self.cursor.execute("""SELECT 
                DistributorDeliveredCaseCost, SRP, PlanogramDepth, PlanogramHeight, PlanogramWidth, VendorSKU
                FROM MasterDataTable
                WHERE BrandName = ?
                AND ProductStyle = ? 
                AND ProductFlavor = ? """, 
            brandName, productStyle, productFlavor)
            return self.cursor.fetchone()
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            data = []
            for i in range (0,100):
                data.append("None")
            return data

    def insertIntoSales(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE MasterDataTable SET DistributorDeliveredCaseCost =?, SRP = ?,
            PlanogramDepth = ?, PlanogramHeight = ?, PlanogramWidth = ?, VendorSKU = ?
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()


    def selectPackaging(self, brandName, productStyle, productFlavor):
        try:
            self.cursor.execute("""SELECT 
                EachHeight, EachWidth, EachDepth, InnerHeight, InnerWidth, InnerDepth,
                CaseHeight, CaseWidth, CaseDepth, CaseCube, PalletHeight, PalletWidth, PalletDepth, 
                PackagingDieline, PackagingSpec, CaseDieline, PalletConfig
                FROM MasterDataTable
                WHERE BrandName = ?
                AND ProductStyle = ? 
                AND ProductFlavor = ? """, 
            brandName, productStyle, productFlavor)
            return self.cursor.fetchone()
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            data = []
            for i in range (0,100):
                data.append("None")
            return data

    def insertIntoPackaging(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE MasterDataTable SET EachHeight = ?, EachWidth = ?, EachDepth = ?, InnerHeight = ?,
            InnerWidth = ?, InnerDepth = ?, CaseHeight = ?, CaseWidth = ?, CaseDepth = ?, CaseCube = ?,
            PalletHeight = ?, PalletWidth = ?, PalletDepth = ?, PackagingDieline = ?, PackagingSpec = ?,
            CaseDieline = ?, PalletConfig = ?
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()


    def selectQuality(self, brandName, productStyle, productFlavor):
        try:    
            self.cursor.execute("""SELECT 
                CountryOfOriginName, CodeDateExample, CodeDateFormula, CodeDateType, CodeDateStamp,
                ShelfLifeDaysGuarantee, ShelfLifeDaysAtProduction, ShippingCondition, StorageCondition,
                ShippingTemperatureRangeHigh, ShippingTemperatureRangeLow, StorageTemperatureRangeHigh, 
                StorageTemperatureRangeLow, NFP, Ingredients
                FROM MasterDataTable
                WHERE BrandName = ?
                AND ProductStyle = ? 
                AND ProductFlavor = ? """, 
            brandName, productStyle, productFlavor)
            return self.cursor.fetchone()
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            data = []
            for i in range (0,100):
                data.append("None")
            return data

    def insertIntoQuality(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE MasterDataTable SET CountryOfOriginName = ?, CodeDateExample = ?, CodeDateFormula = ?,
            CodeDateType = ?, CodeDateStamp = ?, ShelfLifeDaysGuarantee = ?, ShelfLifeDaysAtProduction = ?,
            ShippingCondition = ?, StorageCondition = ?, ShippingTemperatureRangeHigh = ?, ShippingTemperatureRangeLow = ?, 
            StorageTemperatureRangeHigh = ?, StorageTemperatureRangeLow = ?, NFP = ?, Ingredients = ?
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()


    def selectFinance(self, brandName, productStyle, productFlavor):
        try:
            self.cursor.execute("""SELECT 
                UnitCost, CaseCost, InternalItemNumber
                FROM MasterDataTable
                WHERE BrandName = ?
                AND ProductStyle = ? 
                AND ProductFlavor = ? """, 
            brandName, productStyle, productFlavor)
            return self.cursor.fetchone()
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            data = []
            for i in range (0,100):
                data.append("None")
            return data

    def insertIntoFinance(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE MasterDataTable SET UnitCost = ?, CaseCost = ?, InternalItemNumber = ?
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()

    def selectImg(self, brandName, productStyle, productFlavor):
        try:
            self.cursor.execute("""SELECT
                Icon FROM MasterDataTable 
                WHERE BrandName = ?
                AND ProductStyle = ?
                AND ProductFlavor = ? """,
            brandName, productStyle, productFlavor)

            data  = self.cursor.fetchone()[0]
            crudeImg = None
            if data:
                crudeImg = Image.open(io.BytesIO(data))
                crudeImg = crudeImg.resize((300,150), Image.ANTIALIAS)
            return crudeImg
        except Exception as ex:
            print(type(ex))
            print(ex.args)
            return None




    def insertPhoto(self, brandName, productStyle, productFlavor, img_bytes):
        self.cursor.execute("""UPDATE MasterDataTable SET Icon = ? 
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?))""",
           img_bytes, brandName, productStyle, productFlavor)
        self.con.commit()

    def insertUser(self, email, role):
        try:
            self.cursor.execute("""insert into [dbo].[users] ([email], [role]) 
                select * from ( 
                    values (?,?) -- sample value 
                ) as s([email], [role]) 
                where not exists ( 
                    select * from [dbo].[users] t with (updlock) 
                    where s.[email] = t.[email] and s.[role] = t.[role] 
                )""", email, role)
            self.con.commit()
        except Exception:
            print("inserting user in database??? insertUser()")
            
    def getUsers(self):
        self.cursor.execute("""SELECT * FROM [dbo].[users]""")
        data = self.cursor.fetchall()

        return data

    def getUserByEmail(self, email):
        self.cursor.execute("""SELECT email,role 
        FROM [dbo].[users] 
        WHERE email = ?""", email)

        return self.cursor.fetchone()

    def updateUserRole(self, email, role):
        try:
            print(role, email)
            self.cursor.execute("""UPDATE [dbo].[users] SET role = ? WHERE email = ?""", role, email)
            self.cursor.commit()
        except Exception as ex:
            print(ex)

    def __del__(self):
        self.con.close()
        
db = DB();
