from cell import Cell
import random
import time


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _get_adjacent_cells(self,i,j):
        adj = []
        if j-1 < self._num_rows and j-1 >= 0:
            adj.append([i,j-1])
        if i-1 < self._num_cols and i-1 >= 0:
            adj.append([i+1,j])
        if i+1 < self._num_cols and i+1 >= 0:
            adj.append([i+1,j])
        if j+1 < self._num_rows and j+1 >= 0:
            adj.append([i,j+1])  
        return adj  

    def _break_wall_r(self,i,j,seed = None):
        random.seed(seed)
        self._cells[i][j].visited = True
        running = True
        while running:
            #list with adjacent cells
            to_visit = self._get_adjacent_cells(i,j)
            #list with not visited cells
            for cell in to_visit:
                if self._cell[cell[0]][cell[1]].visited == True:
                    to_visit.remove(cell)
            #if no directions possible, return and draw current cell
            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            #pick random direction
            direction = random.randint(0,len(to_visit)-1)
            travel_cell = to_visit[direction]
            #knock down wall between the cells


            
            
