public class Chemistry{} 

public class Element(Chemistry)
{
    public int getNum() {return number;}
    public double getMass() {return mass}
    public String getName() {return name}
    def getSymbol(self):return self.symbol
    def getRadius(self):return self.radius
    def getEneg(self):return self.electronegativity
    def getOx(self):return self.oxidation
    def getCharge(self):return self.charge
    def getBonds(self):return self.bondList
    def addBond(self,aBond):self.bondList.append(aBond)
    def breakBond(self,index):
        try:del self.bondList[index]
        except:print 'No bond at this location'
    def changeBond(self,newBond,index):
        try:self.bondList[index] = newBond
        except:self.addBond(newBond)

class Hydrogen(Element):
    def __init__(self):
        self.number = 1
        self.mass = 1.008
        self.name = 'Hydrogen'
        self.symbol = 'H'
        self.group = 1
        self.radius = 53
        self.electronegativity = 2.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 14.304
        self.bp = 20.28
        self.mp = 14.01

class Helium(Element):
    def __init__(self):
        self.number = 2
        self.mass = 4.002602
        self.name = 'Helium'
        self.symbol = 'He'
        self.group = 18
        self.radius = 31
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 5.193
        self.bp = 4.22
        self.mp = 0.956

class Lithium(Element):
    def __init__(self):
        self.number = 3
        self.mass = 6.94
        self.name = 'Lithium'
        self.symbol = 'Li'
        self.group = 1
        self.radius = 167
        self.electronegativity = 0.98
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 3.582
        self.bp = 1560
        self.mp = 453.69

class Beryllium(Element):
    def __init__(self):
        self.number = 4
        self.mass = 9.012182
        self.name = 'Beryllium'
        self.symbol = 'Be'
        self.group = 2
        self.radius = 112
        self.electronegativity = 1.57
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 1.825
        self.bp = 2742
        self.mp = 1560

class Boron(Element):
    def __init__(self):
        self.number = 5
        self.mass = 10.81
        self.name = 'Boron'
        self.symbol = 'B'
        self.group = 13
        self.radius = 87
        self.electronegativity = 2.04
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 1.026
        self.bp = 4200
        self.mp = 2349

class Carbon(Element):
    def __init__(self):
        self.number = 6
        self.mass = 12.011
        self.name = 'Carbon'
        self.symbol = 'C'
        self.group = 14
        self.radius = 67
        self.electronegativity = 2.55
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.709
        self.bp = 4300
        self.mp = 3800

class Nitrogen(Element):
    def __init__(self):
        self.number = 7
        self.mass = 14.007
        self.name = 'Nitrogen'
        self.symbol = 'N'
        self.group = 15
        self.radius = 56
        self.electronegativity = 3.04
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 1.04
        self.bp = 77.36
        self.mp = 63.15

class Oxygen(Element):
    def __init__(self):
        self.number = 8
        self.mass = 15.999
        self.name = 'Oxygen'
        self.symbol = 'O'
        self.group = 16
        self.radius = 48
        self.electronegativity = 3.44
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.918
        self.bp = 90.2
        self.mp = 54.36

class Fluorine(Element):
    def __init__(self):
        self.number = 9
        self.mass = 18.9984032
        self.name = 'Fluorine'
        self.symbol = 'F'
        self.group = 17
        self.radius = 42
        self.electronegativity = 3.98
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.824
        self.bp = 85.03
        self.mp = 53.53

class Neon(Element):
    def __init__(self):
        self.number = 10
        self.mass = 20.1797
        self.name = 'Neon'
        self.symbol = 'Ne'
        self.group = 18
        self.radius = 38
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 1.03
        self.bp = 27.07
        self.mp = 24.56

class Sodium(Element):
    def __init__(self):
        self.number = 11
        self.mass = 22.98976928
        self.name = 'Sodium'
        self.symbol = 'Na'
        self.group = 1
        self.radius = 190
        self.electronegativity = 0.93
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 1.228
        self.bp = 1156
        self.mp = 370.87

class Magnesium(Element):
    def __init__(self):
        self.number = 12
        self.mass = 24.3059
        self.name = 'Magnesium'
        self.symbol = 'Mg'
        self.group = 2
        self.radius = 145
        self.electronegativity = 1.31
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 1.023
        self.bp = 1363
        self.mp = 923

class Aluminium(Element):
    def __init__(self):
        self.number = 13
        self.mass = 26.9815386
        self.name = 'Aluminium'
        self.symbol = 'Al'
        self.group = 13
        self.radius = 118
        self.electronegativity = 1.61
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.897
        self.bp = 2792
        self.mp = 933.47

class Silicon(Element):
    def __init__(self):
        self.number = 14
        self.mass = 28.085
        self.name = 'Silicon'
        self.symbol = 'Si'
        self.group = 14
        self.radius = 111
        self.electronegativity = 1.9
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.705
        self.bp = 3538
        self.mp = 1687

class Phosphorus(Element):
    def __init__(self):
        self.number = 15
        self.mass = 30.973762
        self.name = 'Phosphorus'
        self.symbol = 'P'
        self.group = 15
        self.radius = 98
        self.electronegativity = 2.19
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.769
        self.bp = 550
        self.mp = 317.3

class Sulfur(Element):
    def __init__(self):
        self.number = 16
        self.mass = 32.06
        self.name = 'Sulfur'
        self.symbol = 'S'
        self.group = 16
        self.radius = 88
        self.electronegativity = 2.58
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.71
        self.bp = 717.87
        self.mp = 388.36

class Chlorine(Element):
    def __init__(self):
        self.number = 17
        self.mass = 35.45
        self.name = 'Chlorine'
        self.symbol = 'Cl'
        self.group = 17
        self.radius = 79
        self.electronegativity = 3.16
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.479
        self.bp = 239.11
        self.mp = 171.6

class Argon(Element):
    def __init__(self):
        self.number = 18
        self.mass = 39.948
        self.name = 'Argon'
        self.symbol = 'Ar'
        self.group = 18
        self.radius = 71
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.52
        self.bp = 87.3
        self.mp = 83.8

class Potassium(Element):
    def __init__(self):
        self.number = 19
        self.mass = 39.0983
        self.name = 'Potassium'
        self.symbol = 'K'
        self.group = 1
        self.radius = 243
        self.electronegativity = 0.82
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.757
        self.bp = 1032
        self.mp = 336.53

class Calcium(Element):
    def __init__(self):
        self.number = 20
        self.mass = 40.078
        self.name = 'Calcium'
        self.symbol = 'Ca'
        self.group = 2
        self.radius = 194
        self.electronegativity = 1
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.647
        self.bp = 1757
        self.mp = 1115

class Scandium(Element):
    def __init__(self):
        self.number = 21
        self.mass = 44.955912
        self.name = 'Scandium'
        self.symbol = 'Sc'
        self.group = 3
        self.radius = 184
        self.electronegativity = 1.36
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.568
        self.bp = 3109
        self.mp = 1814

class Titanium(Element):
    def __init__(self):
        self.number = 22
        self.mass = 47.867
        self.name = 'Titanium'
        self.symbol = 'Ti'
        self.group = 4
        self.radius = 176
        self.electronegativity = 1.54
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.523
        self.bp = 3560
        self.mp = 1941

class Vanadium(Element):
    def __init__(self):
        self.number = 23
        self.mass = 50.9415
        self.name = 'Vanadium'
        self.symbol = 'V'
        self.group = 5
        self.radius = 171
        self.electronegativity = 1.63
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.489
        self.bp = 3680
        self.mp = 2183

class Chromium(Element):
    def __init__(self):
        self.number = 24
        self.mass = 51.9961
        self.name = 'Chromium'
        self.symbol = 'Cr'
        self.group = 6
        self.radius = 166
        self.electronegativity = 1.66
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.449
        self.bp = 2944
        self.mp = 2180

class Manganese(Element):
    def __init__(self):
        self.number = 25
        self.mass = 54.938045
        self.name = 'Manganese'
        self.symbol = 'Mn'
        self.group = 7
        self.radius = 161
        self.electronegativity = 1.55
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.479
        self.bp = 2334
        self.mp = 1519

class Iron(Element):
    def __init__(self):
        self.number = 26
        self.mass = 55.845
        self.name = 'Iron'
        self.symbol = 'Fe'
        self.group = 8
        self.radius = 156
        self.electronegativity = 1.83
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.449
        self.bp = 3134
        self.mp = 1811

class Cobalt(Element):
    def __init__(self):
        self.number = 27
        self.mass = 58.933195
        self.name = 'Cobalt'
        self.symbol = 'Co'
        self.group = 9
        self.radius = 152
        self.electronegativity = 1.88
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.421
        self.bp = 3200
        self.mp = 1768

class Nickel(Element):
    def __init__(self):
        self.number = 28
        self.mass = 58.6934
        self.name = 'Nickel'
        self.symbol = 'Ni'
        self.group = 10
        self.radius = 149
        self.electronegativity = 1.91
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.444
        self.bp = 3186
        self.mp = 1728

class Copper(Element):
    def __init__(self):
        self.number = 29
        self.mass = 63.546
        self.name = 'Copper'
        self.symbol = 'Cu'
        self.group = 11
        self.radius = 145
        self.electronegativity = 1.9
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.385
        self.bp = 2835
        self.mp = 1357.77

class Zinc(Element):
    def __init__(self):
        self.number = 30
        self.mass = 65.38
        self.name = 'Zinc'
        self.symbol = 'Zn'
        self.group = 12
        self.radius = 142
        self.electronegativity = 1.65
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.388
        self.bp = 1180
        self.mp = 692.88

class Gallium(Element):
    def __init__(self):
        self.number = 31
        self.mass = 69.723
        self.name = 'Gallium'
        self.symbol = 'Ga'
        self.group = 13
        self.radius = 136
        self.electronegativity = 1.81
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.371
        self.bp = 2477
        self.mp = 302.9146

class Germanium(Element):
    def __init__(self):
        self.number = 32
        self.mass = 72.630
        self.name = 'Germanium'
        self.symbol = 'Ge'
        self.group = 14
        self.radius = 125
        self.electronegativity = 2.01
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.32
        self.bp = 3106
        self.mp = 1211.4

class Arsenic(Element):
    def __init__(self):
        self.number = 33
        self.mass = 74.92160
        self.name = 'Arsenic'
        self.symbol = 'As'
        self.group = 15
        self.radius = 114
        self.electronegativity = 2.18
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.329
        self.bp = 887
        self.mp = 1090

class Selenium(Element):
    def __init__(self):
        self.number = 34
        self.mass = 78.96
        self.name = 'Selenium'
        self.symbol = 'Se'
        self.group = 16
        self.radius = 103
        self.electronegativity = 2.55
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.321
        self.bp = 958
        self.mp = 453

class Bromine(Element):
    def __init__(self):
        self.number = 35
        self.mass = 79.9049
        self.name = 'Bromine'
        self.symbol = 'Br'
        self.group = 17
        self.radius = 94
        self.electronegativity = 2.96
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.474
        self.bp = 332
        self.mp = 265.8

class Krypton(Element):
    def __init__(self):
        self.number = 36
        self.mass = 83.798
        self.name = 'Krypton'
        self.symbol = 'Kr'
        self.group = 18
        self.radius = 88
        self.electronegativity = 3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.248
        self.bp = 119.93
        self.mp = 115.79

class Rubidium(Element):
    def __init__(self):
        self.number = 37
        self.mass = 85.4678
        self.name = 'Rubidium'
        self.symbol = 'Rb'
        self.group = 1
        self.radius = 265
        self.electronegativity = 0.82
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.363
        self.bp = 961
        self.mp = 312.46

class Strontium(Element):
    def __init__(self):
        self.number = 38
        self.mass = 87.62
        self.name = 'Strontium'
        self.symbol = 'Sr'
        self.group = 2
        self.radius = 219
        self.electronegativity = 0.95
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.301
        self.bp = 1655
        self.mp = 1050

class Yttrium(Element):
    def __init__(self):
        self.number = 39
        self.mass = 88.90585
        self.name = 'Yttrium'
        self.symbol = 'Y'
        self.group = 3
        self.radius = 212
        self.electronegativity = 1.22
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.298
        self.bp = 3609
        self.mp = 1799

class Zirconium(Element):
    def __init__(self):
        self.number = 40
        self.mass = 91.224
        self.name = 'Zirconium'
        self.symbol = 'Zr'
        self.group = 4
        self.radius = 206
        self.electronegativity = 1.33
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.278
        self.bp = 4682
        self.mp = 2128

class Niobium(Element):
    def __init__(self):
        self.number = 41
        self.mass = 92.90638
        self.name = 'Niobium'
        self.symbol = 'Nb'
        self.group = 5
        self.radius = 198
        self.electronegativity = 1.6
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.265
        self.bp = 5017
        self.mp = 2750

class Molybdenum(Element):
    def __init__(self):
        self.number = 42
        self.mass = 95.96
        self.name = 'Molybdenum'
        self.symbol = 'Mo'
        self.group = 6
        self.radius = 190
        self.electronegativity = 2.16
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.251
        self.bp = 4912
        self.mp = 2896

class Technetium(Element):
    def __init__(self):
        self.number = 43
        self.mass = 98]
        self.name = 'Technetium'
        self.symbol = 'Tc'
        self.group = 7
        self.radius = 183
        self.electronegativity = 1.9
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 4538
        self.mp = 2430

class Ruthenium(Element):
    def __init__(self):
        self.number = 44
        self.mass = 101.07
        self.name = 'Ruthenium'
        self.symbol = 'Ru'
        self.group = 8
        self.radius = 178
        self.electronegativity = 2.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.238
        self.bp = 4423
        self.mp = 2607

class Rhodium(Element):
    def __init__(self):
        self.number = 45
        self.mass = 102.90550
        self.name = 'Rhodium'
        self.symbol = 'Rh'
        self.group = 9
        self.radius = 173
        self.electronegativity = 2.28
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.243
        self.bp = 3968
        self.mp = 2237

class Palladium(Element):
    def __init__(self):
        self.number = 46
        self.mass = 106.42
        self.name = 'Palladium'
        self.symbol = 'Pd'
        self.group = 10
        self.radius = 169
        self.electronegativity = 2.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.244
        self.bp = 3236
        self.mp = 1828.05

class Silver(Element):
    def __init__(self):
        self.number = 47
        self.mass = 107.8682
        self.name = 'Silver'
        self.symbol = 'Ag'
        self.group = 11
        self.radius = 165
        self.electronegativity = 1.93
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.235
        self.bp = 2435
        self.mp = 1234.93

class Cadmium(Element):
    def __init__(self):
        self.number = 48
        self.mass = 112.411
        self.name = 'Cadmium'
        self.symbol = 'Cd'
        self.group = 12
        self.radius = 161
        self.electronegativity = 1.69
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.232
        self.bp = 1040
        self.mp = 594.22

class Indium(Element):
    def __init__(self):
        self.number = 49
        self.mass = 114.818
        self.name = 'Indium'
        self.symbol = 'In'
        self.group = 13
        self.radius = 156
        self.electronegativity = 1.78
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.233
        self.bp = 2345
        self.mp = 429.75

class Tin(Element):
    def __init__(self):
        self.number = 50
        self.mass = 118.710
        self.name = 'Tin'
        self.symbol = 'Sn'
        self.group = 14
        self.radius = 145
        self.electronegativity = 1.96
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.228
        self.bp = 2875
        self.mp = 505.08

class Antimony(Element):
    def __init__(self):
        self.number = 51
        self.mass = 121.760
        self.name = 'Antimony'
        self.symbol = 'Sb'
        self.group = 15
        self.radius = 133
        self.electronegativity = 2.05
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.207
        self.bp = 1860
        self.mp = 903.78

class Tellurium(Element):
    def __init__(self):
        self.number = 52
        self.mass = 127.60
        self.name = 'Tellurium'
        self.symbol = 'Te'
        self.group = 16
        self.radius = 123
        self.electronegativity = 2.1
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.202
        self.bp = 1261
        self.mp = 722.66

class Iodine(Element):
    def __init__(self):
        self.number = 53
        self.mass = 126.90447
        self.name = 'Iodine'
        self.symbol = 'I'
        self.group = 17
        self.radius = 115
        self.electronegativity = 2.66
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.214
        self.bp = 457.4
        self.mp = 386.85

class Xenon(Element):
    def __init__(self):
        self.number = 54
        self.mass = 131.293
        self.name = 'Xenon'
        self.symbol = 'Xe'
        self.group = 18
        self.radius = 108
        self.electronegativity = 2.6
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.158
        self.bp = 165.03
        self.mp = 161.4

class Caesium(Element):
    def __init__(self):
        self.number = 55
        self.mass = 132.9054519
        self.name = 'Caesium'
        self.symbol = 'Cs'
        self.group = 1
        self.radius = 298
        self.electronegativity = 0.79
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.242
        self.bp = 944
        self.mp = 301.59

class Barium(Element):
    def __init__(self):
        self.number = 56
        self.mass = 137.327
        self.name = 'Barium'
        self.symbol = 'Ba'
        self.group = 2
        self.radius = 253
        self.electronegativity = 0.89
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.204
        self.bp = 2170
        self.mp = 1000

class Lanthanum(Element):
    def __init__(self):
        self.number = 57
        self.mass = 138.90547
        self.name = 'Lanthanum'
        self.symbol = 'La'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.1
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.195
        self.bp = 3737
        self.mp = 1193

class Cerium(Element):
    def __init__(self):
        self.number = 58
        self.mass = 140.116
        self.name = 'Cerium'
        self.symbol = 'Ce'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.12
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.192
        self.bp = 3716
        self.mp = 1068

class Praseodymium(Element):
    def __init__(self):
        self.number = 59
        self.mass = 140.90765
        self.name = 'Praseodymium'
        self.symbol = 'Pr'
        self.group = 0
        self.radius = 247
        self.electronegativity = 1.13
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.193
        self.bp = 3793
        self.mp = 1208

class Neodymium(Element):
    def __init__(self):
        self.number = 60
        self.mass = 144.242
        self.name = 'Neodymium'
        self.symbol = 'Nd'
        self.group = 0
        self.radius = 206
        self.electronegativity = 1.14
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.19
        self.bp = 3347
        self.mp = 1297

class Promethium(Element):
    def __init__(self):
        self.number = 61
        self.mass = 145
        self.name = 'Promethium'
        self.symbol = 'Pm'
        self.group = 0
        self.radius = 205
        self.electronegativity = 1.13
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 3273
        self.mp = 1315

class Samarium(Element):
    def __init__(self):
        self.number = 62
        self.mass = 150.36
        self.name = 'Samarium'
        self.symbol = 'Sm'
        self.group = 0
        self.radius = 238
        self.electronegativity = 1.17
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.197
        self.bp = 2067
        self.mp = 1345

class Europium(Element):
    def __init__(self):
        self.number = 63
        self.mass = 151.964
        self.name = 'Europium'
        self.symbol = 'Eu'
        self.group = 0
        self.radius = 231
        self.electronegativity = 1.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.182
        self.bp = 1802
        self.mp = 1099

class Gadolinium(Element):
    def __init__(self):
        self.number = 64
        self.mass = 157.25
        self.name = 'Gadolinium'
        self.symbol = 'Gd'
        self.group = 0
        self.radius = 233
        self.electronegativity = 1.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.236
        self.bp = 3546
        self.mp = 1585

class Terbium(Element):
    def __init__(self):
        self.number = 65
        self.mass = 158.92535
        self.name = 'Terbium'
        self.symbol = 'Tb'
        self.group = 0
        self.radius = 225
        self.electronegativity = 1.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.182
        self.bp = 3503
        self.mp = 1629

class Dysprosium(Element):
    def __init__(self):
        self.number = 66
        self.mass = 162.500
        self.name = 'Dysprosium'
        self.symbol = 'Dy'
        self.group = 0
        self.radius = 228
        self.electronegativity = 1.22
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.17
        self.bp = 2840
        self.mp = 1680

class Holmium(Element):
    def __init__(self):
        self.number = 67
        self.mass = 164.93032
        self.name = 'Holmium'
        self.symbol = 'Ho'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.23
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.165
        self.bp = 2993
        self.mp = 1734

class Erbium(Element):
    def __init__(self):
        self.number = 68
        self.mass = 167.259
        self.name = 'Erbium'
        self.symbol = 'Er'
        self.group = 0
        self.radius = 226
        self.electronegativity = 1.24
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.168
        self.bp = 3141
        self.mp = 1802

class Thulium(Element):
    def __init__(self):
        self.number = 69
        self.mass = 168.93421
        self.name = 'Thulium'
        self.symbol = 'Tm'
        self.group = 0
        self.radius = 222
        self.electronegativity = 1.25
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.16
        self.bp = 2223
        self.mp = 1818

class Ytterbium(Element):
    def __init__(self):
        self.number = 70
        self.mass = 173.054
        self.name = 'Ytterbium'
        self.symbol = 'Yb'
        self.group = 0
        self.radius = 222
        self.electronegativity = 1.1
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.155
        self.bp = 1469
        self.mp = 1097

class Lutetium(Element):
    def __init__(self):
        self.number = 71
        self.mass = 174.9668
        self.name = 'Lutetium'
        self.symbol = 'Lu'
        self.group = 3
        self.radius = 217
        self.electronegativity = 1.27
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.154
        self.bp = 3675
        self.mp = 1925

class Hafnium(Element):
    def __init__(self):
        self.number = 72
        self.mass = 178.49
        self.name = 'Hafnium'
        self.symbol = 'Hf'
        self.group = 4
        self.radius = 208
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.144
        self.bp = 4876
        self.mp = 2506

class Tantalum(Element):
    def __init__(self):
        self.number = 73
        self.mass = 180.94788
        self.name = 'Tantalum'
        self.symbol = 'Ta'
        self.group = 5
        self.radius = 200
        self.electronegativity = 1.5
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.14
        self.bp = 5731
        self.mp = 3290

class Tungsten(Element):
    def __init__(self):
        self.number = 74
        self.mass = 183.84
        self.name = 'Tungsten'
        self.symbol = 'W'
        self.group = 6
        self.radius = 193
        self.electronegativity = 2.36
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.132
        self.bp = 5828
        self.mp = 3695

class Rhenium(Element):
    def __init__(self):
        self.number = 75
        self.mass = 186.207
        self.name = 'Rhenium'
        self.symbol = 'Re'
        self.group = 7
        self.radius = 188
        self.electronegativity = 1.9
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.137
        self.bp = 5869
        self.mp = 3459

class Osmium(Element):
    def __init__(self):
        self.number = 76
        self.mass = 190.23
        self.name = 'Osmium'
        self.symbol = 'Os'
        self.group = 8
        self.radius = 185
        self.electronegativity = 2.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.13
        self.bp = 5285
        self.mp = 3306

class Iridium(Element):
    def __init__(self):
        self.number = 77
        self.mass = 192.217
        self.name = 'Iridium'
        self.symbol = 'Ir'
        self.group = 9
        self.radius = 180
        self.electronegativity = 2.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.131
        self.bp = 4701
        self.mp = 2719

class Platinum(Element):
    def __init__(self):
        self.number = 78
        self.mass = 195.084
        self.name = 'Platinum'
        self.symbol = 'Pt'
        self.group = 10
        self.radius = 177
        self.electronegativity = 2.28
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.133
        self.bp = 4098
        self.mp = 2041.4

class Gold(Element):
    def __init__(self):
        self.number = 79
        self.mass = 196.966569
        self.name = 'Gold'
        self.symbol = 'Au'
        self.group = 11
        self.radius = 174
        self.electronegativity = 2.54
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.129
        self.bp = 3129
        self.mp = 1337.33

class Mercury(Element):
    def __init__(self):
        self.number = 80
        self.mass = 200.592
        self.name = 'Mercury'
        self.symbol = 'Hg'
        self.group = 12
        self.radius = 171
        self.electronegativity = 2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.14
        self.bp = 629.88
        self.mp = 234.43

class Thallium(Element):
    def __init__(self):
        self.number = 81
        self.mass = 204.389
        self.name = 'Thallium'
        self.symbol = 'Tl'
        self.group = 13
        self.radius = 156
        self.electronegativity = 1.62
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.129
        self.bp = 1746
        self.mp = 577

class Lead(Element):
    def __init__(self):
        self.number = 82
        self.mass = 207.2
        self.name = 'Lead'
        self.symbol = 'Pb'
        self.group = 14
        self.radius = 154
        self.electronegativity = 1.87
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.129
        self.bp = 2022
        self.mp = 600.61

class Bismuth(Element):
    def __init__(self):
        self.number = 83
        self.mass = 208.98040
        self.name = 'Bismuth'
        self.symbol = 'Bi'
        self.group = 15
        self.radius = 143
        self.electronegativity = 2.02
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.122
        self.bp = 1837
        self.mp = 544.7

class Polonium(Element):
    def __init__(self):
        self.number = 84
        self.mass = 209
        self.name = 'Polonium'
        self.symbol = 'Po'
        self.group = 16
        self.radius = 135
        self.electronegativity = 2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 1235
        self.mp = 527

class Astatine(Element):
    def __init__(self):
        self.number = 85
        self.mass = 210
        self.name = 'Astatine'
        self.symbol = 'At'
        self.group = 17
        self.radius = 'No_Data'
        self.electronegativity = 2.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 610
        self.mp = 575

class Radon(Element):
    def __init__(self):
        self.number = 86
        self.mass = 222
        self.name = 'Radon'
        self.symbol = 'Rn'
        self.group = 18
        self.radius = 120
        self.electronegativity = 2.2
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.094
        self.bp = 211.3
        self.mp = 202

class Francium(Element):
    def __init__(self):
        self.number = 87
        self.mass = 223
        self.name = 'Francium'
        self.symbol = 'Fr'
        self.group = 1
        self.radius = 'No_Data'
        self.electronegativity = 0.7
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 950
        self.mp = 300

class Radium(Element):
    def __init__(self):
        self.number = 88
        self.mass = 226
        self.name = 'Radium'
        self.symbol = 'Ra'
        self.group = 2
        self.radius = 'No_Data'
        self.electronegativity = 0.9
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.094
        self.bp = 2010
        self.mp = 973

class Actinium(Element):
    def __init__(self):
        self.number = 89
        self.mass = 227
        self.name = 'Actinium'
        self.symbol = 'Ac'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.1
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.12
        self.bp = 3471
        self.mp = 1323

class Thorium(Element):
    def __init__(self):
        self.number = 90
        self.mass = 232.03806
        self.name = 'Thorium'
        self.symbol = 'Th'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.113
        self.bp = 5061
        self.mp = 2115

class Protactinium(Element):
    def __init__(self):
        self.number = 91
        self.mass = 231.03588
        self.name = 'Protactinium'
        self.symbol = 'Pa'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.5
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 4300
        self.mp = 1841

class Uranium(Element):
    def __init__(self):
        self.number = 92
        self.mass = 238.02891
        self.name = 'Uranium'
        self.symbol = 'U'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.38
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 0.116
        self.bp = 4404
        self.mp = 1405.3

class Neptunium(Element):
    def __init__(self):
        self.number = 93
        self.mass = 237
        self.name = 'Neptunium'
        self.symbol = 'Np'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.36
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 4273
        self.mp = 917

class Plutonium(Element):
    def __init__(self):
        self.number = 94
        self.mass = 244
        self.name = 'Plutonium'
        self.symbol = 'Pu'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.28
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 3501
        self.mp = 912.5

class Americium(Element):
    def __init__(self):
        self.number = 95
        self.mass = 243
        self.name = 'Americium'
        self.symbol = 'Am'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.13
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 2880
        self.mp = 1449

class Curium(Element):
    def __init__(self):
        self.number = 96
        self.mass = 247
        self.name = 'Curium'
        self.symbol = 'Cm'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.28
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 3383
        self.mp = 1613

class Berkelium(Element):
    def __init__(self):
        self.number = 97
        self.mass = 247
        self.name = 'Berkelium'
        self.symbol = 'Bk'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 2900
        self.mp = 1259

class Californium(Element):
    def __init__(self):
        self.number = 98
        self.mass = 251
        self.name = 'Californium'
        self.symbol = 'Cf'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 1743
        self.mp = 1173

class Einsteinium(Element):
    def __init__(self):
        self.number = 99
        self.mass = 252
        self.name = 'Einsteinium'
        self.symbol = 'Es'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 1269
        self.mp = 1133

class Fermium(Element):
    def __init__(self):
        self.number = 100
        self.mass = 257
        self.name = 'Fermium'
        self.symbol = 'Fm'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 1125

class Mendelevium(Element):
    def __init__(self):
        self.number = 101
        self.mass = 258
        self.name = 'Mendelevium'
        self.symbol = 'Md'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 1100

class Nobelium(Element):
    def __init__(self):
        self.number = 102
        self.mass = 259
        self.name = 'Nobelium'
        self.symbol = 'No'
        self.group = 0
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 1100

class Lawrencium(Element):
    def __init__(self):
        self.number = 103
        self.mass = 262
        self.name = 'Lawrencium'
        self.symbol = 'Lr'
        self.group = 3
        self.radius = 'No_Data'
        self.electronegativity = 1.3
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 1900

class Rutherfordium(Element):
    def __init__(self):
        self.number = 104
        self.mass = 267
        self.name = 'Rutherfordium'
        self.symbol = 'Rf'
        self.group = 4
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 5800
        self.mp = 2400

class Dubnium(Element):
    def __init__(self):
        self.number = 105
        self.mass = 268
        self.name = 'Dubnium'
        self.symbol = 'Db'
        self.group = 5
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 'No_Data'

class Seaborgium(Element):
    def __init__(self):
        self.number = 106
        self.mass = 269
        self.name = 'Seaborgium'
        self.symbol = 'Sg'
        self.group = 6
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 'No_Data'

class Bohrium(Element):
    def __init__(self):
        self.number = 107
        self.mass = 270
        self.name = 'Bohrium'
        self.symbol = 'Bh'
        self.group = 7
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 'No_Data'

class Hassium(Element):
    def __init__(self):
        self.number = 108
        self.mass = 269
        self.name = 'Hassium'
        self.symbol = 'Hs'
        self.group = 8
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 'No_Data'

class Meitnerium(Element):
    def __init__(self):
        self.number = 109
        self.mass = 278
        self.name = 'Meitnerium'
        self.symbol = 'Mt'
        self.group = 9
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 'No_Data'

class Darmstadtium(Element):
    def __init__(self):
        self.number = 110
        self.mass = 281
        self.name = 'Darmstadtium'
        self.symbol = 'Ds'
        self.group = 10
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 'No_Data'

class Roentgenium(Element):
    def __init__(self):
        self.number = 111
        self.mass = 281
        self.name = 'Roentgenium'
        self.symbol = 'Rg'
        self.group = 11
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 'No_Data'
        self.mp = 'No_Data'

class Copernicium(Element):
    def __init__(self):
        self.number = 112
        self.mass = 285
        self.name = 'Copernicium'
        self.symbol = 'Cn'
        self.group = 12
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 357
        self.mp = 'No_Data'

class Ununtrium(Element):
    def __init__(self):
        self.number = 113
        self.mass = 286
        self.name = 'Ununtrium'
        self.symbol = 'Uut'
        self.group = 13
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 1400
        self.mp = 700

class Flerovium(Element):
    def __init__(self):
        self.number = 114
        self.mass = 289
        self.name = 'Flerovium'
        self.symbol = 'Fl'
        self.group = 14
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 420
        self.mp = 340

class Ununpentium(Element):
    def __init__(self):
        self.number = 115
        self.mass = 288
        self.name = 'Ununpentium'
        self.symbol = 'Uup'
        self.group = 15
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 1400
        self.mp = 700

class Livermorium(Element):
    def __init__(self):
        self.number = 116
        self.mass = 293
        self.name = 'Livermorium'
        self.symbol = 'Lv'
        self.group = 16
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 1085
        self.mp = 708.5

class Ununseptium(Element):
    def __init__(self):
        self.number = 117
        self.mass = 294
        self.name = 'Ununseptium'
        self.symbol = 'Uus'
        self.group = 17
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 823
        self.mp = 673

class Ununoctium(Element):
    def __init__(self):
        self.number = 118
        self.mass = 294
        self.name = 'Ununoctium'
        self.symbol = 'Uuo'
        self.group = 18
        self.radius = 'No_Data'
        self.electronegativity = 'No_Data'
        self.oxidation = None
        self.charge = 0
        self.bondList = []
        self.heat = 'No_Data'
        self.bp = 263
        self.mp = 258