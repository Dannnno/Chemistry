"""This module is used to parse CML (Chemical Markup Language) an
extension of XML.  The XML library is extended to work with the
tags and structure of the CML language.  
"""
# Needs work improving run time for larger molecules
# Need to consider the iterparse option
# Consider other support

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
       
tags = ["atomArray", 
        "molecule", 
        "atom", 
        "bond", 
        "bondArray", 
        "string"]
        
attributes = ["builtin=", 
              "convention=", 
              "title=", 
              "id=", 
              "type="]

builtin = ["atomRef", 
           "order", 
           "elementType"]      

class CMLException(Exception):
    """The base CML Exception class"""
    
    def __init__(self, err_message="Problem parsing CML file"):
        """The exception should generally be passed a more specific message"""
        self.message = err_message
        
    def __repr__(self):
        return self.message
        
    def __str__(self):
        return self.message


class CMLParser(object):
    """The base CMLParser class"""
    
    def __init__(self, CML): 
        """CML should be an (open) file object or a string filepath"""
        
        self.molecule = {}
        self.atoms = {}
        self.bonds = {}
        self.CML = CML
        self.molecule["atoms"] = self.atoms
        self.molecule["bonds"] = self.bonds
        
        try:
            if isinstance(self.CML, file): 
                if self.CML.closed:
                    raise CMLException("CML file has been closed")
        
            elif isinstance(CML, basestring):
                self.CML = open(self.CML, "r")
                
            else:
                raise CMLException("Not a valid CML file")
        
        except CMLException as e:
            print e
            return
            
        else:
            self.tree = ET.parse(self.CML)
            try:
                elements = self.tree.findall("atomArray")
                if elements == []: raise CMLException("No atomArray in the molecule")
                for element in elements:
                    sub_elements = element.findall("atom")
                    if sub_elements == []: raise CMLException("No atoms in the atomArray")
                    for sub_element in sub_elements:
                        subs = sub_element.findall("string")
                        if subs == []: raise CMLException("Atom has no information")                
                        for sub in subs:
                            self.atoms[sub_element.attrib['id']] = sub.text
            
                # print "Atoms in molecule ", self.atoms
                
                elements = self.tree.findall("bondArray")
                if elements == []: raise CMLException("No bondArray in the molecule")
                for element in elements:
                    sub_elements = element.findall("bond")
                    if sub_elements == []: raise CMLException("No bonds in the bondArray")                            
                    for sub_element in sub_elements:
                        self.bonds[sub_element.attrib['id']] = ()
                        subs = sub_element.findall("string")
                        if subs == []: raise CMLException("Bond has no information")
                        for sub in subs:
                            self.bonds[sub_element.attrib['id']] += (sub.text,)
                
                # print "Bonds in molecule ", self.bonds       
  
            except CMLException as e:
                print "Aborting:", e
            
            # print "Molecule ", self.molecules    

        finally:
            self.CML.close()      


def insert_attribs(tag, attributes, values): 
    """Takes a desired tag, attribute to add and the value of that attribute.
    Returns a tuple of form ("<tag attribute=value ...>", r"<\tag>").  
    Attribute and value are both lists (of equal length) that will be
    placed in the provided order.
    """
    
    try:
        if len(attributes) != len(values):
            print ("The number of attributes %d does not equal the number of values %d"
                    % len(attributes), len(values))
            raise CMLException("Attributes and Values do not match")
            
        while tag not in tags:
            tag_in = False
            print ("Tag %s is not in the list of expected tags " % tag, tags)
            print "Would you like to use a different tag?"
            while True:
                yes = raw_input("Please indicate yes/no ")
                if yes == "yes":
                    print "Okay, lets pick a different tag"
                    tag = raw_input("Please enter the tag you would like to use: ")
                    break
                else:
                    print "Okay, we'll use that tag"
                    tag_in = True
                    break
                    
        end_tag = "".join(["</", tag, ">"])
        start_tag = ''.join(["<", tag])
        for attribute, value in zip(attributes, values):
            if "=" not in attribute:
                attribute += "="
            while attribute == "builtin=" and value not in builtin:
                print "Value %s is not in the expected values for builtin: " % value, builtin
                go = raw_input("Would you like to use that value anyway (yes/no)? ")
                if go == yes:
                    break
                else:
                    value = raw_input("Please enter the value you would like to use instead")
            
            start_tag = ''.join([start_tag, " %s\"%s\"" % (attribute, value)])
            if attribute != attributes[-1]:
                "".join([start_tag, " "])
        start_tag += ">"
        return start_tag, end_tag
        
    except CMLException as e:
        print e
        return
        
        
def insert_text(): pass
                                                               
class CMLBuilder(object):  
    """A CML constructor object"""
    
    def __init__(self, molecule, filename):
        """Takes a molecule dictionary (same format as would be produced by
        cml.CMLParser().molecule and a filename to write the molecule to
        """        
        
        self.molecule = molecule
        self.filename = filename
        
        if os.path.exists(filename):
            print "Path %s exists - continue?" % filename
            while True:
                go = raw_input("Please enter one of the following: Yes, yes, Y or y if you would like to continue")
                if go in ["Yes", "yes", "Y", "y"]: break
                else: return
        
        with open(filename, "w") as f: 
            base = self.molecule.keys()[0]            