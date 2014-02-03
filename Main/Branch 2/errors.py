class ValenceException(Exception):
    def __init__(self,element):
        self.code = "Too many bonds for " + repr(element)
    def __str__(self):
        return repr(self.code)
        
class InvalidBondException(Exception):
    def __init__(self,aBond):
        self.code = "Not a valid bond order"
    def __str__(self):
        return repr(self.code)