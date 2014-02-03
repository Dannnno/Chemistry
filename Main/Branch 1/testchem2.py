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
                 family,
                 aNum):
        """Creates an element object using the atomic mass, number, symbol, name, electronegativity and atomic family"""
        #!!Needs octet rule support!!
        #!!Needs valence support!!
        
        self.atomicMass = mass
        self.atomicNumber = number
        self.atomicSymbol = symbol
        self.elementName = name
        self.electroneg = electronegativity
        self.atomicFamily = family
        self.bondList = []  
        self.n = aNum
        
    def __str__(self):
        """The string version of an element object -- its name"""
        return self.elementName
            
    def getmass(self):
        """returns the atomic mass as a float"""
        return self.atomicMass
        
    def getnumber(self):
        """returns the atomic number as an integer"""
        return self.atomicNumber
        
    def getname(self):
        """returns the element's name as a string"""
        return self.elementName
        
    def getsymbol(self):
        """returns the atomic symbol as a string"""
        return self.atomicSymbol
        
    def getneg(self):
        """"returns the electronegativity as a float"""
        return self.electroneg
                
    def addBond(self,aBond):
        """adds a Bond object to the element's list of Bonds.
        !!Needs more support for if number of bonds exceeds octet!!"""
        self.bondList.append(aBond)
        
    def getBonds(self):
        """returns the list of bonds the element is a part of"""
        return self.bondList
        
    def getfam(self):
        """returns the atomic family as a string"""
        return atomicFamilies[int(self.atomicFamily)]
        
def bothBonds(first,second,order=1):
    """adds the bond to both elements"""
    first.addBond(second,order)
    second.addBond(first,order)
                
class Mendeleev(Chemistry):  
          
    def __init__(self,
                 loc1,
                 loc2):
        """Creates a periodic table of the elements. Only call this once"""
        
        #generates an array of 1s and 0s to create the shape of the periodic table     
        self.inc = 0
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
                    theTable.append([massList[inc],
                                     nList[inc],
                                     symList[inc],
                                     nameList[inc],
                                     negList[inc],
                                     famList[inc]])
                    inc+=1  
        
        #shapes the periodic table        
        self.finalTable = np.array(theTable).reshape((7,32))
    
    def getTable(self):
        """returns the numpy array that serves as the periodic table"""            
        return self.finalTable

    def getElement(self,symbol):
        """Returns the appropriate element object given the element's symbol"""
        for rows in self.finalTable:
            for columns in self.finalTable:
                for atom in columns:
                    if atom != None:
                        if symbol == atom[2]:
                            self.inc+=1
                            return Element(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],self.inc)
    
    def __str__(self):
        """String representation of the periodic table"""
        return "The Periodic Table of the Elements"

###Defines the locations of the tables
ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
elementsLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\elements.txt'        
theTable = Mendeleev(ptableLoc,elementsLoc)         
                  
class Bond(Chemistry):
    
    def __init__(self,
                 start,
                 end,
                 order=1):
        """Creates a Bond object - input the two elements, and the order (default 1) of the bond"""
               
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
        """returns the element object at the 'front' of the bond"""
        return self.startElement
        
    def getEnd(self):
        """returns the element object at the 'back' of the bond"""
        return self.endElement
        
    def getOrder(self):
        """returns the order of the bond as an integer"""
        return self.order
        
    def getDescrip(self):
        """returns a string version of the bond's order"""
        return self.descriptor   

    def __str__(self):
        """returns a string depiction of a bond"""
        if self.order == 1:
            return 'sb'
        elif self.order == 2:
            return 'db'
        elif self.order == 3:
            return 'tb'
        else:
            return 'None'

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
        return theTable.getElement(anObject)
        
    if type(anObject) == type(Element(1,2,3,4,5,6,7)):
        return anObject
        
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
                                                                              
class Compound(Chemistry):
    
    def __init__(self,formula):   
        """Input a formula for a chemical compound.  (currently) requires special
        syntax in order to be properly parsed."""

        #Initializes variables
        self.formula = formula
        self.centers = formula.split()
        size = (6*len(self.centers)+1)**2
        sidelen = int(np.sqrt(size))
        self.structure = np.empty((sidelen,sidelen), dtype = object)
        self.strstructure = np.empty((sidelen,sidelen), dtype = object)
        
        #Separates the compound
        for i in range(len(self.centers)):
            self.centers[i] = [self.centers[i][:self.centers[i].find('(')],
                               pyp.nestedExpr().parseString(self.centers[i][1:]).asList()[0]]
        
        #Associates symbols with their element objects
        self.centers = populate(self.centers)
        self.centers = toElement(self.centers)
        
        #Associates the compound with self.structure and creates bonds
        middle = int(len(self.structure)/2)
        i=middle
        j=2
        k=0
        
        while k < len(self.centers):
            #self.structure = branching(self.centers[k],self.structure,[j,i])
            k+=1
            j+=2            
       
        j=3
        for i in range(len(self.centers)-1):
           #self.structure[middle][j] = Bond(self.structure[middle][j-1],self.structure[middle][j+1],1)
           #bothBonds(self.structure[middle][j-1],self.structure[middle][j+1],1)
           j+=2
        
        #self.strstructure = stringify(self.structure)
        #print self.strstructure
        
    def __str__(self):
        """the string representation of a compound object"""
        return str(self.formula)  

        
class Ring(Compound):
    def __init__(self,ringList,mark = ''):
        """"""
        self.mark = mark
        self.ringList = populate(ringList)[0]
        self.aLen = len(self.ringList)*2
        self.structure = np.empty((7,4+(self.aLen-2)/2),dtype=object)
        #self.someObject = circulate(self.ringList,self.structure,mark)
        self.theLoc = self.someObject[0]
        self.structure = self.someObject[1]
        
    def getMark(self):
        """"""
        return self.mark
    
    def getLoc(self):
        """"""
        return self.theLoc
        
    def getStruc(self):
        """"""
        return self.structure
        
    def setStruc(self,newStruc):
        """"""
        self.structure = newStruc
        
    def __str__(self):
        """"""
        return 'aRing'  

class BridgedStructure(Ring):
    
    def __init__(self,aRing):pass

def BeginProgram():
    """Function that initializes the program""" 
   
    ###sample compound    
    #testCompound = Compound("C((C((C((H)3))3))3) C((H)2(Cl)1)") #Compound C(C(CH3)3)3)C(H2Cl1)
    #print testCompound #Testing
    #testCompound = Compound("C((+O)2)")
    #print testCompound #Testing
    #testCompound = Compound("N((*N)1)")
    #print testCompound #Testing
    #testCompound = Compound('C((+O((C((H)3))1))1(H)2))')
    #print testCompound #Testing
    testCompound = Compound('C((!@((C((H)2))5(C((H)1(!)1))1))1(H)2) C((C((H)3))3)')
    print testCompound
    
BeginProgram()