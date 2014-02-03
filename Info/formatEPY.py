aFile = open('C://Users/Dan/Documents/GitHub/Chemistry/Info/ab.txt','r')
aList = []
for line in aFile:
    if 'Num' not in line:
        aList.append(line.split())
    else:
        order = line

startString = "class Chemistry():"
startString += "\n    pass"
startString += "\n\nNo_Data = 'No_Data'"
startString += "\n\nclass Element(Chemistry):"
startString += "\n    def __init__(self):"
startString += "\n        pass"
startString += "\n    def getNum(self):"
startString += "\n        return self.number"
startString += "\n    def getMass(self):"
startString += "\n        return self.mass"
startString += "\n    def getName(self):"
startString += "\n        return self.name"
startString += "\n    def getSymbol(self):"
startString += "\n        return self.symbol"
startString += "\n    def getRadius(self):"
startString += "\n        return self.radius"
startString += "\n    def getEneg(self):"
startString += "\n        return self.electronegativity"
startString += "\n    def getOx(self):"
startString += "\n        return self.oxidation"
startString += "\n    def getCharge(self):"
startString += "\n        return self.charge"
startString += "\n    def getBonds(self):"
startString += "\n        return self.bondList"
startString += "\n    def addBond(self,aBond):"
startString += "\n        self.bondList.append(aBond)"
startString += "\n    def breakBond(self,aBond):"
startString += "\n        try:del self.bondList[self.bondList.find(aBond)]"
startString += "\n        except:print 'No bond at this location'"
startString += "\n    def changeBond(self,newBond,index):"
startString += "\n        try:self.bondList[index] = newBond"
startString += "\n        except:self.addBond(newBond)"
startString += "\n    def getHeat(self):"
startString += "\n        return self.heat"
startString += "\n    def getBoil(self):"
startString += "\n        return self.bp"
startString += "\n    def getMelt(self):"
startString += "\n        return self.mp"
startString += "\n    def formalCharge(self):"
startString += "\n        if self.group in [1,2,13,14,15,16,17]:"
startString += "\n            if self.group > 10:"
startString += "\n                valence = self.group - 10"
startString += "\n            else:"
startString += "\n                valence = self.group"
startString += "\n            nBonds = len(self.bondList)"
startString += "\n            nLPE = self.LPE"
startString += "\n            FC = valence - nBonds - nLPE"
startString += "\n            return FC"
startString += "\n    def __str__(self):"
startString += "\n        return self.name\n"

mainString = '\n'
for i in range(len(aList)):
    mainString += "class " + aList[i][2] + "(Element):"
    mainString += "\n    def __init__(self):"
    mainString += "\n        self.number = " + aList[i][0] 
    mainString += "\n        self.symbol = "  + "'" + aList[i][1] + "'"
    mainString += "\n        self.name = " + "'" + aList[i][2] + "'"
    mainString += "\n        self.group = " + aList[i][3]
    mainString += "\n        self.mass = " + aList[i][4]
    mainString += "\n        self.density = " + aList[i][5]
    mainString += "\n        self.melting = " + aList[i][6]
    mainString += "\n        self.boiling = " + aList[i][7]
    mainString += "\n        self.heat = " + aList[i][8]
    mainString += "\n        self.electronegativity = " + aList[i][9]
    mainString += "\n        self.radius = " + aList[i][10]
    mainString += "\n        self.oxidation = " + aList[i][11]
    mainString += "\n        self.charge = 0"
    mainString += "\n        self.bondList = []"
    if i != 117:
        mainString += '\n\n'
    
elementString = startString + mainString

someFile = open('C:\Users\Dan\Documents\GitHub\Chemistry\Info/elements.py','w')
someFile.write(elementString)
someFile.close()