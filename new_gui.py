import sys

import pygame

from button import *
from cell import *
from sudoku_generator import *


def generate_py_board(cell_number):
    pass

def pre_fill_board(cell_number, board_to_use):
    SCREEN.fill("White")
    board = SudokuGenerator(9, cell_number)
    board.draw()


    # Credit to https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/ for code inspo
    for i in range (9):
        for j in range(9):
            if board_to_use[i][j] !=0:

                #populates board
                pygame_board = ACTUAL_FONT.render(str(board_to_use[i][j]), 1, (0,0,0))
                SCREEN.blit (pygame_board, (i* SQUARE_SIZE+15, j* SQUARE_SIZE +15))


def if_winner(board, answer_board):
    if board == answer_board:
        return True
    else:
        return False

def sudoku(cell_number):  # second main function
    #refills screen
    SCREEN.fill("white")
    #initialized board
    psudo_board = SudokuGenerator(9, cell_number)
    psudo_board.fill_values()
    answer_board = copy.deepcopy(psudo_board.get_board())
    psudo_board.remove_cells()
    usable_board= psudo_board.get_board()
    empty_board = copy.deepcopy(psudo_board.get_board())


    #fills board
    pre_fill_board(cell_number, usable_board)
    number = "0"

    while True:
        # initializes buttons
        reset_button = Button(image=None, pos=(WIDTH // 3 - 75, HEIGHT - 60), text="Reset", font=get_font(50),
                              color="black")
        refresh_button = Button(image=None, pos=(WIDTH // 3 + 100, HEIGHT - 60), text="Refresh", font=get_font(50),
                                color="black")
        exit_button = Button(image=None, pos=(WIDTH // 3 + 300, HEIGHT - 60), text="Exit", font=get_font(50),
                             color="black")

        # display each button
        for i in [reset_button, refresh_button, exit_button]:
            i.update(SCREEN)

        #gets the position of the mouse
        MOUSE_POS_GAME = pygame.mouse.get_pos()

    # pygame mechanism for display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #checks for what position was clicked
                clicked_col = int(MOUSE_POS_GAME[0]/SQUARE_SIZE)
                clicked_row = int(MOUSE_POS_GAME[1]/SQUARE_SIZE)
                print(f"Position pressed{clicked_col,clicked_row}")

                if clicked_row <= 8:
                    print(f"INSIDE")
                    if empty_board[clicked_col][clicked_row] == 0:
                        print(f"EMPTYYYYY")
                        psudo_board.mark_square(clicked_col, clicked_row, 0)
                        usable_board = psudo_board.get_board()
                        pre_fill_board(cell_number, usable_board)

                #reset button
                if reset_button.checkInput(MOUSE_POS_GAME):
                    main_menu()
                    break
                if refresh_button.checkInput(MOUSE_POS_GAME):
                    for i in range(9):
                        for j in range(9):
                            if empty_board[i][j] == 0 and usable_board[i][j] != empty_board[i][j]:
                                psudo_board.mark_square(i, j, 0)
                                usable_board = psudo_board.get_board()
                                pre_fill_board(cell_number, usable_board)

                    pre_fill_board(cell_number, usable_board)

                if exit_button.checkInput(MOUSE_POS_GAME):
                    pygame.quit()
                    sys.exit()
            #answers for each key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    number = 1
                if event.key == pygame.K_2:
                    number = 2
                if event.key == pygame.K_3:
                    number = 3
                if event.key == pygame.K_4:
                    number = 4
                if event.key == pygame.K_5:
                    number = 5
                if event.key == pygame.K_6:
                    number = 6
                if event.key == pygame.K_7:
                    number = 7
                if event.key == pygame.K_8:
                    number = 8
                if event.key == pygame.K_9:
                    number = 9
                else:
                    print(f"Error")

                # check if space is empty and use user input in board
                if psudo_board.available_square(clicked_col, clicked_row):
                    psudo_board.mark_square(clicked_col,clicked_row, number)
                    usable_board_2 = psudo_board.get_board()
                    pre_fill_board(cell_number, usable_board_2)


        pygame.display.update()

def get_font(size): #credits to baraltech on youtube for code inspo
    return pygame.font.Font("font.ttf", size)

def main_menu(): #initial screen

    while True:
        SCREEN.fill("white")
        SCREEN.blit(BACKGROUND, (0,0))
        #set the color of background and get the position of the mouse
        MOUSE_POS = pygame.mouse.get_pos()

        #main menu initialization
        title_font = pygame.font.Font("font.ttf", 150)

        menu_text = title_font.render("Sudoku",0, "White")
        menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT//3 -100))
        SCREEN.blit(menu_text, menu_rect)


        #initialize buttons CREDIT to TA logan for dimensions
        easy_button = Button(image= BUTTON_BACKGROUND ,pos=(WIDTH // 2, HEIGHT//3 +50),text = "Easy", font=get_font(75), color="White" )
        medium_button = Button(BUTTON_BACKGROUND, (WIDTH // 2, HEIGHT//3 +200), "Medium", get_font(75), "White")
        hard_button = Button(BUTTON_BACKGROUND, (WIDTH // 2, HEIGHT//3 +350), "Hard", get_font(75), "White")


        #display each button
        for i in [easy_button, medium_button, hard_button]:
            i.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.checkInput(MOUSE_POS):
                    sudoku(30)
                if medium_button.checkInput(MOUSE_POS):
                    sudoku(40)
                if hard_button.checkInput(MOUSE_POS):
                    sudoku(50)
        pygame.display.update()


if __name__ == '__main__':
    # initialization of variables
    pygame.init()
    pygame.display.set_caption("Sudoku Group 12^2")
    cells = 0
    ACTUAL_FONT = pygame.font.Font(None, 60)
    start = main_menu()


