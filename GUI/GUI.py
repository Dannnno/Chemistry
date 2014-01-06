from Tkinter import *
import numpy as np

"""TODO in this program
- Create the main window - Done, sort of
    - This should include several buttons - Buttons created, no function
        - add an element
            - change element by right clicking element
        - add a bond, and then change bond type
            - change bond type by right clicking on bond
        - add lone pair electrons
        - add radicals
        - add charge
- Learn how to detect mouse clicks
    - The goal is to select the proper situation through the above buttons
      and then click in the GUI screen to place them.  The objects need
      to be clickable as well, and right click support would be nice
- it should open with a preset compound - Carbon with nothing on it
  this should then be editable
- make a menu!
- have a mode "Organic" that just lets you draw the bonds for a skeletal 
  structure and then add other elements
 """

class gElement:
    def __init__(self,master,x,y,atom):

        self.xcoord = x
        self.ycoord = y
        self.species = atom
        master.pack()


class gCompound:
    def __init__(self,master):
        """Creates a compound, initializes with a Carbon at the middle of the field"""
        self.master = master
        self.comp = np.zeroes(master.width()*master.height()).reshape((height, width))
        
        center = [master.width()/2,master.height()/2]
        self.comp[center[0],center[1]] = gElement(master,center[0],center[1],periodicTable.getElement(12))
        master.pack()
        self.totQ = 0

    def addElement(self,xloc,yloc,species):
        """adds a gElement object of a specified species at position (xloc,yloc)"""
        newElement = gElement(masterxloc,yloc,species)
        newElement.pack()
    def addBond(self,start,end):
        """adds a single bond that connects two gElement objects (start,end)"""
    def addLocalCharge(self,element,q):
        """adds a charge q to a gElement object element"""
    def addTotalCharge(self,q):
        """adds a total charge q to the molecule. Will return an error upon test if this charge is not
        possible for the given molecule"""
    def addRadical(self,element):
        """adds a radical to a gElement object element"""
    def addLonePair(self,element):
        """adds a lone pair to a gElement object element"""
    def editElement(self,oldSpecies,newSpecies):
        """edits a gElement object oldSpecies and rewrites the self.species value as newSpecies"""
    def editBond(self,bondID,newID):
        """edits a bond bondID between two elements and redefines it as a bond newID"""
    def editLocalCharge(self,loc,newQ):
        """Sets a new charge newQ at gElement object loc"""
    def editTotalCharge(self,newQ):
        """sets the total compound charge to newQ. Will return an error as with addTotalCharge()"""
    def removeLonePair(self,loc):
        """removes a lone pair at gElement object loc"""
    def removeRadical(self,loc):
        """removes a radical at gElement object loc"""
    def removeElement(self,loc):
        """removes gElement object loc"""
    def removeBond(self,loc):
        """removes bond loc"""
    def removeLocalCharge(self,loc):
        """removes a local charge loc"""
    def removeTotalCharge(self):
        """sets self.totQ to 0"""
   
class gBond:
    def __init__(self):
        print "Not Done"
    def create():

class gRad:
    def __init__(self):
        print "Not Done"
    def create():

class gCharge:
    def __init__(self):
        print "Not Done"
    def create():
    
class gLPE:
    def __init__(self):
        print "Not Done"
    def create():

def selButton(n):
    global whichbutton
    whichbutton = n
    #setconfig()

whichbutton = 0

#The dictionary of all the objects in the canvas
#Rethink if this is the best way to handle things
aDict={}
bDict={}
lpDict={}
qDict={}
rDict={}

#Initializing the main window
root = Tk()
maxW = root.winfo_screenwidth()
maxH = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(maxW,maxH))

#Creating the button area
buttonFrame = Frame(root,width=maxW,height=200)
buttonFrame.pack(side=TOP,fill=BOTH)

eButton = Button(buttonFrame,text="Element",command=selButton(1))
eButton.pack(side=LEFT,fill=Y)
bButton = Button(buttonFrame,text="Bond",command=selButton(2))
bButton.pack(side=LEFT,fill=Y)
lpButton = Button(buttonFrame,text="Lone Pair",command=selButton(3))
lpButton.pack(side=LEFT,fill=Y)
qButton = Button(buttonFrame,text="Charge",command=selButton(4))
qButton.pack(side=LEFT,fill=Y)
rButton = Button(buttonFrame,text="Radical",command=selButton(5))
rButton.pack(side=LEFT,fill=Y)
testButton = Button(buttonFrame,text="Test Molecule")
testButton.pack(side=LEFT,fill=Y)
publishButton = Button(buttonFrame,text="Publish Molecule")
publishButton.pack(side=LEFT,fill=Y)

#Creating the workspace area
workFrame = Frame(root, width=maxW-400, height=maxH-200)
workFrame.pack(side=BOTTOM,fill=BOTH)

workspace = Canvas(workFrame)
workFrame.pack(fill=BOTH,expand=True)

clickevent = root.bind('<1>', leftclick)

def near(location):
    """Takes a click location and checks for the nearest object, then checks if it is
    within an acceptable tolerance (how many pixels away it is).  Returns an array of
    form [Boolean, Object]"""
    print "Not Done"

def leftclick(event):
    """Handles left clicks while a button is active"""
    coord = [event.x,event.y]

root.mainloop()