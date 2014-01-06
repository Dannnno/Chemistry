from Tkinter import *

whichbutton = 0

def selButton(n):
    global whichbutton
    whichbutton = n
    setconfig()
    

buttonFrame = Frame(master,width=master.winfo_screenwidth(),height=200)
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
    
def setconfig():
    global eButton, bButton, lpButton, qButton, rButton
    eButton.config(relief=RAISED)
    bButton.config(relief=RAISED)
    lpButton.config(relief=RAISED)
    qButton.config(relief=RAISED)
    rButton.config(relief=RAISED)  
    whichbutton == 1:
        eButton.config(relief=SUNKEN)
    whichbutton == 2:
        bButton.config(relief=SUNKEN)
    whichbutton == 3:
        lpButton.config(relief=SUNKEN)
    whichbutton == 4:
        qButton.config(relief=SUNKEN)
    whichbutton == 5:
        rButton.config(relief=SUNKEN)
                                                
class feedback:
    
    def __init__(self, master):
         print "Not Done"
   
class eworkspace:
    
    def __init__(self, master):
        self.space = Canvas(master,width=master.winfo_screenwidth(),height=master.winfo_screenheight()-400)
        self.space.pack(side=BOTTOM,fill="both",expand=True)
        
    def binding(self,event,handler):
        self.space.bind(event,handler)

aDict={}
bDict={}
lpDict={}
qDict={}
rDict={}

root = Tk()
maxW = root.winfo_screenwidth()
maxH = root.winfo_screenheight()
root.geometry("{0}x{1}+0+0".format(maxW,maxH))

eButtons = ebuttons(root)
eWorkspace = eworkspace(root)

def near(location):
    print "Not Done"


def leftclick(event):
    coord = [event.x,event.y]
                                        
clickevent = eWorkspace.binding('<1>', leftclick)

root.mainloop()