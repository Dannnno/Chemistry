import numpy as np
import re

atomicFamilies = {1:"Alkali Metals",
                  2:"Alkaline Earth Metals",
                  3:"Transition Metals",
                  4:"Transition Metals",
                  5:"Transition Metals",
                  6:"Transition Metals",
                  7:"Transition Metals",
                  8:"Transition Metals",
                  9:"Transition Metals",
                  10:"Transition Metals",
                  11:"Transition Metals",
                  12:"Transition Metals",
                  13:"13",
                  14:"14",
                  15:"15",
                  16:"16",
                  17:"Halogens",
                  18:"Noble Gases",
                  19:"Lanthanoids",
                  20:"Actinoids"}

class Chemistry: pass

class Element(Chemistry):
        
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
        self.bondList = []
        #self.eDict = {self.atomicSymbol():self}        
        
    def __str__(self):
        """The string output of an element object is returned"""
        return self.elementName
            
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
        
    def getelement(self,symbol):
        """element - takes the symbol of an element and returns the element"""
        return self.eDict[symbol]
        
    def makeBond(self,end,order=1):
        """creates a bond object between the current element and another element, default order = 1"""
        self.bondList.append(Bond(self,end,order))
             
    def getfam(self):
        """returns a string that represents the atomic family of the element"""
        return atomicFamilies[int(self.atomicFamily)]
        
class Mendeleev(Chemistry):  
          
    def __init__(self,
                 loc1,
                 loc2):
        """Initializes the periodic Table of the Elements"""
        
        #generates an array of 1s and 0s to create the shape of the periodic table     
        ptable = np.genfromtxt(loc1,dtype='S', unpack=True)
        tempTable = ptable.reshape((7,32))
        theTable = []
        
        #Takes the data for each element and puts it into the appropriate list
        n, symbol, name, family, mass, eneg = np.genfromtxt(loc2, dtype='S', unpack=True)
        nList = n.astype(int)
        nameList = name.astype(str)
        symList = symbol.astype(str)
        famList = family.astype(int)
        massList = mass.astype(float)
        negList = eneg.astype(float)
        
        #Populates the periodic table with element objects
        inc=0
        for i in range(7):
            for j in range(32):
                if tempTable[i][j] == '0':
                    theTable.append(None)
                else:
                    anElement=Element(massList[inc],
                                      nList[inc],
                                      symList[inc],
                                      nameList[inc],
                                      negList[inc],
                                      famList[inc])
                    theTable.append(anElement)
                    inc+=1  
        
        #shapes the periodic table        
        self.finalTable = np.array(theTable).reshape((7,32))
    
    def getTable(self):
        """returns the numpy array that serves as the periodic table"""            
        return self.finalTable
        
    def printableTable(self):
        """returns the periodic table in a string format"""
        stringVal = ''
        for rows in self.finalTable:
            for columns in rows:
                if columns != None:
                    stringVal += str(columns)+'\n'
        return stringVal

    def getElement(self,
                   symbol):
        """Returns the appropriate element object given a string representation of the element's symbol"""
        
        for rows in self.finalTable:
            for columns in self.finalTable:
                for atom in columns:
                    if atom != None:
                        if symbol == atom.getsymbol():
                            return atom
    
    def __str__(self):
        """returns the string value of a Mendeleev object"""
        return "The Periodic Table of the Elements"
        
class Bond(Chemistry):
    
    def __init__(self,
                 start,
                 end,
                 order):
        """input the starting element and the ending element (bond from X to Y) and the order
        (single, double, triple) as an integer (1,2,3) of the bond."""
               
        #Declares the level of the bond and the elements bonded by it
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

    def __str__(self):
        if self.order == 1:
            return 'sb'
        elif self.order == 2:
            return 'db'
        elif self.order == 3:
            return 'tb'
        else:
            return 'None'

###Defines the locations of the tables
ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
elementsLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\elements.txt'        
theTable = Mendeleev(ptableLoc,elementsLoc)          
                                    
class Compound(Chemistry):
    
    def __init__(self,
                 formula):   
        """Input a formula (complete, don't reduce) of the molecule.  Should indicate connectivity
        by separating each molecular center. Ignore double/triple bonds and just show atoms.
        Formula should have form "CHxXxOx CHxXx" etc.  IE CHCl2 CH3
        Something like N-N (triple bond) would be represented as "N N". Bonds will be generated by 
        later functions"""

        #Initializes variables
        self.formula = formula
        self.centers = formula.split()
        size = (3*len(self.centers)+1)**2
        sidelen = int(np.sqrt(size))
        self.structure = np.empty((sidelen,sidelen), dtype = object)
        numList = ['1','2','3','4','5','6','7','8','9']
       
        #Separates the formula in order to create the bond
        inc = 0
        for part in self.centers:
            theCenter = [part[0]]
            theRest = re.split('(\d+)',part[1:])[:-1]
            trueRest = [theRest[i]+theRest[i+1] for i in range(0,len(theRest),2)]
            self.centers[inc] = theCenter+trueRest
            inc += 1
        
        #Splits up the substituents so as to indicate the number of them that are bonded to the center
        for part in self.centers:
            for substituent in range(1,len(part)):
                part[substituent] = re.split('(\d+)',part[substituent])[:-1]

        #Convert the symbols to element objects
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
                            
        #I need to associate the components with self.structure
        middle = int(len(self.structure)/2)
        i=0
        j=1
        while i < len(self.centers):
            x = str(self.centers[i][0])
            self.structure[middle][j] = x
            i+=1
            j+=2
        
        print self.centers
        print self.structure
            
        
        #Create bonds
        for i in range(len(self.centers)): pass
    
    def __str__(self):
        """the string value of a compound object"""
        return str(self.formula)  

def BeginProgram():
    """Function that initializes the program""" 
   
    ###Creates a (numpy) array version of the table then a visual (string) version of the table
    #periodicTable = theTable.getTable()
    #printTable = theTable.printableTable()
    
    ###sample compound    
    testCompound = Compound("CH1Cl2 CH3")  
    print testCompound #Testing

BeginProgram()