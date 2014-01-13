import pyparsing as pyp
import numpy as np

numList = ['1','2','3','4','5','6','7','8','9']
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

class Reactions(Chemistry): pass

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
                
    def addBond(self,end,order=1):
        self.bondList.append(Bond(self,end,order))
        
    def getBonds(self):
        return self.bondList
        
    def getfam(self):
        """returns a string that represents the atomic family of the element"""
        return atomicFamilies[int(self.atomicFamily)]
        
def bothBonds(first,second,order):
    first.addBond(second,order)
    second.addBond(first,order)
                
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
        """Returns the appropriate element object given the element's symbol"""
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
    #Creates the components
    primary = anObject[0]
    substituents = anObject[1:]

    i = 1
    while i < len(substituents):
        aNum = substituents.pop(i)
        if aNum > 1:
            for j in range(aNum):
                substituents.insert(substituents[i-1],i+j)
        i+=(j+2)
        
    print substituents

    locX = location[0]
    locY = location[1]
    structure[locY][locX] = primary
    #Checks if the 4 cardinal points are occupied
    cardinals = [structure[locY-2][locX], #Checks the point above
                 structure[locY][locX-2], #Checks the point to the left
                 structure[locY+2][locX], #Checks the point below
                 structure[locY][locX+2]] #Checks the point to the right

    status = [] #reports on the four cardinal positions (True if empty, False if not)

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
                    #Put something north
                    structure[locY-2][locX] = secondaries[j]
                    structure[locY-1][locX] = Bond(primary,secondaries[j],1)
                    bothBonds(primary,secondaries[j],1)
                if i == 2:
                    #Put something west
                    structure[locY][locX-2] = secondaries[j]
                    structure[locY][locX-1] = Bond(primary,secondaries[j],1)
                    bothBonds(primary,secondaries[j],1)
                if i == 3:
                    #Put something south
                    structure[locY+2][locX] = secondaries[j]
                    structure[locY+1][locX] = Bond(primary,secondaries[j],1)
                    bothBonds(primary,secondaries[j],1)
                if i == 4:
                    #Put something east
                    structure[locY][locX+2] = secondaries[j]
                    structure[locY][locX+1] = Bond(primary,secondaries[j],1)
                    bothBonds(primary,secondaries[j],1)
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

###Defines the locations of the tables
ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
elementsLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\elements.txt'        
theTable = Mendeleev(ptableLoc,elementsLoc)          

def stringify(anArray):
    """takes an array and converts every object within to a string"""
    height = len(anArray)
    width = len(anArray[0])
    newArray = np.empty((width,height),dtype=object)
    for i in range(height):
        for j in range(width):
            newArray[i][j] = str(anArray[i][j])
                                    
    return newArray

def stoElement(anObject):
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        newList = range(len(anObject))#np.empty(len(anObject),dtype = object)
        for i in range(len(anObject)):
            newList[i] = stoElement(anObject[i])
        return newList
    
    if type(anObject) == type(''):
        if anObject[0] not in numList:
            anObject = str(theTable.getElement(anObject))
        return anObject          
        
def toElement(anObject):  
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        newList = range(len(anObject))#np.empty(len(anObject),dtype = object)
        for i in range(len(anObject)):
            newList[i] = toElement(anObject[i])
        return newList
    
    if type(anObject) == type(''):
        if anObject[0] not in numList:
            anObject = str(theTable.getElement(anObject))
        return anObject              
                                                                              
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
        
        #Separates the compound
        for i in range(len(self.centers)):
            self.centers[i] = [self.centers[i][:self.centers[i].find('(')],
                               pyp.nestedExpr().parseString(self.centers[i][1:]).asList()[0]]
        
        #Associates symbols with their element objects
        self.stringCenters = stoElement(self.centers)
        self.centers = toElement(self.centers)
        print self.stringCenters
        
        
        #Associates the compound with self.structure and creates bonds
        middle = int(len(self.structure)/2)
        i=middle
        j=2
        k=0
        
        while k < len(self.centers):
            self.structure = branching(self.centers[k],self.structure,[j,i])
            k+=1
            j+=2            
       
        j=3
        for i in range(len(self.centers)-1):
           self.structure[middle][j] = Bond(self.structure[middle][j-1],self.structure[middle][j+1],1)
           bothBonds(self.structure[middle][j-1],self.structure[middle][j+1],1)
           j+=2
        
        print stringify(self.structure)
        #print self.structure
        
    def __str__(self):
        """the string value of a compound object"""
        return str(self.formula)  

def BeginProgram():
    """Function that initializes the program""" 
   
    ###Creates a (numpy) array version of the table then a visual (string) version of the table
    #periodicTable = theTable.getTable()
    #printTable = theTable.printableTable()
    
    ###sample compound    
    testCompound = Compound("C((H)1(Cl)2)")  
    print testCompound #Testing
    
BeginProgram()