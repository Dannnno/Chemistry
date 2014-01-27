from errors import *

class Chemistry():pass

class Element(Chemistry):

    def __init__(self):pass
    def getNum(self):
        return self.number
    def getMass(self):
        return self.mass
    def getName(self):
        return self.name
    def getSymbol(self):
        return self.symbol    
    def getRadius(self):
        return self.radius        
    def getEneg(self):
        return self.electronegativity        
    def getOx(self):
        return self.oxidation
    def getCharge(self):
        return self.charge
    def getBonds(self):
        return self.bondList
    def getInc(self):
        return self.inc
    def addBond(self,aBond):
        bondList.append(aBond)
    def breakBond(self,index):
        try:
            del bondList[index]
        except:
            print "No bond at this location"
    def changeBond(self,newBond,index):
        try:
            bondList[index] = newBond
        except:
            self.addBond(newBond)

class Hydrogen(Element):
    
    def __init__(self,aNum):
        self.number = 1
        self.mass = 1.00794
        self.name = 'Hydrogen'
        self.symbol = 'H'
        self.radius = 1
        self.electronegativity = 2.2
        self.oxidation = 1
        self.charge = 0
        self.bondList = []
        self.inc = aNum
            
class Helium(Element):
    
    def __init__(self,aNum):
        self.number = s
        self.mass = 4.002602
        self.name = 'Helium'
        self.symbol = 'He'
        self.radius = 1
        self.electronegativity = 0
        self.oxidation = 0
        self.charge = 0
        self.bondList = []
        self.inc = aNum
            
class Lithium(Element):
    
    def __init__(self,aNum):
        self.number = 3
        self.mass = 6.941
        self.name = 'Lithium'
        self.symbol = 'Li'
        self.radius = 1
        self.electronegativity = 0.98
        self.oxidation = 1
        self.charge = 0
        self.bondList = []
        self.inc = aNum
            
class Beryllium(Element):
    
    def __init__(self,aNum):
        self.number = 4
        self.mass = 9.012182
        self.name = 'Beryllium'
        self.symbol = 'Be'
        self.radius = 1
        self.electronegativity = 1.57
        self.oxidation = 2
        self.charge = 0
        self.bondList = []
        self.inc = aNum
        
class Boron(Element):
    
    def __init__(self,aNum):
        self.number = 5
        self.mass = 10.811
        self.name = 'Boron'
        self.symbol = 'B'
        self.radius = 1
        self.electronegativity = 2.04
        self.oxidation = 3
        self.charge = 0
        self.bondList = []
        self.inc = aNum
        
class Carbon(Element):
    
    def __init__(self,aNum):
        self.number = 6
        self.mass = 12.0107
        self.name = 'Carbon'
        self.symbol = 'C'
        self.radius = 1
        self.electronegativity = 2.55
        self.oxidation = 4
        self.charge = 0
        self.bondList = []
        self.inc = aNum            
              
class Nitrogen(Element):
    
    def __init__(self,aNum):
        self.number = 7
        self.mass = 14.0067
        self.name = 'Nitrogen'
        self.symbol = 'N'
        self.radius = 1
        self.electronegativity = 3.04
        self.oxidation = -3
        self.charge = 0
        self.bondList = []
        self.inc = aNum        
              
class Oxygen(Element):
    
    def __init__(self,aNum):
        self.number = 8
        self.mass = 15.9994
        self.name = 'Oxygen'
        self.symbol = 'O'
        self.radius = 1
        self.electronegativity = 3.44
        self.oxidation = -2
        self.charge = 0
        self.bondList = []
        self.inc = aNum              
                     
class Fluorine(Element):
    
    def __init__(self,aNum):
        self.number = 9
        self.mass = 18.9984032
        self.name = 'Fluorine'
        self.symbol = 'F'
        self.radius = 1
        self.electronegativity = 3.98
        self.oxidation = -1
        self.charge = 0
        self.bondList = []
        self.inc = aNum       
                     
class Neon(Element):
    
    def __init__(self,aNum):
        self.number = 10
        self.mass = 20.1797
        self.name = 'Neon'
        self.symbol = 'Ne'
        self.radius = 1
        self.electronegativity = 0
        self.oxidation = 0
        self.charge = 0
        self.bondList = []
        self.inc = aNum           
                                      
class Sodium(Element):
    
    def __init__(self,aNum):
        self.number = 11
        self.mass = 22.98976928
        self.name = 'Sodium'
        self.symbol = 'Na'
        self.radius = 1
        self.electronegativity = 0.93
        self.oxidation = 1
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Magnesium(Element):
    
    def __init__(self,aNum):
        self.number = 12
        self.mass = 24.305
        self.name = 'Magnesium'
        self.symbol = 'Mg'
        self.radius = 1
        self.electronegativity = 1.31
        self.oxidation = 2
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Aluminum(Element):
    
    def __init__(self,aNum):
        self.number = 13
        self.mass = 26.981536
        self.name = 'Aluminum'
        self.symbol = 'Al'
        self.radius = 1
        self.electronegativity = 1.61
        self.oxidation = 3
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Silicon(Element):
    
    def __init__(self,aNum):
        self.number = 14
        self.mass = 28.0855
        self.name = 'Silicon'
        self.symbol = 'Si'
        self.radius = 1
        self.electronegativity = 1.9
        self.oxidation = 4
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Phosphorus(Element):
    
    def __init__(self,aNum):
        self.number = 15
        self.mass = 30.973762
        self.name = 'Phosphorus'
        self.symbol = 'P'
        self.radius = 1
        self.electronegativity = 2.19
        self.oxidation = -3
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Sulfur(Element):
    
    def __init__(self,aNum):
        self.number = 16
        self.mass = 32.065
        self.name = 'Sulfur'
        self.symbol = 'S'
        self.radius = 1
        self.electronegativity = 2.58
        self.oxidation = -2
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Chlorine(Element):
    
    def __init__(self,aNum):
        self.number = 17
        self.mass = 35.453
        self.name = 'Chlorine'
        self.symbol = 'Cl'
        self.radius = 1
        self.electronegativity = 35.453
        self.oxidation = -1
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Argon(Element):
    
    def __init__(self,aNum):
        self.number = 18
        self.mass = 39.948
        self.name = 'Argon'
        self.symbol = 'Ar'
        self.radius = 1
        self.electronegativity = 0
        self.oxidation = 0
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Potassium(Element):
    
    def __init__(self,aNum):
        self.number = 19
        self.mass = 39.0983
        self.name = 'Potassium'
        self.symbol = 'K'
        self.radius = 1
        self.electronegativity = 0.82
        self.oxidation = 1
        self.charge = 0
        self.bondList = []
        self.inc = aNum
                                      
class Calcium(Element):
    
    def __init__(self,aNum):
        self.number = 20
        self.mass = 40.078
        self.name = 'Calcium'
        self.symbol = 'Ca'
        self.radius = 1
        self.electronegativity = 1
        self.oxidation = 2
        self.charge = 0
        self.bondList = []
        self.inc = aNum