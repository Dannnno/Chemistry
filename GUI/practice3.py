import Tkinter as tk

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        canvas = tk.Canvas(self, width=800, height=500)
        canvas.pack(side="top", fill="both", expand=True)
        canvas_id = canvas.create_text(10,10, anchor="nw")

        canvas.itemconfig(canvas_id, text="this is the text")
        canvas.insert(canvas_id, 12, "new ")
        
def callback(event):
    return [event.x,event.y]

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()