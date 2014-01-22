import numpy as np

aList = [['C', [['H'], '2']], '5', ['C', [['H'], '1', ['!'], '1']], '1']

def populate(anObject): 
    print anObject
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        try:
            locDict = {}
            for i in range(len(anObject)):
                try:locDict[i] = int(anObject[i])
                except (ValueError, AttributeError,TypeError):anObject[i] = populate(anObject[i])
                
            locKeys = locDict.keys()
            if len(locKeys) == 0:raise Exception
            locKeys.sort();locKeys.reverse()
            print locDict,locKeys
            
            for item in locKeys:
                amount = locDict[item]
                anObject.pop(item)
                for i in range(amount-1):
                    anObject.insert(item,anObject[item-1])
            print anObject
                
        except:
            return anObject
            
    if type(anObject) == type(''):
        return anObject
        
populate(aList)