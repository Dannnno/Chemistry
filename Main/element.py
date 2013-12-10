import numpy as np

class Element:
        
    def __init__(self,
                 mass,
                 number,
                 symbol,
                 name,
                 electronegativity,
                 family):
                 
        """Creates an element object"""
       
        self.atomicMass = mass
        self.atomicNumber = number
        self.atomicSymbol = symbol
        self.elementName = name
        self.electroneg = electronegativity
        self.atomicFamily = family
        
    def __str__(self):
        """The string output of an element object is returned"""
        return ("This is the "+self.elementName+" element")
            
    def getmass(self):
        """float - returns the average atomic mass of the element"""
        return self.atomicMass
        
    def getnumber(self):
        """int - returns the atomic number of the element"""
        return self.atomicNumber
        
    def getname(self):
        """string - returns the name of the element"""
        return self.elementName
        
    def getsymbol(self):
        """string - returns the atomic symbol of the element"""
        return self.atomicSymbol
        
    def getneg(self):
        """"float - returns the electronegativity of the element"""
        return self.electroneg
        
    def getfam(self):
        """array - returns an array of elements within the family"""
        return periodicTable.getFam(self.atomicFamily)    
        
def createTable(loc1,loc2):
    """(string,string) => array[Element] 
    Creates an array that represents the periodic table - it takes two imputs, string values for the location of the generic ptable
    and the location of the list of elements and associated data, then returns a shaped array of the Elements"""

    ptable = np.genfromtxt(loc1,dtype='S', unpack=True)
    tempTable = ptable.reshape((7,32))
    periodicTable = []
    
    n, name, symbol, family, mass, eneg = np.genfromtxt(loc2, dtype='S', unpack=True)
    nList = n.astype(int)
    nameList = name.astype(str)
    symList = symbol.astype(str)
    famList = family.astype(int)
    massList = mass.astype(float)
    negList = eneg.astype(float)
    
    inc=1
    for i in range(7):
        for j in range(32):
            if tempTable[i][j] == 0:
                periodicTable.append(None)
            else:
                periodicTable.append(Element(massList[inc],
                                             nList[inc],
                                             symList[inc],
                                             nameList[inc],
                                             negList[inc],
                                             famList[inc]))
                inc+=1  
            
    return np.array(periodicTable).reshape((7,32))

ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\ptable.txt'
elementsLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\elements.txt'

periodicTable = createTable(ptableLoc,elementsLoc)