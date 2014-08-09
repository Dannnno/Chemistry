# Don't use this - its unnecessarily bulky.  Will look into optimizing the 
# current parser I'm using (xml.etree.cElementTree) by using .iterparse()

import xml.sax

class CMLHandler(xml.sax.ContentHandler):
    def __init__(self, **kwargs):
        #super(self, CMLHandler).__init__(**kwargs)
        self.id = ""
        self.formula = ""
        self.inIdentifier = False
        self.inchi = "InChI/1="
        self.inBasic = False
        self.inInChI = False
        self.name = ""
        self.inName = False
        self.weight = ""
        self.inWeight = False
        self.mpt = ""
        self.mptSet = False
        self.inMpt = False
        self.bpt = ""
        self.inBpt = False
        self.bptSet = False
        self.atoms = {}
        self.bonds = {}
        
    def startElement(self, name, attributes):
        print "startElement '" + name + "'"
        
        if name == "molecule":
            self.id = attributes["id"]
            
        if name == "atom":
            self.atoms[attributes["id"]] = "atom"
        
        if name == "bond":
            self.bonds[attributes["id"]] = "bond"
            
        if name == "formula":
            self.formula = attributes["concise"]
            
        if name == "identifier":
            self.inIdentifier = True
            if attributes.has_key("version") and attributes["version"] == "InChI/1":
                self.inInChI = True
            
        if name == "basic":
            self.inBasic = True
                
        if name == "name":
            self.inName = True
                
        if  name == "scalar":
            if attributes["dictRef"] == "cml.molwt":
                self.inWeight = True
            elif attributes["dictRef"] == "cml:mpt":
                self.inMpt = True
            elif attributes["dictRef"] == "cml:bpt":
                self.inBpt = True
                    
    def characters(self, data):
        if data.strip():
            print "characters '" + data + "'"
        
        if self.inName:
            self.name += data
            
        if self.inWeight:
                self.weight += data
        
        if self.inMpt:
                self.mpt += data
                
        if self.inBpt:
            self.bpt += data
                
        if self.inBasic and self.inInChI:
            self.inchi += data
                
    def endElement(self, name):
        print "endElement '" + name + "'"
        
        if name == "identifier":
            self.inIdentifier = False
            
        if name == "basic":
            self.inBasic = False
            if self.inInChI:
                self.inInChI = False
        
        if name == "name":
            self.inName = False
            
        if name == "inchi":
            self.inInChI = False
            
        if name == "scalar":
            if self.inWeight:
                self.inWeight = False
            elif self.inMpt:
                self.inMpt = False
                self.mptSet = True
            elif self.inBpt:
                self.inBpt = False
                self.bptSet = True