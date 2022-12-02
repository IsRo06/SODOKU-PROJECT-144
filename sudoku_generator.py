import math, random, copy, pygame
from constants import *
from cell import *


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [[0 for j in range(self.row_length)] for i in range(self.row_length)]
        self.board_empty = self.board
        self.box_length = int(math.sqrt(self.row_length))
        self.height = HEIGHT
        self.width = WIDTH
        self.screen = SCREEN
        self.rows = row_length
        self.cols = row_length
        self.cells = [[Cell(self.board[i][j], i, j, self.height // self.rows,
                            self.width // self.cols) for j in range(row_length)] for i in range(row_length)]

    def draw(self):
        # draw lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (0, SQUARE_SIZE * i),
                             (BOARD_WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        # draw vertical lines
        for i in range(1, 9):
            pygame.draw.line(self.screen, LINE_COLOR, (SQUARE_SIZE * i, 0),
                             (SQUARE_SIZE * i, BOARD_HEIGHT), LINE_WIDTH)

        for i in range(self.rows):
            for j in range(self.cols):
                self.cells[i][j].draw(self.screen)

    def update_cells(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.height // self.rows,
                            self.width // self.cols) for j in range(self.cols)] for i in range(self.rows)]
    def mark_square(self, row, col, number):
        self.board[row][col] = number
        self.update_cells()

    def get_board(self):
        return self.board

    def print_board(self):
        the_board = self.get_board()
        for item in the_board:
            for i in item:
                print(i, end=" ")
            print()

    def valid_in_row(self, row, num):
        part = self.board[row]
        for i in part:
            if int(i) == int(num):
                return False
        return True

    def valid_in_col(self, col, num):
        col_values = []

        for row in range(9):
            col_values += [self.board[row][col]]

        for i in col_values:
            if int(i) == int(num):
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        not_in_box = True

        if row_start < 3 and row_start >= 0:
            for row in range(0, 3):
                if col_start < 3 and col_start >= 0:
                    for col in range(0, 3):
                        if self.board[row][col] == num:
                            not_in_box = False
                elif col_start < 6:
                    for col in range(3, 6):
                        if self.board[row][col] == num:
                            not_in_box = False
                elif col_start < 9:
                    for col in range(6, 9):
                        if self.board[row][col] == num:
                            not_in_box = False
                else:
                    print("Error")
        elif row_start < 6:
            for row in range(3, 6):
                if col_start < 3 and col_start >= 0:
                    for col in range(0, 3):
                        if self.board[row][col] == num:
                            not_in_box = False
                elif col_start < 6:
                    for col in range(3, 6):
                        if self.board[row][col] == num:
                            not_in_box = False
                elif col_start < 9:
                    for col in range(6, 9):
                        if self.board[row][col] == num:
                            not_in_box = False
                else:
                    print("Error")
        elif row_start < 9:
            for row in range(6, 9):
                if col_start < 3 and col_start >= 0:
                    for col in range(0, 3):
                        if self.board[row][col] == num:
                            not_in_box = False
                elif col_start < 6:
                    for col in range(3, 6):
                        if self.board[row][col] == num:
                            not_in_box = False
                elif col_start < 9:
                    for col in range(6, 9):
                        if self.board[row][col] == num:
                            not_in_box = False
                else:
                    print("Error")
        else:
            print("Error")

        return not_in_box

    def is_valid(self, row, col, num):
        not_in_row = self.valid_in_row(row, num)
        not_in_col = self.valid_in_col(col, num)
        not_in_box = self.valid_in_box(row, col, num)

        if not_in_row == False:
            return False
        elif not_in_col == False:
            return False
        elif not_in_box == False:
            return False
        else:
            return True

    def fill_box(self, row_start, col_start):

        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for row in range(3):
            for col in range(3):
                random.shuffle(nums)
                num = nums.pop(0)

                self.board[row_start + row][col_start + col] = num

    def fill_diagonal(self):
        self.fill_box(0, 0)
        self.fill_box(3, 3)
        self.fill_box(6, 6)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called
  
  # NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again
      Parameters: None
      Return: None
    '''

    def remove_cells(self):
        row = 0
        count = int(self.removed_cells)
        while count > 0:
            col_list = []
            col = None

            for i in range(9):
                if self.board[row][i] != 0:
                    col_list += [i]

            random.shuffle(col_list)

            if len(col_list) > 0:
                col = col_list[0]
            else:
                print("empty")
            self.board[row][col] = 0

            count -= 1
            row += 1
            if row == 9:
                row = 0

    def reset_board(self):
        self.board = self.board_empty
        self.update_cells()
    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled
  
      Parameters:
      row, col specify the coordinates of the first empty (0) cell
      Return:
      boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining
      Parameters: None
      Return: None
      '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)



'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution
Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)
Return: list[list] (a 2D Python list to represent the board)
'''

def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

def generate_sudo(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = copy.deepcopy(sudoku.get_board())
    sudoku.remove_cells()
    second_board = sudoku.get_board()
    list_of_boards = [board, second_board]
    return list_of_boards


# The bit of code that actually runs everthing else
if __name__ == '__main__':
    x = generate_sudo(9, 30)

    print("Answer Key:")
    for i in x[0]:
        for j in i:
            print(j, end=' ')
        print()
    print("Game Board:")
    for i in x[1]:
        for j in i:
            print(j, end=' ')
        print()
