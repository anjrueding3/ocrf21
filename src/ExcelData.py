class ExcelData:
    
    def __init__(self, IHD, PO, styleNum):
        self.IHD = IHD
        self.PO = PO
        self.styleNum = styleNum


    def getPO(self):
        return self.PO

    def getIHD(self):
        return self.IHD

    def getStyle(self):
        return self.styleNum

    def setIHD(self, newIHD):
        self.IHD = newIHD

    def setStyle(self, newStyleNum):
        self.styleNum = newStyleNum

    def getInfo(self):
        print('PO#: ' + str(self.PO) + '\nIHD: ' + self.IHD + '\nStyle Number: ' + self.styleNum) 






    
