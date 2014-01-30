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

for i in range(len(num)):
    aString += num[i]+' '
    aString += symb[i]+' '
    aString += element[i]+' '
    aString += group[i]+' '
    if weight[i].rfind('(') != -1:weight[i] = weight[i][:weight[i].rfind('(')]
    elif weight[i][0] == '[':weight[i] = weight[i][1:4]
    else:pass
    aString += weight[i]+' '
    if density[i] == 'nodata':aString += "'No_Data' "
    elif '(' in density[i]: aString += density[i][density[i].find('(')+1:density[i].find(')')]+' '
    else: aString += density[i] + ' '
    if melt[i] == 'nodata':aString += "'No_Data' "
    elif '[' in melt[i]:aString += melt[i][:melt[i].find('[')]+' '
    elif '(' in melt[i]: aString += melt[i][melt[i].find('(')+1:melt[i].find(')')]+' '
    else: aString += melt[i] + ' ' 
    if boil[i] == 'nodata':aString += "'No_Data' "
    elif '(' in boil[i]: aString += boil[i][boil[i].find('(')+1:boil[i].find(')')]+' '
    else: aString += boil[i] + ' ' 
    if heat[i] == 'nodata':aString += "'No_Data' "
    else: aString += heat[i] + ' '
    if eneg[i] == 'nodata':aString += "'No_Data' "
    else: aString += eneg[i] + ' '    
    if rad[i] == 'nodata':aString += "'No_Data' "
    else: aString += rad[i] + ' '
    aString += '\n'

aList = aString.split()
aList = np.array(aList).reshape(119,11)    
            
startString = "class Chemistry():pass \n\nclass Element(Chemistry):\n    def __init__(self):pass\n    def getNum(self):return self.number\n    def getMass(self):return self.mass\n    def getName(self):return self.name\n    def getSymbol(self):return self.symbol\n    def getRadius(self):return self.radius\n    def getEneg(self):return self.electronegativity\n    def getOx(self):return self.oxidation\n    def getCharge(self):return self.charge\n    def getBonds(self):return self.bondList\n    def addBond(self,aBond):self.bondList.append(aBond)\n    def breakBond(self,index):\n        try:del self.bondList[index]\n        except:print 'No bond at this location'\n    def changeBond(self,newBond,index):\n        try:self.bondList[index] = newBond\n        except:self.addBond(newBond)\n"
startString += "    def getHeat(self):return self.heat\n    def getBoil(self):return self.bp\n    def getMelt(self):return self.mp\n"
mainString = '\n'
for i in range(1,len(aList)):
    mainString += "class " + aList[i][2] + "(Element):\n    "
    mainString += "def __init__(self):\n        self.number = " + aList[i][0] + '\n        '
    mainString += "self.mass = " + aList[i][4] + "\n        "
    mainString += "self.name = " + "'" + aList[i][2] + "'" + "\n        "
    mainString += "self.symbol = "  + "'" + aList[i][1] + "'" + "\n        "
    mainString += "self.group = " + aList[i][3] + "\n        "
    mainString += "self.radius = " + aList[i][-1] +"\n        "
    mainString += "self.electronegativity = " + aList[i][-2] + "\n        "
    mainString += "self.oxidation = None\n        "
    mainString += "self.charge = 0\n        "
    mainString += "self.bondList = []\n        "
    mainString += "self.heat = " + aList[i][-3] + "\n        "
    mainString += "self.bp = " + aList[i][-4] + "\n        "
    if i != 118:mainString += "self.mp = " + aList[i][-5] + "\n\n"
    else:mainString += "self.mp = " + aList[i][-5] 
    
elementString = startString + mainString

someFile = open('C:\Users\Dan\Documents\GitHub\Chemistry\Main/elements1.py','w')
someFile.write(elementString)
someFile.close()