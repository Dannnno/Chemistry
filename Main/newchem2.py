from errors import *
from elements import *
import numpy as np

ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
etableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\main/te.txt'

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
        for rows in self.finalTable:
            for column in rows:
                if column != None:
                    if column.keys()[0] == part:
                        return eval(column[column.keys()[0]])
    
    def __str__(self):
        """String representation of the periodic table"""
        return repr(stringify(self.finalTable))#"The Periodic Table of the Elements"

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
        return anObject#eval(theDict[anObject])
        
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
        
periodicTable = Mendeleev(ptableLoc,etableLoc)
theTable = periodicTable.getTable()
print periodicTable.getElement('Sc')