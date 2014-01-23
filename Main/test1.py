import numpy as np

aList = [['C', [['H'], '2']], '5', ['C', [['H'], '1', ['!'], '1']], '1']
bList = [[['Carbon', [['Hydrogen'], '2']], '5', ['Carbon', [['Hydrogen'], '1', ['!'], '1']], '1']]


class Element:
    
    def __init__(self,aString):
        self.aString = aString
        
class Mendeleev:
    
    def __init__(self):
        self.aTable = ['C','H']
    
    def toElement(self,aString):
        aNum = self.aTable.index(aString)
        return aString
        
someTable = Mendeleev()

def populate(anObject): 
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        try:
            locDict = {}
            for i in range(len(anObject)):
                try:locDict[i] = int(anObject[i])
                except (ValueError, AttributeError,TypeError):anObject[i] = populate(anObject[i])
                    
            locKeys = locDict.keys()
            if len(locKeys) == 0:raise Exception
            locKeys.sort();locKeys.reverse()
            
            for item in locKeys:
                amount = locDict[item]
                anObject.pop(item)
                for i in range(amount-1):
                    anObject.insert(item,anObject[item-1])
            return anObject
                
        except:
            for i in range(len(anObject)):
                anObject[i] = populate(anObject[i])
            return anObject#populate(anObject)
            
    if type(anObject) == type(''):
        try:
            some = someTable.toElement(anObject)
            return some
        except:
            return anObject
        
print populate(aList)
print populate(bList)