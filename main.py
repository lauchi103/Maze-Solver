from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self,height,width) -> None:
        self.root = Tk()
        self.root.geometry(f"{width}x{height}")
        self.root.title = "Hallooo"
        self.canv = Canvas()
        self.canv.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    def close(self):
        self.running = False

win = Window(500,300)
win.wait_for_close()