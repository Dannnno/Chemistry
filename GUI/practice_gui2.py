from Tkinter import *
import random


class BubbleFrame:

    def __init__(self, root):
        root.title("Math Bubbles")
        self.bubbles = {}  # this will hold bubbles ids, positions and velocities
        self.score = 0
        Button(root, text="Start", width=8, command=self.initialize_bubbles).pack()  # This button starts the game, making the bubbles move across the screen
        Button(root, text="Quit", width=8, command=root.quit).pack()
        self.canvas = Canvas(root, width=800, height=650, bg='#afeeee')
        self.canvas.create_text(400, 30, fill="darkblue", font="Times 20 italic bold", text="Click the bubbles that are multiples of two.")
        self.canvas.pack()

    def initialize_bubbles(self):
        for each_no in xrange(1, 21):
            xval = random.randint(5, 765)
            yval = random.randint(5, 615)
            oval_id = self.canvas.create_oval(xval, yval, xval + 30, yval + 30,
                                              fill="#00ffff", outline="#00bfff",
                                              width=5, tags="bubble")
            text_id = self.canvas.create_text(xval + 15, yval + 15, text=each_no, tags="bubble")
            self.canvas.tag_bind("bubble", "<Button-1>", lambda x: self.click(x))
            self.bubbles[oval_id] = (xval, yval, 0, 0, each_no, text_id)  # add bubbles to dictionary

    def click(self, event):
        if self.canvas.find_withtag(CURRENT):
            item_uid = event.widget.find_closest(event.x, event.y)[0]
            is_even = False
            try:  # clicked oval
                self.bubbles[item_uid]
            except KeyError:  # clicked the text
                for key, value in self.bubbles.iteritems():
                    if item_uid == value[5]:  # comparing to text_id
                        if value[4] % 2 == 0:
                            is_even = True
                        self.canvas.delete(key)  # deleting oval
                        self.canvas.delete(item_uid)  # deleting text
            else:
                if self.bubbles[item_uid][4] % 2 == 0:
                    is_even = True
                self.canvas.delete(item_uid)  # deleting oval
                self.canvas.delete(self.bubbles[item_uid][5])  # deleting text
            if is_even:
                self.score += 1
            else:
                self.score -= 1
            print self.score

    def loop(self, root):
        for oval_id, (x, y, dx, dy, each_no, text_id) in self.bubbles.items():
            # update velocities and positions
            dx += random.randint(-1, 1)
            dy += random.randint(-1, 1)
            # dx and dy should not be too large
            dx, dy = max(-5, min(dx, 5)), max(-5, min(dy, 5))
            # bounce off walls
            if not 0 < x < 770:
                dx = -dx
            if not 0 < y < 620:
                dy = -dy
            # apply new velocities
            self.canvas.move(oval_id, dx, dy)
            self.canvas.move(text_id, dx, dy)
            self.bubbles[oval_id] = (x + dx, y + dy, dx, dy, each_no, text_id)
        # have mainloop repeat this after 100 ms
        root.after(100, self.loop, root)

if __name__ == "__main__":
    root = Tk()
    frame = BubbleFrame(root)
    frame.loop(root)
    root.mainloop()