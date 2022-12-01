import math, random

class SudokuGenerator:
  
  def __init__(self, row_length, removed_cells):
    self.row_length = row_length
    self.removed_cells = removed_cells
    self.board = [[0 for j in range(self.row_length)] for i in range(self.row_length)]
    self.box_length = int(math.sqrt(self.row_length))
  
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

    # if num in self.board[col] == True:
    #   return False
    # elif num in self.board[col] == False:
    #   return True
    # else:
    #   print("Error")
    
  def valid_in_box(self, row_start, col_start, num):
    not_in_box = True

    if row_start < 3 and row_start >= 0:
      for row in range(0,3):
        if col_start < 3 and col_start >= 0:
          for col in range(0,3):
            if col == num:
              not_in_box = False
        elif col_start < 6:
          for col in range(3,6):
            if col == num:
              not_in_box = False
        elif col_start < 9:
          for col in range(6,9):
            if col == num:
              not_in_box = False
        else:
          print("Error")
    elif row_start < 6:
      for row in range(3,6):
        if col_start < 3 and col_start >= 0:
          for col in range(0,3):
            if col == num:
              not_in_box = False
        elif col_start < 6:
          for col in range(3,6):
            if col == num:
              not_in_box = False
        elif col_start < 9:
          for col in range(6,9):
            if col == num:
              not_in_box = False
        else:
          print("Error")
    elif row_start < 9:
      for row in range(6,9):
        if col_start < 3 and col_start >= 0:
          for col in range(0,3):
            if col == num:
              not_in_box = False
        elif col_start < 6:
          for col in range(3,6):
            if col == num:
              not_in_box = False
        elif col_start < 9:
          for col in range(6,9):
            if col == num:
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

    if not_in_row == True:
      return True 
    if not_in_col == True:
      return True
    if not_in_box == True:
      return True
    else:
      return False
    
  def fill_box(self, row_start, col_start):

    # if row_start < 3 and row_start >= 0:
    #   for row in range(0,3):
    #     if col_start < 3 and col_start >= 0:
    #       for col in range(0,3):
    #         if col == None:
    #           pass
    #           self.board[row][col]
    #         else:
    #           pass
    #     elif col_start < 6:
    #       for col in range(3,6):
    #         if col == num:
    #           not_in_box = False
    #     elif col_start < 9:
    #       for col in range(6,9):
    #         if col == num:
    #           not_in_box = False
    #     else:
    #       print("Error")
    # elif row_start < 6:
    #   for row in range(3,6):
    #     if col_start < 3 and col_start >= 0:
    #       for col in range(0,3):
    #         if col == num:
    #           not_in_box = False
    #     elif col_start < 6:
    #       for col in range(3,6):
    #         if col == num:
    #           not_in_box = False
    #     elif col_start < 9:
    #       for col in range(6,9):
    #         if col == num:
    #           not_in_box = False
    #     else:
    #       print("Error")
    # elif row_start < 9:
    #   for row in range(6,9):
    #     if col_start < 3 and col_start >= 0:
    #       for col in range(0,3):
    #         if col == num:
    #           not_in_box = False
    #     elif col_start < 6:
    #       for col in range(3,6):
    #         if col == num:
    #           not_in_box = False
    #     elif col_start < 9:
    #       for col in range(6,9):
    #         if col == num:
    #           not_in_box = False
    #     else:
    #       print("Error")  

    # if row_start < 3 and row_start >= 0:
    #   start_row = 0
    # elif row_start < 6:
    #   start_row = 3
    # elif row_start < 9:
    #   start_row = 6
    # else:
    #   print("Error")

    # if col_start < 3 and col_start >= 0:
    #   start_col = 0
    # elif col_start < 6:
    #   start_col = 3
    # elif col_start < 9:
    #   start_col = 6
    # else:
    #   print("Error")

    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for row in range(3):
      for col in range(3):
        random.shuffle(nums)
        num = nums.pop(0)
        


        self.board[row_start+row][col_start+col] = num



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


    # list_positions = [[0,0],[0,1]]
    # random.shuffle(list_positions)
    # for i in range(0,30):
    #   position = list_positions.pop(0)
      














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
