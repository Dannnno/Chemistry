import numpy as np
import re
atomicFamilies = {1:"Alkali Metals",2:"Alkaline Earth Metals",3:"Transition Metals",4:"Transition Metals",5:"Transition Metals",6:"Transition Metals",7:"Transition Metals",8:"Transition Metals",9:"Transition Metals",10:"Transition Metals",11:"Transition Metals",12:"Transition Metals",13:"13",14:"14",15:"15",16:"16",17:"Halogens",18:"Noble Gases",19:"Lanthanoids",20:"Actinoids"}
class Chemistry: pass
class Element(Chemistry):        
    def __init__(self,mass,number,symbol,name,electronegativity,family):
        self.atomicMass = mass
        self.atomicNumber = number
        self.atomicSymbol = symbol
        self.elementName = name
        self.electroneg = electronegativity
        self.atomicFamily = family
        self.bondList = []          
    def __str__(self):
        return self.elementName
    def getmass(self):
        return self.atomicMass
    def getnumber(self):
        return self.atomicNumber
    def getname(self):
        return self.elementName        
    def getsymbol(self):
        return self.atomicSymbol
    def getneg(self):
        return self.electroneg        
    def makeBond(self,end,order=1,abool = False):
        self.bondList.append(Bond(self,end,order))
    def getBonds(self):
        return self.bondList
    def getfam(self):
        return atomicFamilies[int(self.atomicFamily)]        
class Mendeleev(Chemistry):            
    def __init__(self,loc1,loc2):
        ptable = np.genfromtxt(loc1,dtype='S', unpack=True)
        tempTable = ptable.reshape((7,32))
        theTable = []
        n, symbol, name, family, mass, eneg = np.genfromtxt(loc2, dtype='S', unpack=True)
        nList = n.astype(int)
        nameList = name.astype(str)
        symList = symbol.astype(str)
        famList = family.astype(int)
        massList = mass.astype(float)
        negList = eneg.astype(float)
        inc=0
        for i in range(7):
            for j in range(32):
                if tempTable[i][j] == '0':
                    theTable.append(None)
                else:
                    theTable.append(Element(massList[inc],nList[inc],symList[inc],nameList[inc],negList[inc],famList[inc]))
                    inc+=1  
        self.finalTable = np.array(theTable).reshape((7,32))
    def getTable(self):
        return self.finalTable        
    def printableTable(self):
        stringVal = ''
        for rows in self.finalTable:
            for columns in rows:
                if columns != None:
                    stringVal += str(columns)+'\n'
        return stringVal
    def getElement(self,symbol):
        for rows in self.finalTable:
            for columns in self.finalTable:
                for atom in columns:
                    if atom != None:
                        if symbol == atom.getsymbol():
                            return atom    
    def __str__(self):
        return "The Periodic Table of the Elements"
class Bond(Chemistry):
    def __init__(self,start,end,order):
        self.startElement = start
        self.endElement = end
        self.order = order
        if self.order == 1:            
            self.descriptor = 'single'
        elif self.order == 2:
            self.descriptor = 'double'
        elif self.order == 3:
            self.descriptor = 'triple'
        else:
            self.descriptor = None    
    def getStart(self):
        return self.startElement
    def getEnd(self):
        return self.endElement
    def getOrder(self):
        return self.order
    def getDescrip(self):
        return self.descriptor   
    def __str__(self):
        if self.order == 1:
            return 'sb'
        elif self.order == 2:
            return 'db'
        elif self.order == 3:
            return 'tb'
        else:
            return 'None'
def branching(anObject,structure,location):
    primary = anObject[0]
    tempsec = anObject[1:]
    secondaries = []
    for subs in tempsec:
        for length in range(subs[-1]):
            secondaries.append(subs[0])            
    locX = location[0]
    locY = location[1]
    structure[locY][locX] = primary
    cardinals = [structure[locY-2][locX],
                 structure[locY][locX-2],
                 structure[locY+2][locX],
                 structure[locY][locX+2]]
    status = []
    for direction in cardinals:
        if direction == None:
            status.append(True)
        else:
            status.append(False)                
    i=1
    j=0
    for point in status:
        if j <= len(secondaries)-1:
            if point:
                if i == 1:
                    structure[locY-2][locX] = secondaries[j]
                    structure[locY-1][locX] = Bond(primary,secondaries[j],1)
                    primary.makeBond(secondaries[j])
                if i == 2:
                    structure[locY][locX-2] = secondaries[j]
                    structure[locY][locX-1] = Bond(primary,secondaries[j],1)
                    primary.makeBond(secondaries[j])
                if i == 3:
                    structure[locY+2][locX] = secondaries[j]
                    structure[locY+1][locX] = Bond(primary,secondaries[j],1)
                    primary.makeBond(secondaries[j])
                if i == 4:
                    structure[locY][locX+2] = secondaries[j]
                    structure[locY][locX+1] = Bond(primary,secondaries[j],1)
                    primary.makeBond(secondaries[j])
                j +=1
        else:
            if i == 1:
                structure[locY-2][locX] = None
            if i == 2:
                structure[locY][locX-2] = None
            if i == 3:
                structure[locY+2][locX] = None
            if i == 4:
                structure[locY][locX+2] = None
        i+=1
    return structure
ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
elementsLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\elements.txt'        
theTable = Mendeleev(ptableLoc,elementsLoc)          
def stringify(anArray):
    height = len(anArray)
    width = len(anArray[0])
    newArray = np.empty((width,height),dtype=object)
    for i in range(height):
        for j in range(width):
            newArray[i][j] = str(anArray[i][j])                                    
    return newArray                                                        
class Compound(Chemistry):
    def __init__(self,formula):   
        self.formula = formula
        self.centers = formula.split()
        size = (3*len(self.centers)+1)**2
        sidelen = int(np.sqrt(size))
        self.structure = np.empty((sidelen,sidelen), dtype = object)
        numList = ['1','2','3','4','5','6','7','8','9']
        inc = 0
        for part in self.centers:
            theCenter = [part[0]]
            theRest = re.split('(\d+)',part[1:])[:-1]
            trueRest = [theRest[i]+theRest[i+1] for i in range(0,len(theRest),2)]
            self.centers[inc] = theCenter+trueRest
            inc += 1
        for part in self.centers:
            for substituent in range(1,len(part)):
                part[substituent] = re.split('(\d+)',part[substituent])[:-1]
        for part in range(len(self.centers)):
            for i in range(len(self.centers[part])):
                if str(type(self.centers[part][i])) == "<type 'str'>":
                    tempSub = theTable.getElement(self.centers[part][i])
                    self.centers[part][i] = tempSub
                elif str(type(self.centers[part][i])) == "<type 'list'>":
                    for j in range(len(self.centers[part][i])):
                        if self.centers[part][i][j][0:1] not in numList:
                            tempSubSub = theTable.getElement(self.centers[part][i][j])
                            self.centers[part][i][j]  = tempSubSub
                        else:
                            self.centers[part][i][j] = int(self.centers[part][i][j])          
        middle = int(len(self.structure)/2)
        i=middle
        j=2
        k=0
        while k < len(self.centers):
            self.structure = branching(self.centers[k],self.structure,[j,i])
            k+=1
            j+=2            
        print stringify(self.structure)
        print self.structure[3][2].getBonds()
        for i in range(len(self.centers)): pass
    def __str__(self):
        return str(self.formula)  
def BeginProgram():
    testCompound = Compound("CH1Cl2 CH3")  
    print testCompound
BeginProgram()