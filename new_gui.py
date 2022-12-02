import pygame, sys
from button import *
from constants import *

pygame.init()
pygame.display.set_caption("Sudoku Group 12^2")
cells = 0


def sudoku(cell_number):  # second main function

    while True:
        #refills screen and gets position of the Mouse
        SCREEN.fill("white")
        MOUSE_POS = pygame.mouse.get_pos()


        #initializes buttons
        reset_button= Button(image=None, pos=(200,675), text="Reset", font=get_font(50),color="black")
        refresh_button = Button(image=None, pos=(360,675), text="Refresh", font=get_font(50),color="black")
        exit_button = Button(image=None, pos=(500,675), text="Exit", font=get_font(50),color="black")


        #draws buttons
        reset_button.update(SCREEN)
        refresh_button.update(SCREEN)
        exit_button.update(SCREEN)

        #pygame mechanism for display
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reset_button.checkInput(MOUSE_POS):
                    main_menu()
                if refresh_button.checkInput(MOUSE_POS):
                    pass
                if exit_button.checkInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

def get_font(size): #credits to baraltech on youtube for code inspo
    return pygame.font.Font("font.ttf", size)

def main_menu(): #initial screen

    while True:
        SCREEN.blit(BACKGROUND, (0,0))
        #set the color of background and get the position of the mouse
        MOUSE_POS = pygame.mouse.get_pos()

        #main menu initialization
        title_font = pygame.font.Font("font.ttf", 150)

        menu_text = title_font.render("Sudoku",0, "White")
        menu_rect = menu_text.get_rect(center=(WIDTH // 2, HEIGHT//3 -100))

        #initialize buttons CREDIT to TA logan for dimensions
        easy_button = Button(image= BUTTON_BACKGROUND ,pos=(WIDTH // 2, HEIGHT//3 +50),text = "Easy", font=get_font(75), color="White" )
        medium_button = Button(BUTTON_BACKGROUND, (WIDTH // 2, HEIGHT//3 +200), "Medium", get_font(75), "White")
        hard_button = Button(BUTTON_BACKGROUND, (WIDTH // 2, HEIGHT//3 +350), "Hard", get_font(75), "White")

        SCREEN.blit(menu_text, menu_rect)

        #display each button
        for i in [easy_button, medium_button, hard_button]:
            i.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.checkInput(MOUSE_POS):
                    cells = 30
                    sudoku(cells)
                if medium_button.checkInput(MOUSE_POS):
                    cells = 40
                    sudoku(cells)
                if hard_button.checkInput(MOUSE_POS):
                    cells = 50
                    sudoku(cells)
        pygame.display.update()

def draw_lines(): #draws line in board
    pass



main_menu()