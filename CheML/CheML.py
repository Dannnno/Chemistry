"""This module is used to parse CML (Chemical Markup Language) an
extension of XML.  The XML library is extended to work with the
tags and structure of the CML language.  
"""

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
    
    def __init__(self, err_message="Problem with the CML file"):
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
        self.id = ""
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
                try:
                    self.id = self.tree.getroot().attrib['id']
                except Exception:
                    raise CMLException("Couldn't find a molecule root object")
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
                
            except CMLException as e:
                print "Aborting:", e

        finally:
            self.CML.close()      


def insert_attribs(tag, attributes, values): 
    """Takes a desired tag, attribute(s) to add and the value(s) of that/those 
    attribute(s). Returns a tuple of form ("<tag attribute=value ...>", "</tag>").  
    Attributes and values are both lists (of equal length) that will be
    added in the given order
    """
    
    try:
        if len(attributes) != len(values):
            print ("The number of attributes %d does not equal the number of values %d"
                    % len(attributes), len(values))
            raise CMLException("Attributes and Values do not match")
            
        end_tag = "".join(["</", tag, ">"])
        start_tag = ''.join(["<", tag])
        for attribute, value in zip(attributes, values):
            if "=" not in attribute:
                attribute += "="
            start_tag = ''.join([start_tag, " %s\"%s\"" % (attribute, value)])
            if attribute != attributes[-1]:
                "".join([start_tag, " "])
                
        start_tag += ">"
        return start_tag, end_tag
        
    except CMLException as e:
        print e
        return
                                                               
class CMLBuilder(object):  
    """A CML constructor object"""
    
    def __init__(self, molecule, filename):
        """Takes a molecule dictionary (same format as would be produced by
        cml.CMLParser().molecule and a filename to write the molecule to
        """        
        
        self.molecule = molecule
        self.filename = filename
        self.depth = 0
        self.indent = "    "
        
        with open(filename, "w") as f: 
            mol_id = self.molecule.keys()[0]   
            opener, closer = insert_attribs("molecule", 
                                            ["id="], 
                                            [mol_id])
            f.write(opener + "\n")
            
            bonds = self.molecule[mol_id]["bonds"]
            bkeys = sorted(bonds.keys())
            atoms = self.molecule[mol_id]["atoms"]
            akeys = sorted(atoms.keys())            
            aaopen, aaclose = insert_attribs("atomArray", [], [])
            bbopen, bbclose = insert_attribs("bondArray", [], [])
            f.write(self.indent + aaopen + "\n")
            
            for key in akeys:
                atopen, atclose = insert_attribs("atom", 
                                                 ["id"], 
                                                 [key])
                stropen, strclose = insert_attribs("string", 
                                                   ["builtin"], 
                                                   ["elementType"])
                f.write(self.indent*2 + atopen + "\n" 
                      + self.indent*3 + stropen + atoms[key] + strclose + "\n" 
                      + self.indent*2 + atclose + "\n")
                      
            f.write(self.indent + aaclose + "\n" 
                  + self.indent + bbopen + "\n")
            
            for key in bkeys:
                bopen, bclose = insert_attribs("bond", 
                                               ["id"], 
                                               [key])
                stropen1, strclose1 = insert_attribs("string", 
                                                     ["builtin"], 
                                                     ["atomRef"])
                stropen2, strclose2 = insert_attribs("string", 
                                                     ["builtin"], 
                                                     ["atomRef"])
                stropen3, strclose3 = insert_attribs("string", 
                                                     ["builtin"], 
                                                     ["order"])
                f.write(self.indent*2 + bopen + "\n" 
                      + self.indent*3 + stropen1 + bonds[key][0] + strclose1 + "\n"
                      + self.indent*3 + stropen2 + bonds[key][1] + strclose2 + "\n"
                      + self.indent*3 + stropen3 + bonds[key][2] + strclose3 + "\n"
                      + self.indent*2 + bclose + "\n")

            f.write(self.indent + bbclose + "\n"
                  + closer)