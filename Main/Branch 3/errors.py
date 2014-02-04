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
        
class InvalidStereoException(Exception):
    
    def __init__(self,funcGroup):
        """
        
        Raises an Exception for invalid stereochemistry. 
        Takes a list funcGroup = [self.__class__.__name__,**kwargs]
        Checks for different inputs based on funcGroup[0] and then raises
        a custom error message
        
        """
        
        self.funcGroup = funcGroup
        if self.funcGroup[0] == 'Alcohol':
            self.stereo = self.funcGroup[1] # The stereochemistry passed to it
            self.code = "Alcohol can not have stereochemistry " + self.stereo
            
    def __str__(self):
        return repr(self.code)
        
class InvalidLocationException(Exception):
    
    def __init__(self,funcGroup):
        """
        
        Raises an Exception for invalid placement on a Carbon.  Takes a list 
        funcGroup = [self.__class__.__name__,**kwargs]
        Checks for different inputs based on funcGroup[0] and then raises
        a custom error message
        
        """
        
        self.funcGroup = funcGroup
        if self.funcGroup[0] == 'Alcohol':
            self.loc = self.funcGroup[1]
            self.code = "Alcohol can not be at location " + self.loc
            
    def __str__(self):
        return repr(self.code)