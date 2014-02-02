import numpy as np
    
# atomic data gotten from:
# http://en.wikipedia.org/wiki/List_of_elements
# http://en.wikipedia.org/wiki/Atomic_radii_of_the_elements_(data_page)
# atomic weight in u()
# Density in g/cm^3
# Melting, Boiling Point in K
# Heat J/g*K
# Calculated radius in pm
at = "C:\\Users\Dan\Documents\GitHub\Chemistry\Main/at.txt"
num,symb,element,group,weight,density,melt,boil,heat,eneg,rad = np.genfromtxt(at,dtype='S',unpack=True)
aString = ''

someFile = open('C:\\Users\Dan\Documents\GitHub\Chemistry\Main/sometext.txt','r')
bString = ''
i=0
for line in someFile:
    tList = line.split()
    if len(tList) == 1:
        bString += '0'
    for part in tList[1:]:
        if part == 'nodata':
            bString += 'No_Data\n'
        elif part != tList[-1]:
            bString += part + ','
        else:
            bString += part + '\n'
    print tList,i
    i += 1 
bList = bString.split()
someFile.close()

for i in range(len(num)):
    aString += num[i]+' '
    aString += symb[i]+' '
    aString += element[i]+' '
    aString += group[i]+' '
    aString += weight[i]+' '
    aString += density[i] + ' '
    aString += melt[i] + ' ' 
    aString += boil[i] + ' ' 
    aString += heat[i] + ' '
    aString += eneg[i] + ' '    
    aString += rad[i] + ' '
    aString += '[' + bList[i] + '] '
    aString += '\n'
someFile = open('C:\\Users\Dan\Documents\GitHub\Chemistry\Main/ab.txt','w')
someFile.write(aString)
someFile.close()
aList = aString.split()
aList = np.array(aList).reshape(119,11)    
            
startString = "class Chemistry():pass"
startString += "\n\nclass Element(Chemistry):"
startString += "\n    def __init__(self):pass"
startString += "\n    def getNum(self):return self.number"
startString += "\n    def getMass(self):return self.mass"
startString += "\n    def getName(self):return self.name"
startString += "\n    def getSymbol(self):return self.symbol"
startString += "\n    def getRadius(self):return self.radius"
startString += "\n    def getEneg(self):return self.electronegativity"
startString += "\n    def getOx(self):return self.oxidation"
startString += "\n    def getCharge(self):return self.charge"
startString += "\n    def getBonds(self):return self.bondList"
startString += "\n    def addBond(self,aBond):self.bondList.append(aBond)"
startString += "\n    def breakBond(self,index):"
startString += "\n        try:del self.bondList[index]"
startString += "\n        except:print 'No bond at this location'"
startString += "\n    def changeBond(self,newBond,index):"
startString += "\n        try:self.bondList[index] = newBond"
startString += "\n        except:self.addBond(newBond)"
startString += "\n    def getHeat(self):return self.heat"
startString += "\n    def getBoil(self):return self.bp"
startString += "\n    def getMelt(self):return self.mp"
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
startString += "\n    def __str__(self):return self.name\n"

mainString = '\n'
num,symb,element,group,weight,density,melt,boil,heat,eneg,rad
for i in range(1,len(aList)):
    mainString += "class " + aList[i][2] + "(Element):"
    mainString += "\n    def __init__(self):\n        self.number = " + aList[i][0]
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
    mainString += "\n        self.oxidation = " + aList[i][10]
    mainString += "\n        self.charge = 0"
    mainString += "\n        self.bondList = []"
    if i != 118:
        mainString += '\n\n'
    
elementString = startString + mainString

someFile = open('C:\Users\Dan\Documents\GitHub\Chemistry\Main/elements1.py','w')
someFile.write(elementString)
someFile.close()