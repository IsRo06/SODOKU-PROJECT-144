import pygame
from constants import *
from cell import Cell

class Board:
    def __init__(self, rows, cols, width, height, screen):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.screen = screen
        self.board = self.initialize_board()
        self.cells = [[Cell(self.board[i][j], i, j, self.height//self.rows,
                            self.width//self.cols) for j in range(cols)] for i in range(rows)]

    def initialize_board(self):
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                row.append(0)
            board.append(row)
        return board

    def print_board(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                print(self.board[i][j], end=" ")
            print()


    def mark_square(self, row, col, number):
        self.board[row][col] = number
        self.update_cells()

    def update_cells(self):
        self.cells = [[Cell(self.board[i][j], i, j, self.height//self.rows,
                            self.width//self.cols) for j in range(self.cols)] for i in range(self.rows)]

    def available_square(self, row, col):
        return self.board[row][col] == 0

    def check_if_winner(self, chip_type):
        for i in range(self.rows):
            if self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2] and self.board[i][2] == chip_type:
                return True

        for j in range(self.cols):
            if self.board[0][j] == self.board[1][j] and self.board[1][j] == self.board[2][j] and self.board[2][j] == chip_type:
                return True

        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] == chip_type:
            return True

        if self.board[2][0] == self.board[1][1] == self.board[0][2] == chip_type:
            return True

        return False

    def board_is_full(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == 0:
                    return False
        return True

    def reset_board(self):
        self.board = self.initialize_board()
        self.update_cells()
