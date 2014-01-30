import numpy as np
    
# atomic data gotten from:
# http://en.wikipedia.org/wiki/List_of_elements
# http://en.wikipedia.org/wiki/Atomic_radii_of_the_elements_(data_page)
# atomic weight in u()
# Density in g/cm^3
# Melting, Boiling Point in K
# Heat J/g*K
# Calculated radius in pm
at = "C:\\Users\Dan\Documents\GitHub\Chemistry\Main/at.txt"
num,symb,element,group,weight,density,melt,boil,heat,eneg,rad = np.genfromtxt(at,dtype='S',unpack=True)
aString = ''

for i in range(len(num)):
    aString += num[i]+' '
    aString += symb[i]+' '
    aString += element[i]+' '
    aString += group[i]+' '
    if weight[i].rfind('(') != -1:weight[i] = weight[i][:weight[i].rfind('(')]
    elif weight[i][0] == '[':weight[i] = weight[i][1:4]
    else:pass
    aString += weight[i]+' '
    if density[i] == 'nodata':aString += "'No_Data' "
    elif '(' in density[i]: aString += density[i][density[i].find('(')+1:density[i].find(')')]+' '
    else: aString += density[i] + ' '
    if melt[i] == 'nodata':aString += "'No_Data' "
    elif '[' in melt[i]:aString += melt[i][:melt[i].find('[')]+' '
    elif '(' in melt[i]: aString += melt[i][melt[i].find('(')+1:melt[i].find(')')]+' '
    else: aString += melt[i] + ' ' 
    if boil[i] == 'nodata':aString += "'No_Data' "
    elif '(' in boil[i]: aString += boil[i][boil[i].find('(')+1:boil[i].find(')')]+' '
    else: aString += boil[i] + ' ' 
    if heat[i] == 'nodata':aString += "'No_Data' "
    else: aString += heat[i] + ' '
    if eneg[i] == 'nodata':aString += "'No_Data' "
    else: aString += eneg[i] + ' '    
    if rad[i] == 'nodata':aString += "'No_Data' "
    else: aString += rad[i] + ' '
    aString += '\n'

aList = aString.split()
aList = np.array(aList).reshape(119,11)    
            
startString = "public class Chemistry{}"
startString += "\n\npublic class Element(Chemistry)\n{"
startString += "\n    public int getNum() {return number;}"
startString += "\n    public double getMass() {return mass;}"
startString += "\n    public String getName() {return name;}"
startString += "\n    public String getSymbol() {return symbol;}"
startString += "\n    public int getGroup() {return group;}"
startString += "\n    public double getDensity() {return density;}"
startString += "\n    public double getRadius() {return radius;}"
startString += "\n    public double getEneg() {return electronegativity;}"
startString += "\n    public int getOx() {return oxidation;}"
startString += "\n    public int getCharge() {return charge;}"
startString += "\n    public double getHeat() {return heat;}"
startString += "\n    public double getBoil() {return bp;}"
startString += "\n    public double getMelt() {return mp;}\n}"

mainString = '\n'
for i in range(1,len(aList)):
    mainString += "public class " + aList[i][2] + "(Element):{\n    "
    mainString += "number = " + aList[i][0] + ';\n    '
    mainString += "mass = " + aList[i][4] + ";\n    "
    mainString += "name = " + "'" + aList[i][2] + "'" + ";\n    "
    mainString += "symbol = "  + "'" + aList[i][1] + "'" + ";\n    "
    mainString += "group = " + aList[i][3] + ";\n    "
    mainString += "density = " + aList[i][5] + ";\n    "
    mainString += "radius = " + aList[i][-1] +";\n    "
    mainString += "electronegativity = " + aList[i][-2] + ";\n    "
    mainString += "oxidation = None;\n    "
    mainString += "charge = 0;\n    "
    mainString += "heat = " + aList[i][-3] + ";\n    "
    mainString += "bp = " + aList[i][-4] + ";\n    "
    if i != 118:mainString += "mp = " + aList[i][-5] + ";\n}\n"
    else:mainString += "mp = " + aList[i][-5] + ";}"
    
elementString = startString + mainString

someFile = open('C:\Users\Dan\Documents\GitHub\Chemistry\Main/elements2.java','w')
someFile.write(elementString)
someFile.close()