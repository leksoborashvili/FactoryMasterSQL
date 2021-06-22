import pyodbc



class DB:

    def __init__(self):
        self.con = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\LeksoBorashvili\source\repos\test\test\masterData.accdb;')
        self.cursor = self.con.cursor()


    def selectMarketing(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""SELECT Format, FoodServiceBulkPack, EachUPC,
            EachWeight, EachUOM, QtyPerInner, InnerPackUPC, InnerWeight, InnerUOM, QtyPerCase, CaseUPC, CaseWeight, CaseUOM,
            QtyCasesperPallet, CaseGTIN, [Short Description], [Long Description], FrontImage, RearImage, Layflat, Perishable,
            IsMultiPack, IsVarietyPack, IsDisplayShipper, PalletUPC, PalletWeight, PalletUOM, PalletTi, PalletHi
            FROM [Master Table] 
            WHERE BrandName = ? 
            AND [ProductStyle /Category] = ? 
            AND ProductFlavor = ? """,
        brandName, productStyle, productFlavor)
        marketingData = self.cursor.fetchone()
        return marketingData

    
    def insertIntoMarketing(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE [Master Table] SET Format = ?, FoodServiceBulkPack = ?, EachUPC = ?,
            EachWeight = ?, EachUOM = ?, QtyPerInner = ?, InnerPackUPC = ?, InnerWeight = ?,
            InnerUOM = ?, QtyPerCase = ?, CaseUPC = ?, CaseWeight = ?, CaseUOM = ?,
            QtyCasesperPallet = ?, CaseGTIN = ?, [Short Description] = ?, [Long Description] = ?,
            FrontImage = ?, RearImage = ?, Layflat = ?, Perishable = ?,
            IsMultiPack = ?, IsVarietyPack = ?, IsDisplayShipper = ?, PalletUPC = ?, PalletWeight = ?, PalletUOM = ?,
            PalletTi = ?, PalletHi = ? 
            WHERE ((BrandName = ?) 
            AND ([ProductStyle /Category] = ?) 
            AND (ProductFlavor = ?)) """, conv_list)
        self.con.commit()

    
    def selectSupplyPlanning(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""SELECT  
            MinOrderCases, Warehouse, PalletPickPriority, FreightClass, NMFC, Manufacture
            FROM [Master Table]
            WHERE BrandName = ?
            AND [ProductStyle /Category] = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


    def insertIntoSupplyPlanning(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE [Master Table] SET MinOrderCases = ?, Warehouse = ?,
            PalletPickPriority = ?, FreightClass = ?, NMFC = ?, Manufacture = ? 
            WHERE ((BrandName = ?) 
            AND ([ProductStyle /Category] = ?) 
            AND (ProductFlavor = ?)) """, conv_list)
        self.con.commit()


    def selectSales(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""SELECT 
            DistributorDeliveredCasePrice, SRP, PlanogramDepth, PlanogramHeight, PlanogramWidth, VendorSKU
            FROM [Master Table]
            WHERE BrandName = ?
            AND [ProductStyle /Category] = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


    def insertIntoSales(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE [Master Table] SET DistributorDeliveredCasePrice =?, SRP = ?,
            PlanogramDepth = ?, PlanogramHeight = ?, PlanogramWidth = ?, VendorSKU = ?
            WHERE ((BrandName = ?) 
            AND ([ProductStyle /Category] = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()


    def selectPackaging(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""SELECT 
            EachHeight, EachWidth, EachDepth, InnerHeight, InnerWidth, InnerDepth,
            CaseHeight, CaseWidth, CaseDepth, CaseCube, PalletHeight, PalletWidth, PalletDepth, 
            PackagingDieline, PackagingSpec, CaseDieline, PalletConfig
            FROM [Master Table]
            WHERE BrandName = ?
            AND [ProductStyle /Category] = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


    def insertIntoPackaging(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE [Master Table] SET EachHeight = ?, EachWidth = ?, EachDepth = ?, InnerHeight = ?,
            InnerWidth = ?, InnerDepth = ?, CaseHeight = ?, CaseWidth = ?, CaseDepth = ?, CaseCube = ?,
            PalletHeight = ?, PalletWidth = ?, PalletDepth = ?, PackagingDieline = ?, PackagingSpec = ?,
            CaseDieline = ?, PalletConfig = ?
            WHERE ((BrandName = ?) 
            AND ([ProductStyle /Category] = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()


    def selectQuality(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""SELECT 
            CountryOfOriginName, CodeDateExample, CodeDateFormula, CodeDateType, CodeDateStamp,
            ShelfLifeDaysGuarantee, ShelfLifeDaysAtProduction, ShippingCondition, StorageCondition,
            ShippingTemperatureRangeHigh, ShippingTemperatureRangeLow, StorageTemperatureRangeHigh, 
            StorageTemperatureRangeLow, NFP, Ingredients
            FROM [Master Table]
            WHERE BrandName = ?
            AND [ProductStyle /Category] = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


    def insertIntoQuality(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE [Master Table] SET CountryOfOriginName = ?, CodeDateExample = ?, CodeDateFormula = ?,
            CodeDateType = ?, CodeDateStamp = ?, ShelfLifeDaysGuarantee = ?, ShelfLifeDaysAtProduction = ?,
            ShippingCondition = ?, StorageCondition = ?, ShippingTemperatureRangeHigh = ?, ShippingTemperatureRangeLow = ?, 
            StorageTemperatureRangeHigh = ?, StorageTemperatureRangeLow = ?, NFP = ?, Ingredients = ?
            WHERE ((BrandName = ?) 
            AND ([ProductStyle /Category] = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()


    def selectFinance(self, brandName, productStyle, productFlavor):
        self.cursor.execute("""SELECT 
            UnitCost, CaseCost, [Internal Item Numberr]
            FROM [Master Table]
            WHERE BrandName = ?
            AND [ProductStyle /Category] = ? 
            AND ProductFlavor = ? """, 
        brandName, productStyle, productFlavor)
        return self.cursor.fetchone()


    def insertIntoFinance(self, brandName, productStyle, productFlavor, values):
        conv_list = list(values)
        conv_list.append(brandName)
        conv_list.append(productStyle)
        conv_list.append(productFlavor)
        self.cursor.execute("""UPDATE [Master Table] SET UnitCost = ?, CaseCost = ?, [Internal Item Numberr] = ?
            WHERE ((BrandName = ?) 
            AND ([ProductStyle /Category] = ?) 
            AND (ProductFlavor = ?))""", conv_list)
        self.con.commit()


    def __del__(self):
        self.con.close()
        
db = DB();
