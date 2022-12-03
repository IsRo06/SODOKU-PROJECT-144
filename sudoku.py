import sys

import pygame

from button import *
from cell import *
from sudoku_generator import *


def pre_fill_board(cell_number, board_to_use, empty_board):
    SCREEN.fill("White")
    board = SudokuGenerator(9, cell_number)
    board.draw()


    # Credit to https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/ for code inspo
    for i in range (9):
        for j in range(9):
            if board_to_use[i][j] !=0:

                #populates board
                if empty_board[i][j] == 0:
                    pygame_board = ACTUAL_FONT.render(str(board_to_use[i][j]), 1, (GREY))
                else:
                    pygame_board = ACTUAL_FONT.render(str(board_to_use[i][j]), 1, (BLACK))
                SCREEN.blit (pygame_board, (i* SQUARE_SIZE+15, j* SQUARE_SIZE +15))

def if_winner(board, answer_board):
    #checks if game is won
    if board == answer_board:
        return True
    else:
        return False

def is_winner():
    while True:
        MOUSE_POS_GAME = pygame.mouse.get_pos()
        SCREEN.fill("white")
        SCREEN.blit(BACKGROUND, (0, 0))
        #initialization of buttons
        title_font = pygame.font.Font("font.ttf", 100)
        menu_text = title_font.render("GAME WON", 0, "White")
        menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 100))
        play_again = Button(BUTTON_BACKGROUND, (WIDTH // 2, HEIGHT // 3 + 100), "Play Again", get_font(75), "white")
        exit_button = Button(image=BUTTON_BACKGROUND, pos=(WIDTH // 2, HEIGHT//3 +300), text="Exit",
                             font=get_font(75),
                             color="white")
        #display on screen
        play_again.update(SCREEN)
        exit_button.update(SCREEN)
        SCREEN.blit(menu_text, menu_rect)

        #pygame functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again.checkInput(MOUSE_POS_GAME):
                    main_menu()
                    break
                if exit_button.checkInput(MOUSE_POS_GAME):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
def is_looser():

    while True:
        #Changes screens an buttons to game lost screen
        MOUSE_POS_GAME = pygame.mouse.get_pos()
        SCREEN.fill("white")
        SCREEN.blit(BACKGROUND, (0, 0))

        #initialization of buttons
        title_font = pygame.font.Font("font.ttf", 100)
        menu_text = title_font.render("GAME OVER", 0, "White")
        menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT // 3 - 100))
        play_again = Button(BUTTON_BACKGROUND, (WIDTH // 2, HEIGHT // 3 + 100), "Play Again", get_font(75), "white")
        exit_button = Button(image=BUTTON_BACKGROUND, pos=(WIDTH // 2, HEIGHT//3+300), text="Exit",
                             font=get_font(75),
                             color="white")
        #display in the screen
        play_again.update(SCREEN)
        exit_button.update(SCREEN)
        SCREEN.blit(menu_text, menu_rect)

        #pygame functionality
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again.checkInput(MOUSE_POS_GAME):
                    main_menu()
                    break
                if exit_button.checkInput(MOUSE_POS_GAME):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
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
    pre_fill_board(cell_number, usable_board, empty_board)

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
                # checks for what position was clicked
                clicked_col = int(MOUSE_POS_GAME[0] / SQUARE_SIZE)
                clicked_row = int(MOUSE_POS_GAME[1] / SQUARE_SIZE)


                if clicked_row <= 8:
                    #Highlights chosen cell
                    pre_fill_board(cell_number, usable_board, empty_board)
                    rect = pygame.Rect(clicked_col*SQUARE_SIZE, clicked_row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                    pygame.draw.rect(SCREEN, DARKER_LINE_COLOR,rect, LINE_WIDTH+1)

                    #clears number inside of cell when usable cell clicked
                    if empty_board[clicked_col][clicked_row] == 0:
                        psudo_board.mark_square(clicked_col, clicked_row, 0)
                        usable_board = psudo_board.get_board()
                        pre_fill_board(cell_number, usable_board, empty_board)
                        rect = pygame.Rect(clicked_col * SQUARE_SIZE, clicked_row * SQUARE_SIZE, SQUARE_SIZE,
                                           SQUARE_SIZE)
                        pygame.draw.rect(SCREEN, DARKER_LINE_COLOR, rect, LINE_WIDTH+1)

                #reset button
                if reset_button.checkInput(MOUSE_POS_GAME):
                    main_menu()
                    break
                #refresh buttton, clears the board and sets all values to 0
                if refresh_button.checkInput(MOUSE_POS_GAME):
                    for i in range(9):
                        for j in range(9):
                            if empty_board[i][j] == 0 and usable_board[i][j] != empty_board[i][j]:
                                psudo_board.mark_square(i, j, 0)
                                usable_board = psudo_board.get_board()
                                pre_fill_board(cell_number, usable_board, empty_board)

                    pre_fill_board(cell_number, usable_board, empty_board)

                # exit button
                if exit_button.checkInput(MOUSE_POS_GAME):
                    pygame.quit()
                    sys.exit()

            #answers for each key press

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    number = 1
                elif event.key == pygame.K_2:
                    number = 2
                elif event.key == pygame.K_3:
                    number = 3
                elif event.key == pygame.K_4:
                    number = 4
                elif event.key == pygame.K_5:
                    number = 5
                elif event.key == pygame.K_6:
                    number = 6
                elif event.key == pygame.K_7:
                    number = 7
                elif event.key == pygame.K_8:
                    number = 8
                elif event.key == pygame.K_9:
                    number = 9
                else:
                    #pop up when no number key is pressed
                    pop_up = Button(BLUE_BACKGROUND,(WIDTH // 2, HEIGHT//3+75),"Invalid Input",get_font(50),"White")
                    small_text = Button(None, (WIDTH // 2, HEIGHT//3+105), "Click anywhere to resume", get_font(25), "White")
                    pop_up.update(SCREEN)
                    small_text.update(SCREEN)
                    continue



                # checks for what position was clicked
                clicked_col = int(MOUSE_POS_GAME[0] / SQUARE_SIZE)
                clicked_row = int(MOUSE_POS_GAME[1] / SQUARE_SIZE)

                # check if space is empty and use user input in board
                if psudo_board.available_square(clicked_col, clicked_row):
                    psudo_board.mark_square(clicked_col,clicked_row, number)
                    usable_board = psudo_board.get_board()
                    pre_fill_board(cell_number, usable_board, empty_board)
                    if psudo_board.board_is_full():
                        if if_winner(usable_board, answer_board):
                            is_winner()
                        else:
                            is_looser()


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

        #pygame functionality and determines how many cells to be removed
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
    #CODE THAT KEEPS THE PYGAME SCREEN RUNNING
    start = main_menu()


