from Tkinter import *

"""TODO in this program
- Create the main window - Done, sort of
    - This should include several buttons - Buttons created, no function
        - add an element
            - change element by clicking element
        - add a bond, and then change bond type
            - change bond type by clicking on bond
        - add lone pair electrons
        - add radicals
        - add charge
- Learn how to detect mouse clicks
    - The goal is to select the proper situation through the above buttons
      and then click in the GUI screen to place them.  The objects need
      to be clickable as well, and right click support would be nice
 """
 
root = Tk()
maxW = root.winfo_screenwidth()
maxH = root.winfo_screenheight()

canvas = Canvas(root,width=maxW,height=maxH-200)
canvas.pack(side="bottom", fill="both",expand=True)

def callback(event):
    coord = [event.x,event.y]
    print coord
    return coord
    
root.bind("<Button-1>", callback)
    
def element():
    point = callback(event)
    x = int(point[0])
    y = int(point[1])
    canvas_id = canvas.create_text(x,y, anchor="nw")
    canvas.itemconfig(canvas_id, text="C")
    canvas.insert(canvas_id,12,"new ")
    print "Element"

def bond():
    print "Bond"
    
def lpe():
    print "Lone Pair Electron"

def charge():
    print "Charge"

def radical():
    print "Radical"

buttonFrame = Frame(root, width=maxW, height=200)
buttonFrame.pack(side=TOP)

button = Button(buttonFrame, 
                text="Element",
                command=element)
button.pack()
button = Button(buttonFrame,
                text="Bond",
                command=bond)
button.pack()
button = Button(buttonFrame,
                text="Lone Pair",
                command=lpe)
button.pack()
button = Button(buttonFrame,
                text="Charge",
                command=charge)
button.pack()
button = Button(buttonFrame,
                text="Radical",
                command=radical)
button.pack()

root.geometry("{0}x{1}+0+0".format(maxW,maxH))
     
root.mainloop()
    