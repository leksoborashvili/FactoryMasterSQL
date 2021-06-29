import pyodbc
import io
from PIL import  Image, ImageTk


class DB:

    def __init__(self):
        server = 'factorydataserver.database.windows.net'
        database = 'DataBase1'
        username = 'Kpursell'
        password = 'F@ct0ry315'
        driver= '{ODBC Driver 17 for SQL Server}'
        with pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
            self.con = conn
        #self.con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\LeksoBorashvili\source\repos\test\test\masterData.accdb;')
        self.cursor = self.con.cursor()


    def createObject(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""INSERT INTO MasterDataTable (BrandName, ProductStyle, ProductFlavor)
                            VALUES(?,?,?) """, brandName, productStyle, productFlavor)
        self.cursor.commit()


    def selectMarketing(self, brandName, productStyle, productFlavor):
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
        self.cursor.execute("""SELECT  
            MinOrderCases, Warehouse, PalletPickPriority, FreightClass, NMFC, Manufacturer
            FROM MasterDataTable
            WHERE BrandName = ?
            AND ProductStyle = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


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
        self.cursor.execute("""SELECT 
            DistributorDeliveredCaseCost, SRP, PlanogramDepth, PlanogramHeight, PlanogramWidth, VendorSKU
            FROM MasterDataTable
            WHERE BrandName = ?
            AND ProductStyle = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


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
        self.cursor.execute("""SELECT 
            UnitCost, CaseCost, InternalItemNumber
            FROM MasterDataTable
            WHERE BrandName = ?
            AND ProductStyle = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


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

    def insertPhoto(self, brandName, productStyle, productFlavor, img_bytes):
        self.cursor.execute("""UPDATE MasterDataTable SET Icon = ? 
            WHERE ((BrandName = ?) 
            AND (ProductStyle = ?) 
            AND (ProductFlavor = ?))""",
           img_bytes, brandName, productStyle, productFlavor)
        self.con.commit()
    def __del__(self):
        self.con.close()
        
db = DB();
