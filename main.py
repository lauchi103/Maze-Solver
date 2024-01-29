from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self,height,width) -> None:
        self._root = Tk()
        self._root.geometry(f"{width}x{height}")
        self._root.title = "Hallooo"
        self.canv = Canvas()
        self.canv.pack()
        self._running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()
    def wait_for_close(self):
        self._running = True
        while self._running:
            self.redraw()
    def close(self):
        self._running = False
    def draw_line(self,line,fill_color):
        line.draw(self.canv,fill_color)
        

class Point():
    def __init__(self,x=0,y=0) -> None:
        self.x = x
        self.y = y

class Line():
    def __init__(self,x1,y1,x2,y2) -> None:
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
    def draw(self,canv,fill_color):
        canv.create_line(
            self._x1, self._y1, self._x2, self._y2, fill=fill_color, width=2
        )
        canv.pack()

class Cell():
    def __init__(self,x1,y1,x2,y2,win,has_left_Wall = True ,has_right_Wall = True ,has_top_Wall = True ,has_bottom_Wall = True ) -> None:
        self.has_left_wall = has_left_Wall
        self.has_right_wall = has_right_Wall
        self.has_top_wall = has_top_Wall
        self.has_bottom_wall = has_bottom_Wall
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._win = win
    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(Line(self._x1,self._y1,self._x1,self._y2), "black")
        if self.has_right_wall:
            self._win.draw_line(Line(self._x2,self._y1,self._x2,self._y2), "black")
        if self.has_top_wall:
            self._win.draw_line(Line(self._x1,self._y1,self._x2,self._y1), "black")
        if self.has_bottom_wall:
            self._win.draw_line(Line(self._x1,self._y2,self._x2,self._y2), "black")
    def draw_move(self,to_cell,undo = False):
        width = (self._x2-self._x1)//2
        height = (self._y2 - self._y1)//2
        if undo:
            fill_color = "grey"
        else:
            fill_color = "red"

        self._win.draw_line(Line(self._x1+width,self._y1+height,to_cell._x1+width,to_cell._y1+height),fill_color)

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._create_cells()# hier weiter 7. MazeClass



def main():
    win = Window(500,300)
    
    

    win.wait_for_close()

if __name__ == "__main__":
    main()