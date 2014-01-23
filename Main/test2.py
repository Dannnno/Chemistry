import numpy as np

class Bond:pass

class Ring:
    
    def __init__(self):
        self.aStruc = np.empty((7,7),dtype=object)
        self.aStruc[3][3] = '!'
    def getStruc(self):
        return self.aStruc
    def __str__(self):
        return 'aRing'

def findMark(aRing,mark):
    someStruc = aRing.getStruc()
    for i in range(len(someStruc)):
        for j in range(len(someStruc[i])):
            if someStruc[i][j] == mark:
                return [i,j]

def bondIt(aComp,aStruc,locS,locE,locB,order=1):
    
    if str(aComp) == 'aRing':pass
    
    else:
        start = aStruc[locS[0]][locS[1]]
        end = aStruc[locE[0]][locE[1]]
        bond = aStruc[locB[0]][locB[1]]
        
        aList = [start,end,bond]
        aList.append('')
        
        try:
            theBond = Bond(aStruc[locS[0]][locS[1]],aStruc[locE[0]][locE[1]],order)
            aStruc[locB[0]][locB[1]] = theBond
            aStruc[locS[0]][locS[1]].addBond(theBond)
            aStruc[locE[0]][locE[1]].addBond(theBond)
        except:
            if str(aStruc[locS[0]][locS[1]]) == 'aRing' and str(aStruc[locE[0]][locE[1]]) == 'aRing':
                pass
            if str(aStruc[locS[0]][locS[1]]) == 'aRing':
                pass
            elif str(aStruc[locE[0]][locE[1]]) == 'aRing':
                pass
