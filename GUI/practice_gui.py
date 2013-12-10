from Tkinter import *

class App:

    ##constructor called with parent widgit, master
    def __init__(self, master):

        #Frame instance created as frame, call pack to make visible
        frame = Frame(master)
        frame.pack()

        #Creating two buttons
        
        #Creates the quit button, makes it red, commands it to quit, puts it on the left
        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=LEFT)

        #Creates the hi button, 
        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    #initializes the function called say_hi
    def say_hi(self):
        print("hi there, everyone!")

#initializes a root object (ie the window)
root = Tk()

#one instance of the App class with root as the parent
app = App(root)

#Starts the application loop
root.mainloop()

#Optional - depends on environment. When necessary is always necessary
#root.destroy()