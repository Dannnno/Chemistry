from elements import *
import numpy as np

class Bond(Chemistry):
    
    def __init__(self,start,end,order):
        
        self.start = start
        self.end = end
        self.order = order
        
    def __str__(self):
        if self.order == 1:
            return 'sb'
        elif self.order == 2:
            return 'db'
        elif self.order == 3:
            return 'tb'
        else:
            raise BondException
            
    def __repr__(self):
        return str(order) + " order bond between " + repr(self.start) + " and " + repr(self.end)
        
    def breakBond(self):
        self.start.removeBond(self)
        self.end.removeBond(self)

class Compound(Chemistry):pass

class fGroups(Chemistry):pass

class sp3Carbon(fGroups):
    
    def __init__(self):
        
        self.structure = np.empty((5,5), dtype=object)
        
        self.structure[0][2] = 'Available'
        self.structure[4][2] = 'Available'
        self.structure[2][0] = 'Available'
        self.structure[2][4] = 'Available'
        self.structure[2][2] = Carbon()
        
    def bondUp(self,new,order):
        
        self.structure[0][2] = new
        self.structure[1][2] = Bond(self.structure[2][2],self.structure[0][2],order)
   
    def bondLeft(self,new,order):
        
        self.structure[2][0] = new
        self.structure[2][1] = Bond(self.structure[2][2],self.structure[2][1],order)
    
    def bondDown(self,new,order):
        
        self.structure[4][2] = new
        self.structure[3][2] = Bond(self.structure[2][2],self.structure[4][2],order)
    
    def bondRight(self,new,order):
        
        self.structure[2][4] = new
        self.structure[2][3] = Bond(self.structure[2][2],self.structure[2][4],order)
        
    def bondTo(