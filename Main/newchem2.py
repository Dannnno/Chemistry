from errors import *
from elements import *
import numpy as np
import pyparsing as pyp

ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
etableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\main/te.txt'

def stringify(anObject):
    """converts every object within anObject to a string"""
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        newList = range(len(anObject))
        for i in range(len(anObject)):
            newList[i] = stringify(anObject[i])
        return newList
    if type(anObject) == type(''):return anObject
    if anObject == None:return anObject
    if type(anObject) == type({}):
        return stringify(anObject.keys())
    else:return str(anObject)  
    
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
            return 'error'#raise InvalidBondException(self)

def bondIt(aStruc,sLoc,eLoc,bLoc,order):
    """"""
    sLocx = sLoc[0];sLocy = sLoc[1]
    eLocx = eLoc[0];eLocy = eLoc[1]
    bLocx = bLoc[0];bLocy = bLoc[1]
    
    if len(eLoc) == 3:
        i = eLoc[2]
        bStruc = aStruc[eLocx][eLocy]
        if i == 1:
            aBond = Bond(aStruc[sLocx][sLocy],bStruc[2][2],order)
            bStruc[2][2].addBond(aBond)
        if i == 2:
            aBond = Bond(aStruc[sLocx][sLocy],bStruc[2][2],order)
            bStruc[2][2].addBond(aBond)
        if i == 3:
            aBond = Bond(aStruc[sLocx][sLocy],bStruc[0][2],order)
            bStruc[0][2].addBond(aBond)            
        if i == 4:
            aBond = Bond(aStruc[sLocx][sLocy],bStruc[2][0],order)
            bStruc[2][0].addBond(aBond)
        aStruc[sLocx][sLocy].addBond(aBond)
        aStruc[bLocx][bLocy] = aBond
        aStruc[eLocx][eLocy] = bStruc
        return aStruc
                    
    else:
        aBond = Bond(aStruc[sLocx][sLocy],aStruc[eLocx][eLocy],order)
        aStruc[sLocx][sLocy].addBond(aBond)
        aStruc[eLocx][eLocy].addBond(aBond)
        aStruc[bLocx][bLocy] = aBond
        return aStruc
    
class Mendeleev(Chemistry):
    
    def __init__(self,loc1,loc2):
        """Creates a periodic table of the elements. Only call this once"""
        
        ptable = np.genfromtxt(loc1,dtype='S',unpack=True)
        symb, ele = np.genfromtxt(loc2, dtype='S', unpack=True)
        tempTable = ptable.reshape((7,32))
        theTable = []
        
        #Populates the periodic table with element objects
        inc = 0
        for i in range(7):
            for j in range(32):
                if tempTable[i][j] == '0':
                    theTable.append(None)
                else:
                    theTable.append({symb[inc]:ele[inc]})
                    inc += 1
        
        #shapes the periodic table        
        self.finalTable = np.array(theTable).reshape((7,32))
    
    def getTable(self):
        """returns the numpy array that serves as the periodic table"""            
        return self.finalTable
        
    def getElement(self,part):
        """"""
        for rows in self.finalTable:
            for column in rows:
                if column != None:
                    if column.keys()[0] == part:
                        return eval(column[column.keys()[0]])
    
    def __str__(self):
        """String representation of the periodic table"""
        return repr(stringify(self.finalTable))

periodicTable = Mendeleev(ptableLoc,etableLoc)
theTable = periodicTable.getTable()
    
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
        return periodicTable.getElement(anObject)
    
    else:
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

def branching(anObject,structure,location):
    """recursive function that takes an array of element objects, a structure to place them in
    and the starting location and uses it to shape a compound"""
    #Creates the components
    primary = anObject[0]
    porder = 1
    if type(primary) == type(''):
        if primary[0] == '+':
            primary = toElement(primary[1:])
            porder = 2
        elif primary[0] == '*':
            primary = toElement(primary[1:])
            porder = 3
    tsubstituents = anObject[1:][0]
    substituents = []
    for part in tsubstituents:
        substituents.append(part)
    
    locX = location[0]
    locY = location[1]
    structure[locY][locX] = primary
    
    #Checks if the 4 cardinal points are occupied
    if (locY - 2) < 0: a1 = 1
    else:
        try: a1 = structure[locY-2][locX]
        except: a1 = 1
    if (locX - 2) < 0: a2 = 1
    else:
        try:a2 = structure[locY][locX-2]
        except: a2 = 1
    try: a3 = structure[locY+2][locX]
    except: a3 = 1
    try: a4 = structure[locY][locX+2]
    except: a4 = 1
    
    cardinals = [a1,a2,a3,a4]
    status = []
    i=1
    j=0

    for direction in cardinals:
        if direction == None: status.append(True)
        else: status.append(False)
    
    for point in status:
        if j <= len(substituents)-1:
            if point:
                theElement = substituents[j]
                if len(theElement) == 1:
                    theElement = theElement[0]
                aBool = False
                order = 1
                if type(theElement) == type([]) or type(theElement) == type(np.zeros(1)):
                    for part in theElement:
                        if type(part) == type([]) or type(part) == type(np.zeros(1)):
                            aBool = True
                if aBool:
                    if type(theElement[0]) == type(''):
                        if theElement[0][0] == '+':
                            theElement[0] = toElement(theElement[0][1:])
                            order = 2
                        elif theElement[0][0] == '*':
                            theElement[0] = toElement(theElement[0][1:])
                            order = 3
                    if i%2 != 0:subStruct = np.empty((3,5),dtype = object)
                    else:subStruct = np.empty((5,3),dtype = object)
                    if i == 1:
                        structure[locY-2][locX] = branching(theElement,subStruct,[2,2])
                        structure = bondIt(structure,[locY,locX],[locY-2,locX,i],[locY-1,locX],order)
                    if i == 2:
                        structure[locY][locX-2] = branching(theElement,subStruct,[2,2])
                        structure = bondIt(structure,[locY,locX],[locY,locX-2,i],[locY,locX-1],order)
                    if i == 3:
                        structure[locY+2][locX] = branching(theElement,subStruct,[2,0])
                        structure = bondIt(structure,[locY,locX],[locY+2,locX,i],[locY+1,locX],order)
                    if i == 4:
                        structure[locY][locX+2] = branching(theElement,subStruct,[0,2])
                        structure = bondIt(structure,[locY,locX],[locY,locX+2,i],[locY,locX+1],order)
                    j+=1
                else:
                    #theElement = theElement[0]
                    if type(theElement) == type(''):
                        if theElement[0] == '+':
                            tempElement = theElement[1:]
                            theElement = toElement(tempElement)
                            order = 2
                        elif theElement[0] == '*':
                            tempElement = theElement[1:]
                            theElement = toElement(tempElement)
                            order = 3
                    if i == 1:
                        structure[locY-2][locX] = theElement
                        structure = bondIt(structure,[locY,locX],[locY-2,locX],[locY-1,locX],order)
                    if i == 2:
                        structure[locY][locX-2] = theElement
                        structure = bondIt(structure,[locY,locX],[locY,locX-2],[locY,locX-1],order)
                    if i == 3:
                        structure[locY+2][locX] = theElement
                        structure = bondIt(structure,[locY,locX],[locY+2,locX],[locY+1,locX],order)
                    if i == 4:
                        structure[locY][locX+2] = theElement                        
                        structure = bondIt(structure,[locY,locX],[locY,locX+2],[locY,locX+1],order)
                    j += 1
            i+=1
    try:
        if structure[locY][locX+2] == None:
            structure[locY][locX+1] = porder
    except:pass
    return structure
        
class Compound(Chemistry):
    
    def __init__(self,formula):   
        """Input a formula for a chemical compound.  (currently) requires special
        syntax in order to be properly parsed."""

        #Initializes variables
        self.formula = formula
        self.centers = formula.split()
        self.structure = np.empty((5,int(np.sqrt(3*len(self.centers)+1)**2)), dtype = object)
        
        #Separates the compound
        for i in range(len(self.centers)):
            self.centers[i] = [self.centers[i][:self.centers[i].find('(')],
                               pyp.nestedExpr().parseString(self.centers[i][1:]).asList()[0]]
        
        #Associates symbols with their element objects
        self.centers = toElement(populate(self.centers))
        self.strcenters = stringify(self.centers)
                
        #Associates the compound with self.structure and creates bonds
        j = 2
        k = 0
        while k < len(self.centers):
            self.structure = branching(self.centers[k],self.structure,[j,2])
            j += 2 
            k += 1
       
        j=3
        for i in range(len(self.centers)-1):
            order = self.structure[2][j]
            self.structure = bondIt(self.structure,[2,j-1],[2,j+1],[2,j],order)
            j+=2
        
        self.strstructure = stringify(self.structure)
        print self.strstructure
        
    def __str__(self):
        """the string representation of a compound object"""
        return str(self.formula)          

a = Compound("C((C((H)3))3) C((+O)1(H)1)")
#b = Compound('C((!@((C((H)2))5(C((H)1(!)1))1))1(H)2) C((C((H)3))3)')
print a