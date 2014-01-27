from errors import *
import numpy as np
#from elements import *

ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
etableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\main\elements2.txt'

class Chemistry():pass

class Reactions(Chemistry): pass

class Element(Chemistry):

    def __init__(self):pass
    def getNum(self):
        return self.number
    def getMass(self):
        return self.mass
    def getName(self):
        return self.name
    def getSymbol(self):
        return self.symbol    
    def getRadius(self):
        return self.radius        
    def getEneg(self):
        return self.electronegativity        
    def getOx(self):
        return self.oxidation
    def getCharge(self):
        return self.charge
    def getBonds(self):
        return self.bondList
    def getInc(self):
        return self.inc
    def addBond(self,aBond):
        bondList.append(aBond)
    def breakBond(self,index):
        try:
            del bondList[index]
        except:
            print "No bond at this location"
    def changeBond(self,newBond,index):
        try:
            bondList[index] = newBond
        except:
            self.addBond(newBond)

class Hydrogen(Element):
    
    def __init__(self,aNum):
        self.number = 1
        self.mass = 1.00794
        self.name = 'Hydrogen'
        self.symbol = 'H'
        self.radius = 1
        self.electronegativity = 2.2
        self.oxidation = 1
        self.charge = 0
        self.bondList = []
        self.inc = aNum
            
class Carbon(Element):
    
    def __init__(self,aNum):
        self.number = 6
        self.mass = 12.0107
        self.name = 'Carbon'
        self.symbol = 'C'
        self.radius = 1
        self.electronegativity = 2.55
        self.oxidation = 4
        self.charge = 0
        self.bondList = []
        self.inc = aNum            
              
class Nitrogen(Element):
    
    def __init__(self,aNum):
        self.number = 7
        self.mass = 14.0067
        self.name = 'Nitrogen'
        self.symbol = 'N'
        self.radius = 1
        self.electronegativity = 3.04
        self.oxidation = -3
        self.charge = 0
        self.bondList = []
        self.inc = aNum        
              
class Oxygen(Element):
    
    def __init__(self,aNum):
        self.number = 8
        self.mass = 15.9994
        self.name = 'Oxygen'
        self.symbol = 'O'
        self.radius = 1
        self.electronegativity = 3.44
        self.oxidation = -2
        self.charge = 0
        self.bondList = []
        self.inc = aNum              
                     
class Fluorine(Element):
    
    def __init__(self,aNum):
        self.number = 9
        self.mass = 18.9984032
        self.name = 'Fluorine'
        self.symbol = 'F'
        self.radius = 1
        self.electronegativity = 3.98
        self.oxidation = -1
        self.charge = 0
        self.bondList = []
        self.inc = aNum       

class Sulfur(Element):
    
    def __init__(self,aNum):
        self.number = 16
        self.mass = 32.065
        self.name = 'Sulfur'
        self.symbol = 'S'
        self.radius = 1
        self.electronegativity = 2.58
        self.oxidation = -2
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Chlorine(Element):
    
    def __init__(self,aNum):
        self.number = 17
        self.mass = 35.453
        self.name = 'Chlorine'
        self.symbol = 'Cl'
        self.radius = 1
        self.electronegativity = 3.16
        self.oxidation = -1
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                             
class Iodine(Element):
    
    def __init__(self,aNum):
        self.number = 53
        self.mass = 126.904
        self.name = 'Iodine'
        self.symbol = 'I'
        self.radius = 1
        self.electronegativity = 2.66
        self.oxidation = -1
        self.charge = 0
        self.bondList = []
        self.inc = aNum                   
                                      
class Bromine(Element):
    
    def __init__(self,aNum):
        self.number = 35
        self.mass = 79.904
        self.name = 'Bromine'
        self.symbol = 'Br'
        self.radius = 1
        self.electronegativity = 2.96
        self.oxidation = -1
        self.charge = 0
        self.bondList = []
        self.inc = aNum    
        
theDict = {} 
        
class Bond(Chemistry):
    
    def __init__(self,start,end,order):
        self.start = start
        self.end = end
        self.degree = order
        
    def getStart(self):
        return self.start        
    def getEnd(self):
        return self.end
    def getOrder(self):
        return self.degree
    def newOrder(self,nOrder):
        self.degree = nOrder
    def __str__(self):
        if self.degree == 1:
            return 'sb'
        elif self.degree == 2:
            return 'db'
        elif self.degree == 3:
            return 'tb'
        else:
            raise InvalidBondException

class Mendeleev(Chemistry):
    
    def __init__(self,loc1,loc2):
        """Creates a periodic table of the elements. Only call this once"""
        
        #generates an array of 1s and 0s to create the shape of the periodic table     
        ptable = np.genfromtxt(loc1,dtype='S',unpack=True)
        eTable = np.genfromtxt(loc2,dtype='S',unpack=True)
        tempTable = ptable.reshape((7,32))
        theTable = []
        #Do something to open the text file at loc2 here
        
        #Populates the periodic table with element objects
        inc = 0
        for i in range(7):
            for j in range(32):
                if tempTable[i][j] == '0':
                    theTable.append(None)
                else:
                    theTable.append(eval(eTable[inc]))
        
        #shapes the periodic table        
        self.finalTable = np.array(theTable).reshape((7,32))
    
    def getTable(self):
        """returns the numpy array that serves as the periodic table"""            
        return self.finalTable
    
    def __str__(self):
        """String representation of the periodic table"""
        return stringify(self.finalTable)#"The Periodic Table of the Elements"

def stringify(anObject):
    """takes an array and converts every object within to a string"""
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        newList = range(len(anObject))
        for i in range(len(anObject)):
            newList[i] = stringify(anObject[i])
        return newList
    if type(anObject) == type(''):return anObject
    if anObject == None:return anObject
    else:return str(anObject)  
    
def toElement(anObject):
    """"""
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        for i in range(len(anObject)):
            anObject[i] = toElement(anObject[i])
        return anObject
    
    if type(anObject) == type(''):
        for part in anObject:
            if part in ['+','*','@','!']:
                return anObject
        return eval(theDict[anObject])
        
def populate(anObject): 
    """"""
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        try:
            if '@' in anObject[0]:
                return [anObject[0],populate(anObject[1:][0])]
        except:pass
        try:
            locDict = {}
            for i in range(len(anObject)):
                try:locDict[i] = int(anObject[i])
                except (ValueError, AttributeError,TypeError):pass
                    
            locKeys = locDict.keys()
            if len(locKeys) == 0:raise Exception
            locKeys.sort();locKeys.reverse()
            
            for item in locKeys:
                amount = locDict[item]
                anObject.pop(item)
                if amount == 1:
                    anObject[item-1] = populate(anObject[item-1])
                for i in range(amount-1):
                    anObject.insert(item,populate(anObject[item-1]))
            return anObject
                
        except:
            for i in range(len(anObject)):
                anObject[i] = populate(anObject[i])
            return anObject
            
    if type(anObject) == type(''):
        return anObject  