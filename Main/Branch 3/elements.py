class Chemistry():
    pass

No_Data = 'No_Data'

class Element(Chemistry):
    def __init__(self):
        pass
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
    def addBond(self,aBond):
        self.bondList.append(aBond)
    def breakBond(self,index):
        try:del self.bondList[index]
        except:print 'No bond at this location'
    def changeBond(self,newBond,index):
        try:self.bondList[index] = newBond
        except:self.addBond(newBond)
    def getHeat(self):
        return self.heat
    def getBoil(self):
        return self.bp
    def getMelt(self):
        return self.mp
    def formalCharge(self):
        if self.group in [1,2,13,14,15,16,17]:
            if self.group > 10:
                valence = self.group - 10
            else:
                valence = self.group
            nBonds = len(self.bondList)
            nLPE = self.LPE
            FC = valence - nBonds - nLPE
            return FC
    def __str__(self):
        return self.name

class Hydrogen(Element):
    def __init__(self):
        self.number = 1
        self.symbol = 'H'
        self.name = 'Hydrogen'
        self.group = 1
        self.mass = 1.008
        self.density = 0.00008988
        self.melting = 14.01
        self.boiling = 20.28
        self.heat = 14.304
        self.electronegativity = 2.2
        self.radius = 53
        self.oxidation = [1,-1]
        self.charge = 0
        self.bondList = []

class Helium(Element):
    def __init__(self):
        self.number = 2
        self.symbol = 'He'
        self.name = 'Helium'
        self.group = 18
        self.mass = 4.002602
        self.density = 0.0001785
        self.melting = 0.956
        self.boiling = 4.22
        self.heat = 5.193
        self.electronegativity = No_Data
        self.radius = 31
        self.oxidation = [0]
        self.charge = 0
        self.bondList = []

class Lithium(Element):
    def __init__(self):
        self.number = 3
        self.symbol = 'Li'
        self.name = 'Lithium'
        self.group = 1
        self.mass = 6.94
        self.density = 0.534
        self.melting = 453.69
        self.boiling = 1560
        self.heat = 3.582
        self.electronegativity = 0.98
        self.radius = 167
        self.oxidation = [1]
        self.charge = 0
        self.bondList = []

class Beryllium(Element):
    def __init__(self):
        self.number = 4
        self.symbol = 'Be'
        self.name = 'Beryllium'
        self.group = 2
        self.mass = 9.012182
        self.density = 1.85
        self.melting = 1560
        self.boiling = 2742
        self.heat = 1.825
        self.electronegativity = 1.57
        self.radius = 112
        self.oxidation = [1,2]
        self.charge = 0
        self.bondList = []

class Boron(Element):
    def __init__(self):
        self.number = 5
        self.symbol = 'B'
        self.name = 'Boron'
        self.group = 13
        self.mass = 10.81
        self.density = 2.34
        self.melting = 2349
        self.boiling = 4200
        self.heat = 1.026
        self.electronegativity = 2.04
        self.radius = 87
        self.oxidation = [1,2,3]
        self.charge = 0
        self.bondList = []

class Carbon(Element):
    def __init__(self):
        self.number = 6
        self.symbol = 'C'
        self.name = 'Carbon'
        self.group = 14
        self.mass = 12.011
        self.density = 2.267
        self.melting = 3800
        self.boiling = 4300
        self.heat = 0.709
        self.electronegativity = 2.55
        self.radius = 67
        self.oxidation = [1,2,3,4,-4,-3,-2,-1]
        self.charge = 0
        self.bondList = []

class Nitrogen(Element):
    def __init__(self):
        self.number = 7
        self.symbol = 'N'
        self.name = 'Nitrogen'
        self.group = 15
        self.mass = 14.007
        self.density = 0.0012506
        self.melting = 63.15
        self.boiling = 77.36
        self.heat = 1.04
        self.electronegativity = 3.04
        self.radius = 56
        self.oxidation = [1,2,3,4,5,-3,-2,-1]
        self.charge = 0
        self.bondList = []

class Oxygen(Element):
    def __init__(self):
        self.number = 8
        self.symbol = 'O'
        self.name = 'Oxygen'
        self.group = 16
        self.mass = 15.999
        self.density = 0.001429
        self.melting = 54.36
        self.boiling = 90.2
        self.heat = 0.918
        self.electronegativity = 3.44
        self.radius = 48
        self.oxidation = [1,2,-2,-1]
        self.charge = 0
        self.bondList = []

class Fluorine(Element):
    def __init__(self):
        self.number = 9
        self.symbol = 'F'
        self.name = 'Fluorine'
        self.group = 17
        self.mass = 18.9984032
        self.density = 0.001696
        self.melting = 53.53
        self.boiling = 85.03
        self.heat = 0.824
        self.electronegativity = 3.98
        self.radius = 42
        self.oxidation = [-1]
        self.charge = 0
        self.bondList = []

class Neon(Element):
    def __init__(self):
        self.number = 10
        self.symbol = 'Ne'
        self.name = 'Neon'
        self.group = 18
        self.mass = 20.1797
        self.density = 0.0008999
        self.melting = 24.56
        self.boiling = 27.07
        self.heat = 1.03
        self.electronegativity = No_Data
        self.radius = 38
        self.oxidation = [0]
        self.charge = 0
        self.bondList = []

class Sodium(Element):
    def __init__(self):
        self.number = 11
        self.symbol = 'Na'
        self.name = 'Sodium'
        self.group = 1
        self.mass = 22.98976928
        self.density = 0.971
        self.melting = 370.87
        self.boiling = 1156
        self.heat = 1.228
        self.electronegativity = 0.93
        self.radius = 190
        self.oxidation = [1,-1]
        self.charge = 0
        self.bondList = []

class Magnesium(Element):
    def __init__(self):
        self.number = 12
        self.symbol = 'Mg'
        self.name = 'Magnesium'
        self.group = 2
        self.mass = 24.3059
        self.density = 1.738
        self.melting = 923
        self.boiling = 1363
        self.heat = 1.023
        self.electronegativity = 1.31
        self.radius = 145
        self.oxidation = [1,2]
        self.charge = 0
        self.bondList = []

class Aluminium(Element):
    def __init__(self):
        self.number = 13
        self.symbol = 'Al'
        self.name = 'Aluminium'
        self.group = 13
        self.mass = 26.9815386
        self.density = 2.698
        self.melting = 933.47
        self.boiling = 2792
        self.heat = 0.897
        self.electronegativity = 1.61
        self.radius = 118
        self.oxidation = [1,2,3]
        self.charge = 0
        self.bondList = []

class Silicon(Element):
    def __init__(self):
        self.number = 14
        self.symbol = 'Si'
        self.name = 'Silicon'
        self.group = 14
        self.mass = 28.085
        self.density = 2.3296
        self.melting = 1687
        self.boiling = 3538
        self.heat = 0.705
        self.electronegativity = 1.9
        self.radius = 111
        self.oxidation = [1,2,3,4,-4,-3,-2,-1]
        self.charge = 0
        self.bondList = []

class Phosphorus(Element):
    def __init__(self):
        self.number = 15
        self.symbol = 'P'
        self.name = 'Phosphorus'
        self.group = 15
        self.mass = 30.973762
        self.density = 1.82
        self.melting = 317.3
        self.boiling = 550
        self.heat = 0.769
        self.electronegativity = 2.19
        self.radius = 98
        self.oxidation = [1,2,3,4,5,-3,-2,-1]
        self.charge = 0
        self.bondList = []

class Sulfur(Element):
    def __init__(self):
        self.number = 16
        self.symbol = 'S'
        self.name = 'Sulfur'
        self.group = 16
        self.mass = 32.06
        self.density = 2.067
        self.melting = 388.36
        self.boiling = 717.87
        self.heat = 0.71
        self.electronegativity = 2.58
        self.radius = 88
        self.oxidation = [1,2,3,4,5,6,-1]
        self.charge = 0
        self.bondList = []

class Chlorine(Element):
    def __init__(self):
        self.number = 17
        self.symbol = 'Cl'
        self.name = 'Chlorine'
        self.group = 17
        self.mass = 35.45
        self.density = 0.003214
        self.melting = 171.6
        self.boiling = 239.11
        self.heat = 0.479
        self.electronegativity = 3.16
        self.radius = 79
        self.oxidation = [1,2,3,4,5,6,7,-1]
        self.charge = 0
        self.bondList = []

class Argon(Element):
    def __init__(self):
        self.number = 18
        self.symbol = 'Ar'
        self.name = 'Argon'
        self.group = 18
        self.mass = 39.948
        self.density = 0.0017837
        self.melting = 83.8
        self.boiling = 87.3
        self.heat = 0.52
        self.electronegativity = No_Data
        self.radius = 71
        self.oxidation = [0]
        self.charge = 0
        self.bondList = []

class Potassium(Element):
    def __init__(self):
        self.number = 19
        self.symbol = 'K'
        self.name = 'Potassium'
        self.group = 1
        self.mass = 39.0983
        self.density = 0.862
        self.melting = 336.53
        self.boiling = 1032
        self.heat = 0.757
        self.electronegativity = 0.82
        self.radius = 243
        self.oxidation = [1,-1]
        self.charge = 0
        self.bondList = []

class Calcium(Element):
    def __init__(self):
        self.number = 20
        self.symbol = 'Ca'
        self.name = 'Calcium'
        self.group = 2
        self.mass = 40.078
        self.density = 1.54
        self.melting = 1115
        self.boiling = 1757
        self.heat = 0.647
        self.electronegativity = 1
        self.radius = 194
        self.oxidation = [1,2]
        self.charge = 0
        self.bondList = []

class Scandium(Element):
    def __init__(self):
        self.number = 21
        self.symbol = 'Sc'
        self.name = 'Scandium'
        self.group = 3
        self.mass = 44.955912
        self.density = 2.989
        self.melting = 1814
        self.boiling = 3109
        self.heat = 0.568
        self.electronegativity = 1.36
        self.radius = 184
        self.oxidation = [1,2,3]
        self.charge = 0
        self.bondList = []

class Titanium(Element):
    def __init__(self):
        self.number = 22
        self.symbol = 'Ti'
        self.name = 'Titanium'
        self.group = 4
        self.mass = 47.867
        self.density = 4.54
        self.melting = 1941
        self.boiling = 3560
        self.heat = 0.523
        self.electronegativity = 1.54
        self.radius = 176
        self.oxidation = [1,2,3,4,-1]
        self.charge = 0
        self.bondList = []

class Vanadium(Element):
    def __init__(self):
        self.number = 23
        self.symbol = 'V'
        self.name = 'Vanadium'
        self.group = 5
        self.mass = 50.9415
        self.density = 6.11
        self.melting = 2183
        self.boiling = 3680
        self.heat = 0.489
        self.electronegativity = 1.63
        self.radius = 171
        self.oxidation = [1,2,3,4,5,-1]
        self.charge = 0
        self.bondList = []

class Chromium(Element):
    def __init__(self):
        self.number = 24
        self.symbol = 'Cr'
        self.name = 'Chromium'
        self.group = 6
        self.mass = 51.9961
        self.density = 7.15
        self.melting = 2180
        self.boiling = 2944
        self.heat = 0.449
        self.electronegativity = 1.66
        self.radius = 166
        self.oxidation = [1,2,3,4,5,6,-2,-1]
        self.charge = 0
        self.bondList = []

class Manganese(Element):
    def __init__(self):
        self.number = 25
        self.symbol = 'Mn'
        self.name = 'Manganese'
        self.group = 7
        self.mass = 54.938045
        self.density = 7.44
        self.melting = 1519
        self.boiling = 2334
        self.heat = 0.479
        self.electronegativity = 1.55
        self.radius = 161
        self.oxidation = [1,2,3,4,5,6,7,-3,-2,-1]
        self.charge = 0
        self.bondList = []

class Iron(Element):
    def __init__(self):
        self.number = 26
        self.symbol = 'Fe'
        self.name = 'Iron'
        self.group = 8
        self.mass = 55.845
        self.density = 7.874
        self.melting = 1811
        self.boiling = 3134
        self.heat = 0.449
        self.electronegativity = 1.83
        self.radius = 156
        self.oxidation = [1,2,3,4,5,6,-2,-1]
        self.charge = 0
        self.bondList = []

class Cobalt(Element):
    def __init__(self):
        self.number = 27
        self.symbol = 'Co'
        self.name = 'Cobalt'
        self.group = 9
        self.mass = 58.933195
        self.density = 8.86
        self.melting = 1768
        self.boiling = 3200
        self.heat = 0.421
        self.electronegativity = 1.88
        self.radius = 152
        self.oxidation = [1,2,3,4,5,-1]
        self.charge = 0
        self.bondList = []

class Nickel(Element):
    def __init__(self):
        self.number = 28
        self.symbol = 'Ni'
        self.name = 'Nickel'
        self.group = 10
        self.mass = 58.6934
        self.density = 8.912
        self.melting = 1728
        self.boiling = 3186
        self.heat = 0.444
        self.electronegativity = 1.91
        self.radius = 149
        self.oxidation = [1,2,3,4,-1]
        self.charge = 0
        self.bondList = []

class Copper(Element):
    def __init__(self):
        self.number = 29
        self.symbol = 'Cu'
        self.name = 'Copper'
        self.group = 11
        self.mass = 63.546
        self.density = 8.96
        self.melting = 1357.77
        self.boiling = 2835
        self.heat = 0.385
        self.electronegativity = 1.9
        self.radius = 145
        self.oxidation = [1,2,3,4]
        self.charge = 0
        self.bondList = []

class Zinc(Element):
    def __init__(self):
        self.number = 30
        self.symbol = 'Zn'
        self.name = 'Zinc'
        self.group = 12
        self.mass = 65.38
        self.density = 7.134
        self.melting = 692.88
        self.boiling = 1180
        self.heat = 0.388
        self.electronegativity = 1.65
        self.radius = 142
        self.oxidation = [1,2]
        self.charge = 0
        self.bondList = []

class Gallium(Element):
    def __init__(self):
        self.number = 31
        self.symbol = 'Ga'
        self.name = 'Gallium'
        self.group = 13
        self.mass = 69.723
        self.density = 5.907
        self.melting = 302.9146
        self.boiling = 2477
        self.heat = 0.371
        self.electronegativity = 1.81
        self.radius = 136
        self.oxidation = [1,2,3]
        self.charge = 0
        self.bondList = []

class Germanium(Element):
    def __init__(self):
        self.number = 32
        self.symbol = 'Ge'
        self.name = 'Germanium'
        self.group = 14
        self.mass = 72.630
        self.density = 5.323
        self.melting = 1211.4
        self.boiling = 3106
        self.heat = 0.32
        self.electronegativity = 2.01
        self.radius = 125
        self.oxidation = [1,2,3,4,-4,-3,-2,-1]
        self.charge = 0
        self.bondList = []

class Arsenic(Element):
    def __init__(self):
        self.number = 33
        self.symbol = 'As'
        self.name = 'Arsenic'
        self.group = 15
        self.mass = 74.92160
        self.density = 5.776
        self.melting = 1090
        self.boiling = 887
        self.heat = 0.329
        self.electronegativity = 2.18
        self.radius = 114
        self.oxidation = [1,2,3,5,-3]
        self.charge = 0
        self.bondList = []

class Selenium(Element):
    def __init__(self):
        self.number = 34
        self.symbol = 'Se'
        self.name = 'Selenium'
        self.group = 16
        self.mass = 78.96
        self.density = 4.809
        self.melting = 453
        self.boiling = 958
        self.heat = 0.321
        self.electronegativity = 2.55
        self.radius = 103
        self.oxidation = [1,2,4,6,-2]
        self.charge = 0
        self.bondList = []

class Bromine(Element):
    def __init__(self):
        self.number = 35
        self.symbol = 'Br'
        self.name = 'Bromine'
        self.group = 17
        self.mass = 79.9049
        self.density = 3.122
        self.melting = 265.8
        self.boiling = 332
        self.heat = 0.474
        self.electronegativity = 2.96
        self.radius = 94
        self.oxidation = [1,2,3,4,5,7,-1]
        self.charge = 0
        self.bondList = []

class Krypton(Element):
    def __init__(self):
        self.number = 36
        self.symbol = 'Kr'
        self.name = 'Krypton'
        self.group = 18
        self.mass = 83.798
        self.density = 0.003733
        self.melting = 115.79
        self.boiling = 119.93
        self.heat = 0.248
        self.electronegativity = 3
        self.radius = 88
        self.oxidation = [2]
        self.charge = 0
        self.bondList = []

class Rubidium(Element):
    def __init__(self):
        self.number = 37
        self.symbol = 'Rb'
        self.name = 'Rubidium'
        self.group = 1
        self.mass = 85.4678
        self.density = 1.532
        self.melting = 312.46
        self.boiling = 961
        self.heat = 0.363
        self.electronegativity = 0.82
        self.radius = 265
        self.oxidation = [1,-1]
        self.charge = 0
        self.bondList = []

class Strontium(Element):
    def __init__(self):
        self.number = 38
        self.symbol = 'Sr'
        self.name = 'Strontium'
        self.group = 2
        self.mass = 87.62
        self.density = 2.64
        self.melting = 1050
        self.boiling = 1655
        self.heat = 0.301
        self.electronegativity = 0.95
        self.radius = 219
        self.oxidation = [1,2]
        self.charge = 0
        self.bondList = []

class Yttrium(Element):
    def __init__(self):
        self.number = 39
        self.symbol = 'Y'
        self.name = 'Yttrium'
        self.group = 3
        self.mass = 88.90585
        self.density = 4.469
        self.melting = 1799
        self.boiling = 3609
        self.heat = 0.298
        self.electronegativity = 1.22
        self.radius = 212
        self.oxidation = [1,2,3]
        self.charge = 0
        self.bondList = []

class Zirconium(Element):
    def __init__(self):
        self.number = 40
        self.symbol = 'Zr'
        self.name = 'Zirconium'
        self.group = 4
        self.mass = 91.224
        self.density = 6.506
        self.melting = 2128
        self.boiling = 4682
        self.heat = 0.278
        self.electronegativity = 1.33
        self.radius = 206
        self.oxidation = [1,2,3,4]
        self.charge = 0
        self.bondList = []

class Niobium(Element):
    def __init__(self):
        self.number = 41
        self.symbol = 'Nb'
        self.name = 'Niobium'
        self.group = 5
        self.mass = 92.90638
        self.density = 8.57
        self.melting = 2750
        self.boiling = 5017
        self.heat = 0.265
        self.electronegativity = 1.6
        self.radius = 198
        self.oxidation = [1,2,3,4,5,-1]
        self.charge = 0
        self.bondList = []

class Molybdenum(Element):
    def __init__(self):
        self.number = 42
        self.symbol = 'Mo'
        self.name = 'Molybdenum'
        self.group = 6
        self.mass = 95.96
        self.density = 10.22
        self.melting = 2896
        self.boiling = 4912
        self.heat = 0.251
        self.electronegativity = 2.16
        self.radius = 190
        self.oxidation = [1,2,3,4,5,6,-2,-1]
        self.charge = 0
        self.bondList = []

class Technetium(Element):
    def __init__(self):
        self.number = 43
        self.symbol = 'Tc'
        self.name = 'Technetium'
        self.group = 7
        self.mass = 98
        self.density = 11.5
        self.melting = 2430
        self.boiling = 4538
        self.heat = No_Data
        self.electronegativity = 1.9
        self.radius = 183
        self.oxidation = [1,2,3,4,5,6,7,-3,-1]
        self.charge = 0
        self.bondList = []

class Ruthenium(Element):
    def __init__(self):
        self.number = 44
        self.symbol = 'Ru'
        self.name = 'Ruthenium'
        self.group = 8
        self.mass = 101.07
        self.density = 12.37
        self.melting = 2607
        self.boiling = 4423
        self.heat = 0.238
        self.electronegativity = 2.2
        self.radius = 178
        self.oxidation = [1,2,3,4,5,6,7,8,-2]
        self.charge = 0
        self.bondList = []

class Rhodium(Element):
    def __init__(self):
        self.number = 45
        self.symbol = 'Rh'
        self.name = 'Rhodium'
        self.group = 9
        self.mass = 102.90550
        self.density = 12.41
        self.melting = 2237
        self.boiling = 3968
        self.heat = 0.243
        self.electronegativity = 2.28
        self.radius = 173
        self.oxidation = [1,2,3,4,5,6,-1]
        self.charge = 0
        self.bondList = []

class Palladium(Element):
    def __init__(self):
        self.number = 46
        self.symbol = 'Pd'
        self.name = 'Palladium'
        self.group = 10
        self.mass = 106.42
        self.density = 12.02
        self.melting = 1828.05
        self.boiling = 3236
        self.heat = 0.244
        self.electronegativity = 2.2
        self.radius = 169
        self.oxidation = [1,2,4,6]
        self.charge = 0
        self.bondList = []

class Silver(Element):
    def __init__(self):
        self.number = 47
        self.symbol = 'Ag'
        self.name = 'Silver'
        self.group = 11
        self.mass = 107.8682
        self.density = 10.501
        self.melting = 1234.93
        self.boiling = 2435
        self.heat = 0.235
        self.electronegativity = 1.93
        self.radius = 165
        self.oxidation = [1,2,3,4]
        self.charge = 0
        self.bondList = []

class Cadmium(Element):
    def __init__(self):
        self.number = 48
        self.symbol = 'Cd'
        self.name = 'Cadmium'
        self.group = 12
        self.mass = 112.411
        self.density = 8.69
        self.melting = 594.22
        self.boiling = 1040
        self.heat = 0.232
        self.electronegativity = 1.69
        self.radius = 161
        self.oxidation = [1,2]
        self.charge = 0
        self.bondList = []

class Indium(Element):
    def __init__(self):
        self.number = 49
        self.symbol = 'In'
        self.name = 'Indium'
        self.group = 13
        self.mass = 114.818
        self.density = 7.31
        self.melting = 429.75
        self.boiling = 2345
        self.heat = 0.233
        self.electronegativity = 1.78
        self.radius = 156
        self.oxidation = [1,2,3]
        self.charge = 0
        self.bondList = []

class Tin(Element):
    def __init__(self):
        self.number = 50
        self.symbol = 'Sn'
        self.name = 'Tin'
        self.group = 14
        self.mass = 118.710
        self.density = 7.287
        self.melting = 505.08
        self.boiling = 2875
        self.heat = 0.228
        self.electronegativity = 1.96
        self.radius = 145
        self.oxidation = [2,4,-4]
        self.charge = 0
        self.bondList = []

class Antimony(Element):
    def __init__(self):
        self.number = 51
        self.symbol = 'Sb'
        self.name = 'Antimony'
        self.group = 15
        self.mass = 121.760
        self.density = 6.685
        self.melting = 903.78
        self.boiling = 1860
        self.heat = 0.207
        self.electronegativity = 2.05
        self.radius = 133
        self.oxidation = [3,5,-3]
        self.charge = 0
        self.bondList = []

class Tellurium(Element):
    def __init__(self):
        self.number = 52
        self.symbol = 'Te'
        self.name = 'Tellurium'
        self.group = 16
        self.mass = 127.60
        self.density = 6.232
        self.melting = 722.66
        self.boiling = 1261
        self.heat = 0.202
        self.electronegativity = 2.1
        self.radius = 123
        self.oxidation = [2,4,5,6,-2]
        self.charge = 0
        self.bondList = []

class Iodine(Element):
    def __init__(self):
        self.number = 53
        self.symbol = 'I'
        self.name = 'Iodine'
        self.group = 17
        self.mass = 126.90447
        self.density = 4.93
        self.melting = 386.85
        self.boiling = 457.4
        self.heat = 0.214
        self.electronegativity = 2.66
        self.radius = 115
        self.oxidation = [1,3,4,5,7,-1]
        self.charge = 0
        self.bondList = []

class Xenon(Element):
    def __init__(self):
        self.number = 54
        self.symbol = 'Xe'
        self.name = 'Xenon'
        self.group = 18
        self.mass = 131.293
        self.density = 0.005887
        self.melting = 161.4
        self.boiling = 165.03
        self.heat = 0.158
        self.electronegativity = 2.6
        self.radius = 108
        self.oxidation = [1,2,4,6,8]
        self.charge = 0
        self.bondList = []

class Caesium(Element):
    def __init__(self):
        self.number = 55
        self.symbol = 'Cs'
        self.name = 'Caesium'
        self.group = 1
        self.mass = 132.9054519
        self.density = 1.873
        self.melting = 301.59
        self.boiling = 944
        self.heat = 0.242
        self.electronegativity = 0.79
        self.radius = 298
        self.oxidation = [1,-1]
        self.charge = 0
        self.bondList = []

class Barium(Element):
    def __init__(self):
        self.number = 56
        self.symbol = 'Ba'
        self.name = 'Barium'
        self.group = 2
        self.mass = 137.327
        self.density = 3.594
        self.melting = 1000
        self.boiling = 2170
        self.heat = 0.204
        self.electronegativity = 0.89
        self.radius = 253
        self.oxidation = [2]
        self.charge = 0
        self.bondList = []

class Lanthanum(Element):
    def __init__(self):
        self.number = 57
        self.symbol = 'La'
        self.name = 'Lanthanum'
        self.group = 0
        self.mass = 138.90547
        self.density = 6.145
        self.melting = 1193
        self.boiling = 3737
        self.heat = 0.195
        self.electronegativity = 1.1
        self.radius = No_Data
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Cerium(Element):
    def __init__(self):
        self.number = 58
        self.symbol = 'Ce'
        self.name = 'Cerium'
        self.group = 0
        self.mass = 140.116
        self.density = 6.77
        self.melting = 1068
        self.boiling = 3716
        self.heat = 0.192
        self.electronegativity = 1.12
        self.radius = No_Data
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Praseodymium(Element):
    def __init__(self):
        self.number = 59
        self.symbol = 'Pr'
        self.name = 'Praseodymium'
        self.group = 0
        self.mass = 140.90765
        self.density = 6.773
        self.melting = 1208
        self.boiling = 3793
        self.heat = 0.193
        self.electronegativity = 1.13
        self.radius = 247
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Neodymium(Element):
    def __init__(self):
        self.number = 60
        self.symbol = 'Nd'
        self.name = 'Neodymium'
        self.group = 0
        self.mass = 144.242
        self.density = 7.007
        self.melting = 1297
        self.boiling = 3347
        self.heat = 0.19
        self.electronegativity = 1.14
        self.radius = 206
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Promethium(Element):
    def __init__(self):
        self.number = 61
        self.symbol = 'Pm'
        self.name = 'Promethium'
        self.group = 0
        self.mass = 145
        self.density = 7.26
        self.melting = 1315
        self.boiling = 3273
        self.heat = No_Data
        self.electronegativity = 1.13
        self.radius = 205
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Samarium(Element):
    def __init__(self):
        self.number = 62
        self.symbol = 'Sm'
        self.name = 'Samarium'
        self.group = 0
        self.mass = 150.36
        self.density = 7.52
        self.melting = 1345
        self.boiling = 2067
        self.heat = 0.197
        self.electronegativity = 1.17
        self.radius = 238
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Europium(Element):
    def __init__(self):
        self.number = 63
        self.symbol = 'Eu'
        self.name = 'Europium'
        self.group = 0
        self.mass = 151.964
        self.density = 5.243
        self.melting = 1099
        self.boiling = 1802
        self.heat = 0.182
        self.electronegativity = 1.2
        self.radius = 231
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Gadolinium(Element):
    def __init__(self):
        self.number = 64
        self.symbol = 'Gd'
        self.name = 'Gadolinium'
        self.group = 0
        self.mass = 157.25
        self.density = 7.895
        self.melting = 1585
        self.boiling = 3546
        self.heat = 0.236
        self.electronegativity = 1.2
        self.radius = 233
        self.oxidation = [1,2,3]
        self.charge = 0
        self.bondList = []

class Terbium(Element):
    def __init__(self):
        self.number = 65
        self.symbol = 'Tb'
        self.name = 'Terbium'
        self.group = 0
        self.mass = 158.92535
        self.density = 8.229
        self.melting = 1629
        self.boiling = 3503
        self.heat = 0.182
        self.electronegativity = 1.2
        self.radius = 225
        self.oxidation = [1,2,3,4]
        self.charge = 0
        self.bondList = []

class Dysprosium(Element):
    def __init__(self):
        self.number = 66
        self.symbol = 'Dy'
        self.name = 'Dysprosium'
        self.group = 0
        self.mass = 162.500
        self.density = 8.55
        self.melting = 1680
        self.boiling = 2840
        self.heat = 0.17
        self.electronegativity = 1.22
        self.radius = 228
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Holmium(Element):
    def __init__(self):
        self.number = 67
        self.symbol = 'Ho'
        self.name = 'Holmium'
        self.group = 0
        self.mass = 164.93032
        self.density = 8.795
        self.melting = 1734
        self.boiling = 2993
        self.heat = 0.165
        self.electronegativity = 1.23
        self.radius = No_Data
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Erbium(Element):
    def __init__(self):
        self.number = 68
        self.symbol = 'Er'
        self.name = 'Erbium'
        self.group = 0
        self.mass = 167.259
        self.density = 9.066
        self.melting = 1802
        self.boiling = 3141
        self.heat = 0.168
        self.electronegativity = 1.24
        self.radius = 226
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Thulium(Element):
    def __init__(self):
        self.number = 69
        self.symbol = 'Tm'
        self.name = 'Thulium'
        self.group = 0
        self.mass = 168.93421
        self.density = 9.321
        self.melting = 1818
        self.boiling = 2223
        self.heat = 0.16
        self.electronegativity = 1.25
        self.radius = 222
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Ytterbium(Element):
    def __init__(self):
        self.number = 70
        self.symbol = 'Yb'
        self.name = 'Ytterbium'
        self.group = 0
        self.mass = 173.054
        self.density = 6.965
        self.melting = 1097
        self.boiling = 1469
        self.heat = 0.155
        self.electronegativity = 1.1
        self.radius = 222
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Lutetium(Element):
    def __init__(self):
        self.number = 71
        self.symbol = 'Lu'
        self.name = 'Lutetium'
        self.group = 3
        self.mass = 174.9668
        self.density = 9.84
        self.melting = 1925
        self.boiling = 3675
        self.heat = 0.154
        self.electronegativity = 1.27
        self.radius = 217
        self.oxidation = [3]
        self.charge = 0
        self.bondList = []

class Hafnium(Element):
    def __init__(self):
        self.number = 72
        self.symbol = 'Hf'
        self.name = 'Hafnium'
        self.group = 4
        self.mass = 178.49
        self.density = 13.31
        self.melting = 2506
        self.boiling = 4876
        self.heat = 0.144
        self.electronegativity = 1.3
        self.radius = 208
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Tantalum(Element):
    def __init__(self):
        self.number = 73
        self.symbol = 'Ta'
        self.name = 'Tantalum'
        self.group = 5
        self.mass = 180.94788
        self.density = 16.654
        self.melting = 3290
        self.boiling = 5731
        self.heat = 0.14
        self.electronegativity = 1.5
        self.radius = 200
        self.oxidation = [2,3,4,5,-1]
        self.charge = 0
        self.bondList = []

class Tungsten(Element):
    def __init__(self):
        self.number = 74
        self.symbol = 'W'
        self.name = 'Tungsten'
        self.group = 6
        self.mass = 183.84
        self.density = 19.25
        self.melting = 3695
        self.boiling = 5828
        self.heat = 0.132
        self.electronegativity = 2.36
        self.radius = 193
        self.oxidation = [1,2,3,4,5,6,-2,-1]
        self.charge = 0
        self.bondList = []

class Rhenium(Element):
    def __init__(self):
        self.number = 75
        self.symbol = 'Re'
        self.name = 'Rhenium'
        self.group = 7
        self.mass = 186.207
        self.density = 21.02
        self.melting = 3459
        self.boiling = 5869
        self.heat = 0.137
        self.electronegativity = 1.9
        self.radius = 188
        self.oxidation = [1,2,3,4,5,6,7,-3,-1]
        self.charge = 0
        self.bondList = []

class Osmium(Element):
    def __init__(self):
        self.number = 76
        self.symbol = 'Os'
        self.name = 'Osmium'
        self.group = 8
        self.mass = 190.23
        self.density = 22.61
        self.melting = 3306
        self.boiling = 5285
        self.heat = 0.13
        self.electronegativity = 2.2
        self.radius = 185
        self.oxidation = [1,2,3,4,5,6,7,8,-2,-1]
        self.charge = 0
        self.bondList = []

class Iridium(Element):
    def __init__(self):
        self.number = 77
        self.symbol = 'Ir'
        self.name = 'Iridium'
        self.group = 9
        self.mass = 192.217
        self.density = 22.56
        self.melting = 2719
        self.boiling = 4701
        self.heat = 0.131
        self.electronegativity = 2.2
        self.radius = 180
        self.oxidation = [1,2,3,4,5,6,7,8,-3,-1]
        self.charge = 0
        self.bondList = []

class Platinum(Element):
    def __init__(self):
        self.number = 78
        self.symbol = 'Pt'
        self.name = 'Platinum'
        self.group = 10
        self.mass = 195.084
        self.density = 21.46
        self.melting = 2041.4
        self.boiling = 4098
        self.heat = 0.133
        self.electronegativity = 2.28
        self.radius = 177
        self.oxidation = [1,2,3,4,5,6,-2,-1]
        self.charge = 0
        self.bondList = []

class Gold(Element):
    def __init__(self):
        self.number = 79
        self.symbol = 'Au'
        self.name = 'Gold'
        self.group = 11
        self.mass = 196.966569
        self.density = 19.282
        self.melting = 1337.33
        self.boiling = 3129
        self.heat = 0.129
        self.electronegativity = 2.54
        self.radius = 174
        self.oxidation = [1,2,3,5,-1]
        self.charge = 0
        self.bondList = []

class Mercury(Element):
    def __init__(self):
        self.number = 80
        self.symbol = 'Hg'
        self.name = 'Mercury'
        self.group = 12
        self.mass = 200.592
        self.density = 13.5336
        self.melting = 234.43
        self.boiling = 629.88
        self.heat = 0.14
        self.electronegativity = 2
        self.radius = 171
        self.oxidation = [1,2,4]
        self.charge = 0
        self.bondList = []

class Thallium(Element):
    def __init__(self):
        self.number = 81
        self.symbol = 'Tl'
        self.name = 'Thallium'
        self.group = 13
        self.mass = 204.389
        self.density = 11.85
        self.melting = 577
        self.boiling = 1746
        self.heat = 0.129
        self.electronegativity = 1.62
        self.radius = 156
        self.oxidation = [1,3,-1]
        self.charge = 0
        self.bondList = []

class Lead(Element):
    def __init__(self):
        self.number = 82
        self.symbol = 'Pb'
        self.name = 'Lead'
        self.group = 14
        self.mass = 207.2
        self.density = 11.342
        self.melting = 600.61
        self.boiling = 2022
        self.heat = 0.129
        self.electronegativity = 1.87
        self.radius = 154
        self.oxidation = [2,4,-4]
        self.charge = 0
        self.bondList = []

class Bismuth(Element):
    def __init__(self):
        self.number = 83
        self.symbol = 'Bi'
        self.name = 'Bismuth'
        self.group = 15
        self.mass = 208.98040
        self.density = 9.807
        self.melting = 544.7
        self.boiling = 1837
        self.heat = 0.122
        self.electronegativity = 2.02
        self.radius = 143
        self.oxidation = [1,3,5,-3]
        self.charge = 0
        self.bondList = []

class Polonium(Element):
    def __init__(self):
        self.number = 84
        self.symbol = 'Po'
        self.name = 'Polonium'
        self.group = 16
        self.mass = 209
        self.density = 9.32
        self.melting = 527
        self.boiling = 1235
        self.heat = No_Data
        self.electronegativity = 2
        self.radius = 135
        self.oxidation = [2,4,5,6,-2]
        self.charge = 0
        self.bondList = []

class Astatine(Element):
    def __init__(self):
        self.number = 85
        self.symbol = 'At'
        self.name = 'Astatine'
        self.group = 17
        self.mass = 210
        self.density = 7
        self.melting = 575
        self.boiling = 610
        self.heat = No_Data
        self.electronegativity = 2.2
        self.radius = No_Data
        self.oxidation = [1,3,5,7,-1]
        self.charge = 0
        self.bondList = []

class Radon(Element):
    def __init__(self):
        self.number = 86
        self.symbol = 'Rn'
        self.name = 'Radon'
        self.group = 18
        self.mass = 222
        self.density = 0.00973
        self.melting = 202
        self.boiling = 211.3
        self.heat = 0.094
        self.electronegativity = 2.2
        self.radius = 120
        self.oxidation = [2,6]
        self.charge = 0
        self.bondList = []

class Francium(Element):
    def __init__(self):
        self.number = 87
        self.symbol = 'Fr'
        self.name = 'Francium'
        self.group = 1
        self.mass = 223
        self.density = 1.87
        self.melting = 300
        self.boiling = 950
        self.heat = No_Data
        self.electronegativity = 0.7
        self.radius = No_Data
        self.oxidation = [1]
        self.charge = 0
        self.bondList = []

class Radium(Element):
    def __init__(self):
        self.number = 88
        self.symbol = 'Ra'
        self.name = 'Radium'
        self.group = 2
        self.mass = 226
        self.density = 5.5
        self.melting = 973
        self.boiling = 2010
        self.heat = 0.094
        self.electronegativity = 0.9
        self.radius = No_Data
        self.oxidation = [2]
        self.charge = 0
        self.bondList = []

class Actinium(Element):
    def __init__(self):
        self.number = 89
        self.symbol = 'Ac'
        self.name = 'Actinium'
        self.group = 0
        self.mass = 227
        self.density = 10.07
        self.melting = 1323
        self.boiling = 3471
        self.heat = 0.12
        self.electronegativity = 1.1
        self.radius = No_Data
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Thorium(Element):
    def __init__(self):
        self.number = 90
        self.symbol = 'Th'
        self.name = 'Thorium'
        self.group = 0
        self.mass = 232.03806
        self.density = 11.72
        self.melting = 2115
        self.boiling = 5061
        self.heat = 0.113
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Protactinium(Element):
    def __init__(self):
        self.number = 91
        self.symbol = 'Pa'
        self.name = 'Protactinium'
        self.group = 0
        self.mass = 231.03588
        self.density = 15.37
        self.melting = 1841
        self.boiling = 4300
        self.heat = No_Data
        self.electronegativity = 1.5
        self.radius = No_Data
        self.oxidation = [2,3,4,5]
        self.charge = 0
        self.bondList = []

class Uranium(Element):
    def __init__(self):
        self.number = 92
        self.symbol = 'U'
        self.name = 'Uranium'
        self.group = 0
        self.mass = 238.02891
        self.density = 18.95
        self.melting = 1405.3
        self.boiling = 4404
        self.heat = 0.116
        self.electronegativity = 1.38
        self.radius = No_Data
        self.oxidation = [2,3,4,5,6]
        self.charge = 0
        self.bondList = []

class Neptunium(Element):
    def __init__(self):
        self.number = 93
        self.symbol = 'Np'
        self.name = 'Neptunium'
        self.group = 0
        self.mass = 237
        self.density = 20.45
        self.melting = 917
        self.boiling = 4273
        self.heat = No_Data
        self.electronegativity = 1.36
        self.radius = No_Data
        self.oxidation = [3,4,5,6,7]
        self.charge = 0
        self.bondList = []

class Plutonium(Element):
    def __init__(self):
        self.number = 94
        self.symbol = 'Pu'
        self.name = 'Plutonium'
        self.group = 0
        self.mass = 244
        self.density = 19.84
        self.melting = 912.5
        self.boiling = 3501
        self.heat = No_Data
        self.electronegativity = 1.28
        self.radius = No_Data
        self.oxidation = [3,4,5,6,7,8]
        self.charge = 0
        self.bondList = []

class Americium(Element):
    def __init__(self):
        self.number = 95
        self.symbol = 'Am'
        self.name = 'Americium'
        self.group = 0
        self.mass = 243
        self.density = 13.69
        self.melting = 1449
        self.boiling = 2880
        self.heat = No_Data
        self.electronegativity = 1.13
        self.radius = No_Data
        self.oxidation = [2,3,4,5,6,7]
        self.charge = 0
        self.bondList = []

class Curium(Element):
    def __init__(self):
        self.number = 96
        self.symbol = 'Cm'
        self.name = 'Curium'
        self.group = 0
        self.mass = 247
        self.density = 13.51
        self.melting = 1613
        self.boiling = 3383
        self.heat = No_Data
        self.electronegativity = 1.28
        self.radius = No_Data
        self.oxidation = [2,3,4,6,8]
        self.charge = 0
        self.bondList = []

class Berkelium(Element):
    def __init__(self):
        self.number = 97
        self.symbol = 'Bk'
        self.name = 'Berkelium'
        self.group = 0
        self.mass = 247
        self.density = 14.79
        self.melting = 1259
        self.boiling = 2900
        self.heat = No_Data
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Californium(Element):
    def __init__(self):
        self.number = 98
        self.symbol = 'Cf'
        self.name = 'Californium'
        self.group = 0
        self.mass = 251
        self.density = 15.1
        self.melting = 1173
        self.boiling = 1743
        self.heat = No_Data
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Einsteinium(Element):
    def __init__(self):
        self.number = 99
        self.symbol = 'Es'
        self.name = 'Einsteinium'
        self.group = 0
        self.mass = 252
        self.density = 8.84
        self.melting = 1133
        self.boiling = 1269
        self.heat = No_Data
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [2,3,4]
        self.charge = 0
        self.bondList = []

class Fermium(Element):
    def __init__(self):
        self.number = 100
        self.symbol = 'Fm'
        self.name = 'Fermium'
        self.group = 0
        self.mass = 257
        self.density = No_Data
        self.melting = 1125
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Mendelevium(Element):
    def __init__(self):
        self.number = 101
        self.symbol = 'Md'
        self.name = 'Mendelevium'
        self.group = 0
        self.mass = 258
        self.density = No_Data
        self.melting = 1100
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Nobelium(Element):
    def __init__(self):
        self.number = 102
        self.symbol = 'No'
        self.name = 'Nobelium'
        self.group = 0
        self.mass = 259
        self.density = No_Data
        self.melting = 1100
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [2,3]
        self.charge = 0
        self.bondList = []

class Lawrencium(Element):
    def __init__(self):
        self.number = 103
        self.symbol = 'Lr'
        self.name = 'Lawrencium'
        self.group = 3
        self.mass = 262
        self.density = No_Data
        self.melting = 1900
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = 1.3
        self.radius = No_Data
        self.oxidation = [3]
        self.charge = 0
        self.bondList = []

class Rutherfordium(Element):
    def __init__(self):
        self.number = 104
        self.symbol = 'Rf'
        self.name = 'Rutherfordium'
        self.group = 4
        self.mass = 267
        self.density = 23.2
        self.melting = 2400
        self.boiling = 5800
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [4]
        self.charge = 0
        self.bondList = []

class Dubnium(Element):
    def __init__(self):
        self.number = 105
        self.symbol = 'Db'
        self.name = 'Dubnium'
        self.group = 5
        self.mass = 268
        self.density = 29.3
        self.melting = No_Data
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [5]
        self.charge = 0
        self.bondList = []

class Seaborgium(Element):
    def __init__(self):
        self.number = 106
        self.symbol = 'Sg'
        self.name = 'Seaborgium'
        self.group = 6
        self.mass = 269
        self.density = 35.0
        self.melting = No_Data
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [6]
        self.charge = 0
        self.bondList = []

class Bohrium(Element):
    def __init__(self):
        self.number = 107
        self.symbol = 'Bh'
        self.name = 'Bohrium'
        self.group = 7
        self.mass = 270
        self.density = 37.1
        self.melting = No_Data
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [7]
        self.charge = 0
        self.bondList = []

class Hassium(Element):
    def __init__(self):
        self.number = 108
        self.symbol = 'Hs'
        self.name = 'Hassium'
        self.group = 8
        self.mass = 269
        self.density = 40.7
        self.melting = No_Data
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [8]
        self.charge = 0
        self.bondList = []

class Meitnerium(Element):
    def __init__(self):
        self.number = 109
        self.symbol = 'Mt'
        self.name = 'Meitnerium'
        self.group = 9
        self.mass = 278
        self.density = 37.4
        self.melting = No_Data
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [8]
        self.charge = 0
        self.bondList = []

class Darmstadtium(Element):
    def __init__(self):
        self.number = 110
        self.symbol = 'Ds'
        self.name = 'Darmstadtium'
        self.group = 10
        self.mass = 281
        self.density = 34.8
        self.melting = No_Data
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Roentgenium(Element):
    def __init__(self):
        self.number = 111
        self.symbol = 'Rg'
        self.name = 'Roentgenium'
        self.group = 11
        self.mass = 281
        self.density = 28.7
        self.melting = No_Data
        self.boiling = No_Data
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Copernicium(Element):
    def __init__(self):
        self.number = 112
        self.symbol = 'Cn'
        self.name = 'Copernicium'
        self.group = 12
        self.mass = 285
        self.density = 23.7
        self.melting = No_Data
        self.boiling = 357
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Ununtrium(Element):
    def __init__(self):
        self.number = 113
        self.symbol = 'Uut'
        self.name = 'Ununtrium'
        self.group = 13
        self.mass = 286
        self.density = 16
        self.melting = 700
        self.boiling = 1400
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Flerovium(Element):
    def __init__(self):
        self.number = 114
        self.symbol = 'Fl'
        self.name = 'Flerovium'
        self.group = 14
        self.mass = 289
        self.density = 14
        self.melting = 340
        self.boiling = 420
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Ununpentium(Element):
    def __init__(self):
        self.number = 115
        self.symbol = 'Uup'
        self.name = 'Ununpentium'
        self.group = 15
        self.mass = 288
        self.density = 13.5
        self.melting = 700
        self.boiling = 1400
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Livermorium(Element):
    def __init__(self):
        self.number = 116
        self.symbol = 'Lv'
        self.name = 'Livermorium'
        self.group = 16
        self.mass = 293
        self.density = 12.9
        self.melting = 708.5
        self.boiling = 1085
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Ununseptium(Element):
    def __init__(self):
        self.number = 117
        self.symbol = 'Uus'
        self.name = 'Ununseptium'
        self.group = 17
        self.mass = 294
        self.density = 7.2
        self.melting = 673
        self.boiling = 823
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []

class Ununoctium(Element):
    def __init__(self):
        self.number = 118
        self.symbol = 'Uuo'
        self.name = 'Ununoctium'
        self.group = 18
        self.mass = 294
        self.density = 5.0
        self.melting = 258
        self.boiling = 263
        self.heat = No_Data
        self.electronegativity = No_Data
        self.radius = No_Data
        self.oxidation = [No_Data]
        self.charge = 0
        self.bondList = []