import chemistry as chem
#import GUI


def BeginProgram():
    """Function that initializes the program""" 
   
    ###Defines the locations of the 
    ptableLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\ptable.txt'
    elementsLoc = 'C:\Users\Dan\Documents\GitHub\Chemistry\Main\elements.txt'
            
    ###Creates the initial table, then a (numpy) array version of the table, then a visual (string) version of the table
    theTable = chem.Mendeleev(ptableLoc,elementsLoc)   
    periodicTable = theTable.getTable()
    printTable = theTable.printableTable()
    
    ###Testing purposes
    print periodicTable #array version of table
    print printTable #string version of table
    print theTable #string version of a mendeleev object
    
    ###sample compound    
    testCompound = chem.Compound("CH1Cl2 CH3")  
    #print testCompound

BeginProgram()