class ValenceException(Exception):
    def __init__(self,element):
        self.code = "Too many bonds for " + repr(element)
    def __str__(self):
        return repr(self.code)
        
class BondOrderException(Exception):
    def __init__(self,start,end,order):
        self.code = "Bond between " + repr(start) + " and " + repr(end) + " of order " + repr(order) + " is not a valid bond"       
    def __str__(self):
        return repr(self.code)