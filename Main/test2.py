import numpy as np

def bondIt(aStruc,locS,locE,locB,order=1,rBool=False):
    """"""
    
    if rBool:
        substituents = locS
        if len(aStruc[0])%2 == 0:
            i = 
            pass
        else:
            pass
    
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
                strucA = aStruc[locS[0]][locS[1]].getStruc()
                strucB = aStruc[locE[0]][locE[1]].getStruc()
                
                aLoc = aStruc[locS[0]][locS[1]].getLoc()
                #bondLocA = aLoc[0]
                bondEndA = aLoc[1]
                
                bLoc = aStruc[locE[0]][locE[1]].getLoc()
                #bondLocB = bLoc[0]
                bondEndB = bLoc[1]
                
                theBond = Bond(strucA[bondEndA[0]][bondEndA[1]],strucB[bondEndB[0]][bondEndB[1]],order)
                strucA[bondEndA[0]][bondEndA[1]].addBond(theBond)
                strucB[bondEndB[0]][bondEndB[1]].addBond(theBond)
                #strucA[bondLocA[0]][bondLocA[1]] = theBond
                #strucB[bondLocB[0]][bondLocB[1]] = theBond
                aStruc[locB[0]][locB[1]] = theBond
                aStruc[locS[0]][locS[1]] = strucA
                aStruc[locE[0]][locE[1]] = strucB
                
                return aStruc
                
            if str(aStruc[locS[0]][locS[1]]) == 'aRing':
                strucA = aStruc[locS[0]][locS[1]].getStruc()
                aLoc = aStruc[locS[0]][locS[1]].getLoc()
                #bondLoc = aLoc[0]
                bondEnd = aLoc[1]
                theBond = Bond(aStruc[locE[0]][locE[1]],strucA[bondEnd[0]][bondEnd[1]],order)
                aStruc[locB[0]][locB[1]] = theBond
                aStruc[locE[0]][locE[1]].addBond(theBond)
                strucA[bondEnd[0]][bondEnd[1]].addBond(theBond)
                aStruc[locS[0]][locS[1]] = strucA
                
                return aStruc
                
            elif str(aStruc[locE[0]][locE[1]]) == 'aRing':
                strucA = aStruc[locE[0]][locE[1]].getStruc()
                aLoc = aStruc[locE[0]][locE[1]].getLoc()
                #bondLoc = aLoc[0]
                bondEnd = aLoc[1]
                theBond = Bond(aStruc[locS[0]][locS[1]],strucA[bondEnd[0]][bondEnd[1]],order)
                aStruc[locB[0]][locB[1]] = theBond
                aStruc[locS[0]][locS[1]].addBond(theBond)
                strucA[bondEnd[0]][bondEnd[1]].addBond(theBond)
                aStruc[locE[0]][locE[1]] = strucA
                
                return aStruc                