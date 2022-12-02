import pygame, sys
from button import *
from constants import *
from sudoku_generator import *
from cell import *


def draw_lines(): #draws line in board
    #prints horizontal line
    for i in range (1, 9):
        pygame.draw.line(SCREEN, LINE_COLOR, (0, i* SQUARE_SIZE), (WIDTH, i *SQUARE_SIZE), LINE_WIDTH)
    #prints vertical line
    for i in range (1,9):
        pygame.draw.line(SCREEN, LINE_COLOR, (i* SQUARE_SIZE, 0), (i* SQUARE_SIZE, HEIGHT), LINE_WIDTH)
def generate_py_board(cell_number):
    psudo_board = generate_sudo(9, cell_number)
    psudo_board = psudo_board[1]
    return psudo_board

def pre_fill_board(cell_number, board_to_use):
    board = SudokuGenerator(9, cell_number)
    board.draw()


    # Credit to https://www.geeksforgeeks.org/building-and-visualizing-sudoku-game-using-pygame/ for code inspo
    for i in range (9):
        for j in range(9):
            if board_to_use[i][j] !=0:

                #populates board
                pygame_board = ACTUAL_FONT.render(str(board_to_use[i][j]), 1, (0,0,0))
                SCREEN.blit (pygame_board, (i* SQUARE_SIZE+15, j* SQUARE_SIZE +15))



def sudoku(cell_number):  # second main function
    #refills screen
    SCREEN.fill("white")
    #fills board
    board = generate_py_board(cell_number)
    pre_fill_board(cell_number, board)

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
                clicked_row = int(MOUSE_POS_GAME[0]/SQUARE_SIZE)
                clicked_col = int(MOUSE_POS_GAME[1]/SQUARE_SIZE)
                print(clicked_row, clicked_col)

                if reset_button.checkInput(MOUSE_POS_GAME):
                    main_menu()
                    break
                if refresh_button.checkInput(MOUSE_POS_GAME):
                    pre_fill_board(cell_number,board)
                if exit_button.checkInput(MOUSE_POS_GAME):
                    pygame.quit()
                    sys.exit()

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


