from func import *

def toAlkane(aCompound,secondary=None):
    """
    
    Takes some functional group `aCompound` and optional secondary arguments
    (used for specific functional groups) and returns either a tuple of the 
    returned types or a single new functional group object.
    
    EX: 
        >>> print(toAlkane(Alkyne()))
        Alkane
        >>> print(toAlkane(SomeDifferentFuncGroup()))
        (Some, Tuple, Of, Functional, Groups)
    
    """
    
    if aCompound.__class__.__name__ == 'Alkyne':
        return Alkane(2)
    
    elif aCompound.__class__.__name__ == 'Alkene':
        return Alkane(2)
    
def toAlkene(aCompound,secondary=None):
    """    
    
    Takes some functional group `aCompound` and optional secondary arguments
    (used for specific functional groups) and returns either a tuple of the 
    returned types or a single new functional group object.
    
    EX: 
        >>> print(toAlkene(Alkyne()))
        Alkane
        >>> print(toAlkene(Alkane(6)))
        (Alkane, Alkene, Alkane)
        
    """
    
    if aCompound.__class__.__name__ == 'Alkyne':
        return Alkene()
    
    elif aCompound.__class__.__name__ == 'Alkane':
        part1 = secondary[0]
        part2 = secondary[1]
        return Alkane(part1), Alkene(), Alkane(part2)
        
def toAlkyne(aCompound,secondary=None):
    """    
    
    Takes some functional group `aCompound` and optional secondary arguments
    (used for specific functional groups) and returns either a tuple of the 
    returned types or a single new functional group object.
    
    EX: 
        >>> print(toAlkyne(Alkene()))
        Alkyne
        >>> print(toAlkyne(Alkane(6)))
        (Alkane, Alkyne, Alkane)
        
    """
    
    if aCompound.__class__.__name__ == 'Alkene':
        return Alkyne()
    
    elif aCompound.__class__.__name__ == 'Alkane':
        part1 = secondary[0]
        part2 = secondary[1]
        return Alkane(part1), Alkyne(), Alkane(part2)
    
class Compound(Chemistry):pass

class Alkane(Compound):

    def __init__(self,n):
        """
        
        Creates a generic, linear Alkane of form C(n)H(n+2)
        
        """
        
        self.length = n
        
        self.structure = np.empty((5,2*n+3), dtype=object)
        
        ## Creates the backbone of the chain
        for i in range(2,2*n+1,2):
            self.structure[0][i] = Hydrogen()
            self.structure[4][i] = Hydrogen()
            self.structure[2][i] = Carbon()
            self.structure[1][i] = Bond(self.structure[2][i], self.structure[0][i], 1)
            self.structure[3][i] = Bond(self.structure[2][i], self.structure[4][i], 1)
        
        for i in range(3,2*n,2):
            self.structure[2][i] = Bond(self.structure[2][i-1], self.structure[2][i+1], 1)
        
        ## Sticks on the final two Hydrogens
        self.structure[2][0] = Hydrogen()
        self.structure[2][-1] = Hydrogen()
        self.structure[2][1] = Bond(self.structure[2][2], self.structure[2][0], 1)
        self.structure[2][-2] = Bond(self.structure[2][-3], self.structure[2][-1], 1)
    
    def __str__(self):
        return 'Alkane(' + str(self.length) + ')'
        
    def __repr__(self):
        return repr(stringify(self.structure))
        
            
class Alkene(Compound):

    def __init__(self):
        """
        
        Creates a generic Alkene H(2)C=CH(2)
        
        """
        
        ## Makes the Alkene
        self.structure = np.empty((5,6), dtype=object)
        self.structure[2][2] = Carbon()
        self.structure[2][4] = Carbon()
        self.structure[2][3] = Bond(self.structure[2][2], self.structure[2][4], 2)
        
        ## Adds Hydrogens
        self.structure[0][0] = Hydrogen()
        self.structure[1][1] = Bond(self.structure[2][2], self.structure[0][0], 1)
        self.structure[4][0] = Hydrogen()
        self.structure[3][1] = Bond(self.structure[2][2], self.structure[4][0], 1)
        
        self.structure[0][-1] = Hydrogen()
        self.structure[1][-2] = Bond(self.structure[2][4], self.structure[0][-1], 1)
        self.structure[4][-1] = Hydrogen()
        self.structure[3][-2] = Bond(self.structure[2][4], self.structure[4][-1], 1)
        
    def __str__(self):
        return 'Alkene()'
        
    def __repr__(self):
        return repr(stringify(self.structure))

class Alkyne(Compound):
   
    def __init__(self):
        """
        
        Creates a generic Alkyne H-C=-C-H
        
        """
        
        ## Make Alkyne
        self.structure = np.empty(7, dtype=object)
        self.structure[2] = Carbon()
        self.structure[4] = Carbon()
        self.structure[3] = Bond(self.structure[2], self.structure[4], 3)
        
        ## Add Hydrogens
        self.structure[0] = Hydrogen()
        self.structure[1] = Bond(self.structure[2], self.structure[0], 1)
        self.structure[-1] = Hydrogen()
        self.structure[-2] = Bond(self.structure[4], self.structure[-1], 1)
        
    def __str__(self):
        return 'Alkyne'
    
    def __repr__(self):
        return repr(stringify(self.structure))
                
class Alcohol(Compound):
   
    def __init__(self, alchLoc=1, stereoInfo='-'):
        """
        
        Creates a generic Alcohol CH(2)OH with 4 potential alcohol locations 
        North, West, South, East (NWSE) and with 3 potential stereo directions
        into page ('V'), out of page ('/'), in plane of page ('-').  Can bond 
        with other functional groups
        
        """
        
        self.stereo = stereoInfo
        self.Loc = alchLoc
        self.structure = np.empty((5,5), dtype=object)
        self.structure[2][2] = Carbon()
        
        if self.stereo not in ['-','/','V']: raise InvalidStereoException(['Alcohol', stereoInfo])
            
        ## Puts the Alcohol in the proper orientation
        if self.Loc not in range(1,5): raise InvalidLocationException(['Alcohol',self.Loc])
        
        self.structure[0][2] = Oxygen()
        self.structure[0][0] = Hydrogen()
        self.structure[0][1] = Bond(self.structure[0][2], self.structure[0][0], 1)            
        self.structure[1][2] = Bond(self.structure[2][2], self.structure[0][2], 1, self.stereo)
        
        self.structure[2][0] = Hydrogen()
        self.structure[2][1] = Bond(self.structure[2][2], self.structure[2][0], 1)       
        self.structure[4][2] = Hydrogen()
        self.structure[3][2] = Bond(self.structure[2][2], self.structure[4][2], 1)
        self.structure[2][4] = Hydrogen()
        self.structure[2][3] = Bond(self.structure[2][2], self.structure[2][4], 1)   
        self.orient()
        
    def orient(self,n=1):
        """"""
        if n == 1:
            if self.Loc == 2:
                self.structure = np.rot90(self.structure,1)
            elif self.Loc == 3:
                self.structure = np.rot90(self.structure,2)
            elif self.Loc == 4:
                self.structure = np.rot90(self.structure,3)
        elif n == 2:
            if self.Loc == 3:
                self.structure = np.rot90(self.structure,1)
            elif self.Loc == 4:
                self.structure = np.rot90(self.structure,2)
            elif self.Loc == 1:
                self.structure = np.rot90(self.structure,3)        
        elif n == 3:
            if self.Loc == 4:
                self.structure = np.rot90(self.structure,1)
            elif self.Loc == 1:
                self.structure = np.rot90(self.structure,2)
            elif self.Loc == 2:
                self.structure = np.rot90(self.structure,3)
        elif n == 4:
            if self.Loc == 1:
                self.structure = np.rot90(self.structure,1)
            elif self.Loc == 2:
                self.structure = np.rot90(self.structure,2)
            elif self.Loc == 3:
                self.structure = np.rot90(self.structure,3)   
                     
        else: raise InvalidLocationException(['Alcohol',n])
        
        print stringify(self.structure)
        
    def __str__(self):
        if self.stereo == None:
            t = '-'
        elif self.stereo:
            t = '/'
        else:
            t = 'V'
        return 'Alcohol(' + str(alchoLoc) + t + ')'
        
    def __repr__(self):
        return repr(stringify(self.structure))        
            
class Carbonyl(Compound):pass

class Ketone(Carbonyl):pass

class Aldehyde(Carbonyl):pass

class Amine(Compound):pass

class Amide(Compound):pass

class Nitrile(Compound):pass

#Alkane(6)
#Alkene()
#Alkyne()
#toAlkane(Alkyne())
Alcohol(1)
Alcohol(2)
Alcohol(3)
Alcohol(4)