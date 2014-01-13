import numpy as np

aList = [['Carbon', [['Carbon',[['Hydrogen'], '3']], '1', ['Hydrogen'], '1', ['Chlorine'], '2']]]
size = (10*len(aList)+1)**2
sidelen = int(np.sqrt(size))
thestructure = np.empty((sidelen,sidelen), dtype = object)
middle = int(np.divide(len(thestructure),2))
i=middle
j=2
k=0


def branching(anObject,structure,location):
    #Creates the components
    primary = anObject[0]
    substituents = anObject[1:]
    print primary,substituents
    locDict = {}
    
    for i in range(len(substituents)):
        try:
            locDict[i] = int(substituents[i])
        except ValueError:
            pass
        except TypeError:
            pass
            
    locKeys = locDict.keys();locKeys.sort();locKeys.reverse()
    for item in locKeys:
        theElement = substituents[item-1]
        aNum = int(substituents.pop(item))
        if aNum > 1:
            for i in range(aNum-1):
                substituents.insert(i+item,theElement)

    locX = location[0]
    locY = location[1]
    structure[locY][locX] = primary
    
    #Checks if the 4 cardinal points are occupied
    cardinals = [structure[locY-2][locX], #Checks the point above
                 structure[locY][locX-2], #Checks the point to the left
                 structure[locY+2][locX], #Checks the point below
                 structure[locY][locX+2]] #Checks the point to the right

    status = [] #reports on the four cardinal positions (True if empty, False if not)

    for direction in cardinals:
        if direction == None:
            status.append(True)
        else:
            status.append(False)
                
    i=1
    j=0

    for point in status:
        if j <= len(substituents)-1:
            if point:
                theElement = substituents[j]
                aBool = False
                if type(theElement) != type(''):
                    for part in theElement:
                        if type(part) == type([]) or type(part) == type(np.zeros(1)):
                            aBool = True
                if aBool:
                    print structure
                    if i == 1:
                        tempstructure = branching(theElement,structure,[locX,locY-2])
                        structure = tempstructure
                    if i == 2:
                        tempstructure = branching(theElement,structure,[locX-2,locY])
                        structure = tempstructure
                    if i == 3:
                        tempstructure = branching(theElement,structure,[locX,locY+2])
                        structure = tempstructure
                    if i == 4:
                        tempstructure = branching(theElement,structure,[locX+2,locY])
                        structure = tempstructure
                    j+=1
                else:
                    print structure
                    if i == 1:
                        #Put something north
                        structure[locY-2][locX] = theElement
                        #structure[locY-1][locX] = Bond(primary,secondaries[j],1)
                        #bothBonds(primary,secondaries[j],1)
                    if i == 2:
                        #Put something west
                        structure[locY][locX-2] = theElement
                        #structure[locY][locX-1] = Bond(primary,secondaries[j],1)
                        #bothBonds(primary,secondaries[j],1)
                    if i == 3:
                        #Put something south
                        structure[locY+2][locX] = theElement
                        #structure[locY+1][locX] = Bond(primary,secondaries[j],1)
                        #bothBonds(primary,secondaries[j],1)
                    if i == 4:
                        #Put something east
                        structure[locY][locX+2] = theElement
                        #structure[locY][locX+1] = Bond(primary,secondaries[j],1)
                        #bothBonds(primary,secondaries[j],1)
                    j +=1
        i+=1

    return structure

for part in aList:
    thestructure = branching(part,thestructure,[j,i])
    print thestructure