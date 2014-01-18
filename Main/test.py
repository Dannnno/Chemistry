# double bond, triple bond,ring support
# they need to be marked in some fashion in the string
##      + represents a double bond
##      * represents a triple bond
##      @ represents a ring

##      C((+O)2) represents O=C=O
##      N((*N)1) represents N=-N
##      @((C((H)2))6) represents C6H12 carbon ring:
##              H  H  H  H
##               \  \|  |
##            H--C--C--C--H
##               \     \
##            H--C--C--C--H
##              /  /\   \
##             H  H  H   H

# What needs to happen:
#   - parser should not delete these symbols - DONE
#   - branching() should recognize +/* and handle them appropriately - DONE
#   - branching() should recognize @ and pass the contents to the ring class
#       - parser will have to be able to separate this segment uniquely - DONE
#       - branching() will have to correctly identify where the rest of the structure is bonded to 
#         the ring

import pyparsing as pyp
import numpy as np

class Compound():pass

def populate(anObject):
    """"""
    if type(anObject) == type([]) or type(anObject) == type(np.zeros(1)):
        try:
            locDict = {}
            for i in range(len(anObject)):
                try:locDict[i] = int(anObject[i])
                except (ValueError,TypeError): pass
            
            locKeys = locDict.keys();locKeys.sort();locKeys.reverse()
            if len(locKeys) == 0:raise Exception
                
            for item in locKeys:
                anObject[item-1] = populate(anObject[item-1])
                insertObject = anObject[item-1]
                aNum = int(anObject.pop(item))
                if aNum > 1:
                    for i in range(aNum-1):anObject.insert(i+item,insertObject)
            return anObject
        except:
            for i in range(len(anObject)):anObject[i] = populate(anObject[i])
            return anObject
            
        for i in range(len(anObject)):anObject[i] = populate(anObject[i])
        return anObject
        
    if type(anObject) == type(''):return anObject 

def circulate(aRing,aStruc):
    """"""
    k = 0
    primarys = [part[0] for part in aRing]
    substituents = [part[1] for part in aRing]
    if len(aStruc[0])%2 == 0:
        for i in range(2,len(aStruc[0])-3,2):
            aStruc[2][i] = primarys[k]
            if i == 2:
                aStruc[0][i] = substituents[k][0][0]
                aStruc[1][i] = 'sb'
                aStruc[2][i-2] = substituents[k][1][0]
                aStruc[2][i-1] = 'sb'
            else:
                aStruc[0][i-1] = substituents[k][0][0]
                aStruc[1][i-1] = 'sb'
                aStruc[0][i] = substituents[k][1][0]
                aStruc[1][i] = 'sb'
            k += 1
        aStruc[3][-3] = primarys[k]
        aStruc[2][-1] = substituents[k][0][0]
        aStruc[2][-2] = 'sb'
        aStruc[3][-1] = substituents[k][1][0]
        aStruc[3][-2] = 'sb'
        k += 1
        for i in range(len(aStruc[2])-4,2,-2):
            aStruc[4][i] = primarys[k]
            aStruc[6][i+1] = substituents[k][0][0]
            aStruc[5][i+1] = 'sb'
            aStruc[6][i] = substituents[k][1][0]
            aStruc[5][i] = 'sb'
            k += 1
        aStruc[4][2] = primarys[k]
        aStruc[4][0] = substituents[k][0][0]
        aStruc[4][1] = 'sb'
        aStruc[6][2] = substituents[k][1][0]
        aStruc[5][2] = 'sb'
        for i in range(3,len(aStruc[0])-2,2):
            aStruc[2][i] = 'sb'
        for i in range(len(aStruc[2])-3,2,-2):
            aStruc[4][i] = 'sb'
        aStruc[3][2] = 'sb'
    else:
        for i in range(2,len(aStruc[0])-2,2):
            aStruc[2][i] = primarys[k]
            if i == 2:
                aStruc[0][i] = substituents[k][0][0]
                aStruc[1][i] = 'sb'
                aStruc[2][0] = substituents[k][1][0]
                aStruc[2][1] = 'sb'
            elif i == len(aStruc[0])-3:
                aStruc[0][i] = substituents[k][0][0]
                aStruc[1][i] = 'sb'
                aStruc[2][-1] = substituents[k][1][0]
                aStruc[2][-2] = 'sb'
            else:
                aStruc[0][i-1] = substituents[k][0][0]
                aStruc[1][i-1] = 'sb'
                aStruc[0][i] = substituents[k][1][0]
                aStruc[1][i] = 'sb'
            k += 1
        for i in range(len(aStruc[2])-3,0,-2):
            aStruc[4][i] = primarys[k]
            if i == 2:
                aStruc[-1][i] = substituents[k][0][0]
                aStruc[-2][i] = 'sb'
                aStruc[4][0] = substituents[k][1][0]
                aStruc[4][1] = 'sb'
            elif i == len(aStruc[2]) - 3:
                aStruc[4][-1] = substituents[k][0][0]
                aStruc[4][-2] = 'sb'
                aStruc[-1][i] = substituents[k][1][0]
                aStruc[-2][i] = 'sb'
            else:
                aStruc[-1][i+1] = substituents[k][0][0]
                aStruc[-2][i+1] = 'sb'
                aStruc[-1][i] = substituents[k][1][0]
                aStruc[-2][i] = 'sb'
            k+= 1
        for i in range(3,len(aStruc[0])-2,2):
            aStruc[2][i] = 'sb'
        aStruc[3][-3] = 'sb'
        for i in range(len(aStruc[2])-4,2,-2):
            aStruc[4][i] = 'sb'
        aStruc[3][2] = 'sb'
        
    return aStruc   
        
class Ring(Compound):
    def __init__(self,ringList):
        """"""
        self.ringList = populate(ringList)
        self.aLen = len(self.ringList)*2
        self.structure = np.empty((7,4+(self.aLen-2)/2),dtype=object)
        self.structure = circulate(self.ringList,self.structure)
        print self.structure
        
        
aString = "@((C((H)2))5(C((H)1(!)1))1) N((*N)1) C((+O)2)"
aList = aString.split()

for i in range(len(aList)):
    aList[i] = [aList[i][:aList[i].find('(')],
        pyp.nestedExpr().parseString(aList[i][1:]).asList()[0]]
        
for part in aList:
    if part[0] == '@':
        Ring(part[1:][0])