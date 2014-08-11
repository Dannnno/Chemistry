"""This program is intended to test the various aspects of my parser

"""

import CheML

def clean_print_molecule(adict):
    
    if not isinstance(adict, dict):
        print "Not a dictionary"
        return
        
    for key in sorted(adict.keys()):
        print key
        if isinstance(adict[key], dict):
            # print("\t", end="") - only for python 3
            print " "
            clean_print_molecule(adict[key])
        else:
            print "", adict[key]
        if key == sorted(adict.keys())[-1]:
            print "\n"
    
                            
filepaths = []
directory = "C:/Users/Dan/Desktop/Programming/1 - GitHub/Chemistry/CML work/"
filepaths.append(''.join([directory, "CML_1.cml"]))
filepaths.append(''.join([directory, "CML_2.cml"]))

molecules = {}
try:
    broken_files = []
    for i, afile in enumerate(filepaths):
        #if os.path.exists(afile):
            a_molecule = CheML.CMLParser(afile)
            molecules[''.join(["m", str(i+1)])] = a_molecule.molecule
        #else:
        #    broken_files.append(afile)
    if broken_files:
        raise CheML.CMLException("Broken File(s) at:\n " + "\n ".join(broken_files))

except CheML.CMLException as e:
    print e
    
print "\nMolecules parsed:\n"
#clean_print_molecule(molecules)
for mol_id in molecules:
    print mol_id, molecules[mol_id]

CheML.CMLBuilder(molecules, "CML_3.cml")