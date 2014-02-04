from errors import *
from elements import *
import numpy as np
#import pyparsing as pyp

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
    
class Particle(Chemistry):pass

class Electron(Particle):
    def __init__(self):
        self.charge = -1
    def getCharge(self):
        return self.charge
    def __str__(self):
        return 'e-'
            
class Proton(Particle):
    def __init__(self):
        self.charge = 1    
    def getCharge(self):
        return self.charge
    def __str__(self):
        return 'p+'

class Neutron(Particle):
    def __init__(self):
        self.charge = 0    
    def getCharge(self):
        return self.charge
    def __str__(self):
        return 'n0'
        
class LPE(Electron):
    def __init__(self):
        self.electrons = [Electron(),Electron()]
        
class Bond(Electron):
    def __init__(self, start, end, order, direction='-'):
        self.start = start
        self.end = end
        self.order = order
        self.direction = direction
        if self.order not in range(1,4):
            raise BondOrderException(self.start, self.end, self.order)
        self.start.addBond(self)
        self.end.addBond(self)
        if order > 1:
            self.resonance = True
        else:
            self.resonance = False
        self.nPi = order-1
    
    def resonate(self):
        return self.resonance
        
    def makeSingle(self):
        self.order = 1
        self.nPi = 0
        self.resonance = False
        
    def makeDouble(self):
        self.order = 2
        self.nPi = 1
        self.resonance = True
    
    def makeTriple(self):
        self.order = 3
        self.nPi = 2
        self.resonance = True
    
    def __str__(self):
        if self.order == 1:
            return 'sb'
        elif self.order == 2:
            return 'db'
        elif self.order == 3:
            return 'tb'

class Radical(Electron):
    def __init__(self):
        self.electron = Electron()