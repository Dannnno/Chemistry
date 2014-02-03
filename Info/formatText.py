Base = 'C:\Users\Dan\Documents\GitHub\Chemistry\Info'
a = Base + '/ab.txt'

fileA = open(a,'r')
aList = []
for line in fileA:
    newLine = line.split()
    aList.append(newLine)

# file A = C:\Users\Dan\Documents\GitHub\Chemistry\Info/ab.txt
#
# Index [0] is Num 
# Index [1] is Sym
# Index [2] is Element
# Index [3] is Group
# Index [4] is Weight
# Index [5] is Density
# Index [6] is Melting
# Index [7] is Boiling
# Index [8] is Heat
# Index [9] is Eneg
# Index [10] is Radius
# Index [11] is Oxidation
"""
print '# file A = ' + a + '\n#'
for i in range(len(aList[0])):
    print '# Index ['+str(i)+'] is '+aList[0][i]
"""

theStr = ''
for i in range(len(aList)):
    for j in range(len(aList[i])):
        if j in [0,1,3]:
            theStr += aList[i][j].ljust(6)
        elif j in [2,4,5]:
            theStr += aList[i][j].ljust(15)
        else:
            theStr += aList[i][j].ljust(10)
    if i != len(aList)-1:
        theStr += '\n'
        
fileA.close()
fileA = open(a,'w')
fileA.seek(0)
fileA.write(theStr)
fileA.close()