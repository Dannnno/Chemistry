class ValenceException(Exception):
    def __init__(self,element):
        self.code = "Too many bonds for " + repr(element)
    def __str__(self):
        return repr(self.code)