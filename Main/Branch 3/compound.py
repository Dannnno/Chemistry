from func import *

class Compound(Chemistry):pass

class Alkane(Compound):

    def __init__(self,n):
        self.structure = np.empty((5,2*n+3),dtype=object)
        for i in range(2,2*n+1,2):
            self.structure[0][i] = Hydrogen()
            self.structure[4][i] = Hydrogen()
            self.structure[2][i] = Carbon()
            self.structure[1][i] = Bond(self.structure[2][i],self.structure[0][i],1)
            self.structure[3][i] = Bond(self.structure[2][i],self.structure[4][i],1)
        for i in range(3,2*n,2):
            self.structure[2][i] = Bond(self.structure[2][i-1],self.structure[2][i+1],1)
        self.structure[2][0] = Hydrogen()
        self.structure[2][-1] = Hydrogen()
        self.structure[2][1] = Bond(self.structure[2][2],self.structure[2][0],1)
        self.structure[2][-2] = Bond(self.structure[2][-3],self.structure[2][-1],1)
        print stringify(self.structure)
        
    def bondTo(self,loc1,loc2,newThing):
        locY1 = loc1[0]
        locX1 = loc1[1]
        
        locY2 = loc2[0]
        locX2 = loc2[1]
        
        if locX1 == 2 or locX1 == len(self.structure[0]) - 3:
            #Do stuff with terminal ones
            pass
        else:
            partA = []
            partB = []
            for i in range(len(self.structure)):
                for j in range(len(self.structure[i])):
                    if j < locX1:
                        partA.append(self.structure[i][j])
                        if j == locX1 - 1:
                            try:
                                partA[0][j].breakBond(partA[0][j+1])
                                partA.append(None)
                            except:
                                partA.append(None)
                    elif j > locX1:
                        partB.append(self.structure[i][j])
                        if j == locX1 + 1:
                            try:
                                partB[0][j-locX1-1].breakBond(partA[0][j-locX1-2])
                                partB.insert(j-locX1-2,None)
                            except:
                                partB.insert(j-locX1-2,None)
            
            strucA = np.array(partA).reshape(5,len(partA)/5)
            strucB = np.array(partB).reshape(5,len(partB)/5)
            
            
class Alkene(Compound):pass

class Alkyne(Compound):pass

class Alcohol(Compound):pass

class Carbonyl(Compound):pass

class Ketone(Carbonyl):pass

class Aldehyde(Carbonyl):pass

class Amine(Compound):pass

class Amide(Compound):pass

class Nitrile(Compound):pass

Alkane(6).bondTo([2,5],[4,5],'a')