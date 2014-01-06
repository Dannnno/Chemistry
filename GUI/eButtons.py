from Tkinter import *

class buttons:
    
    def __init__(self, master):
        
        buttonFrame = Frame(master, width=master.winfo_screenwidth(), height=master.winfo_screenheight()-200)
        buttonFrame.pack(side=TOP)
        
        eButton = Button(buttonFrame,text="Element",command=element)
        eButton.pack(side=LEFT)

        bButton = Button(buttonFrame,text="Bond",command=bond)
        bButton.pack(side=LEFT)

        lpButton = Button(buttonFrame,text="Lone Pair",command=lpe)
        lpButton.pack(side=LEFT)

        qButton = Button(buttonFrame,text="Charge",command=charge)
        qButton.pack(side=LEFT)

        rButton = Button(buttonFrame,text="Radical",command=radical)
        rButton.pack(side=LEFT)
        
    def element():
        print "Element"
        
    def bond():
        print "Bond"
    
    def lpe():
        print "Lone Pair Electron"

    def charge():
        print "Charge"

    def radical():
        print "Radical"  
    
    def leftclick(event):
        