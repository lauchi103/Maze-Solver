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
        seed = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

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

    def _break_wall_r(self,i,j):
        self._cells[i][j].visited = True
        running = True
        while running:
            next_index_list = []
            #list with adjacent cells
             # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
            #if no directions possible, return and draw current cell
            if len(next_index_list) == 0:
                self._draw_cell(i,j)
                return
            #pick random direction
            direction = random.randrange(len(next_index_list))
            next_index = next_index_list[direction]
            
            #knock down wall between the cells
            x_diff = next_index[0] - i
            y_diff = next_index[1] -j
            
            match (x_diff,y_diff):
                case (0,-1):
                    self._cells[i][j].has_top_wall = False
                    self._cells[i+x_diff][j+y_diff].has_bottom_wall = False
                case (0,1):
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i+x_diff][j+y_diff].has_top_wall = False
                case (-1,0):
                    self._cells[i][j].has_left_wall = False
                    self._cells[i+x_diff][j+y_diff].has_right_wall = False
                case (1,0):
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+x_diff][j+y_diff].has_left_wall = False
                case _:
                    raise Exception("Error with _break_wall_r, x_diff und y_diff unerwartet")
            self._draw_cell(i,j)
            self._draw_cell(i+x_diff,j+y_diff)
            #move to next cell
            self._break_wall_r(i+x_diff,j+y_diff)
            
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False

    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self,i,j):
        self._cells[i][j].visited = True
        if i == self._num_cols-1 and j == self._num_rows-1:
            return True
        
        if self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False and i>0:
            self._cells[i][j].draw_move(self._cells[i][j-1],True)
            self._animate()
            if self._solve_r(i,j-1):
                self._cells[i][j].draw_move(self._cells[i][j-1])
                self._animate()
                return True
        if self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
            self._cells[i][j].draw_move(self._cells[i][j+1],True)
            self._animate()
            if self._solve_r(i,j+1):
                self._cells[i][j].draw_move(self._cells[i][j+1])
                self._animate()
                return True
        if self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i-1][j],True)
            self._animate()
            if self._solve_r(i-1,j):
                self._cells[i][j].draw_move(self._cells[i-1][j])
                self._animate()
                return True
        if self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
            self._cells[i][j].draw_move(self._cells[i+1][j],True)
            self._animate()
            if self._solve_r(i+1,j):
                self._cells[i][j].draw_move(self._cells[i+1][j])
                self._animate()
                return True
            
        return False
            
