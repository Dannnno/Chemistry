from func import *

class Reactions(Chemistry):pass
    
class AcidBase(Reactions):

    def FindProton(self):
        Acid = self.Acid
        Base = self.Base
        
    def pKa(self):pass

class Lewis(AcidBase):pass

class Bronsted(AcidBase):pass

class NucleophilicSub(Reactions):pass
    
class SN1(NucleophilicSub):pass

class SN2(NucleophilicSub):pass

class Elimination(Reactions):pass

class E1(Elimination):pass

class E2(Elimination):pass