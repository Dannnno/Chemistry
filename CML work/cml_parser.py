try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
    
# store molecules, atoms and bonds in dictionaries
# consider using classes to encapsulate each? or just tuples?


molecules = {}
    
with open("CML_1.cml", "r") as cml:
    tree = ET.parse(cml)
    atoms = {}
    bonds = {}
    try:
        elements = tree.findall("atomArray")
        if elements == []: raise Exception("No atomArray in the molecule")
        for element in elements:
            sub_elements = element.findall("atom")
            if sub_elements == []: raise Exception("No atoms in the atomArray")
            for sub_element in sub_elements:
                subs = sub_element.findall("string")
                if subs == []: raise Exception("Atom has no information")                
                for sub in subs:
                    atoms[sub_element.attrib['id']] = sub.text
    
        print "atoms in molecule ", atoms
        
        elements = tree.findall("bondArray")
        if elements == []: raise Exception("No bondArray in the molecule")
        for element in tree.findall("bondArray"):
            sub_elements = element.findall("bond")
            if sub_elements == []: raise Exception("No bonds in the bondArray")                            
            for sub_element in sub_elements:
                bonds[sub_element.attrib['id']] = ()
                subs = sub_element.findall("string")
                if subs == []: raise Exception("Bond has no information")
                for sub in subs:
                    bonds[sub_element.attrib['id']] += (sub.text,)
         
        print "bonds in molecule ", bonds       
        
        molecules["m1"] = (atoms, bonds)
        
    except Exception as e:
        print "Aborting:", e
    
print molecules