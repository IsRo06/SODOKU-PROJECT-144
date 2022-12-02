import pygame
from constants import *

class Cell:
    def __init__(self, number, row, col, width, height):
        self.number = number
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False

    def set(self, val):
        self.number = val

    def draw(self, screen):

        number_font = pygame.font.Font(FONT, 60)
        one_surf = number_font.render('1', True, CROSS_COLOR)
        two_surf = number_font.render('2', 0, CROSS_COLOR)
        three_surf = number_font.render('3', 0, CROSS_COLOR)
        four_surf = number_font.render('4', 0, CROSS_COLOR)
        five_surf = number_font.render('5', 0, CROSS_COLOR)
        six_surf = number_font.render('6', 0, CROSS_COLOR)
        seven_surf = number_font.render('7', 0, CROSS_COLOR)
        eight_surf = number_font.render('8', 0, CROSS_COLOR)
        nine_surf = number_font.render('9', 0, CROSS_COLOR)
        if self.selected:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.col *
                                                              SQUARE_SIZE, self.row * SQUARE_SIZE, SQUARE_SIZE,
                                                              SQUARE_SIZE), 12)
            self.selected = False

        if self.number== '1':
            number_one_rect = one_surf.get_rect(
                center=(self.width//8+self.width*self.col, self.height//8+self.height*self.row))
            screen.blit(one_surf, number_one_rect)
        if self.number== '2':
            number_two_rect = two_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(two_surf, number_two_rect)
        if self.number== '3':
            number_three_rect = three_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(three_surf, number_three_rect)
        if self.number== '4':
            number_four_rect = four_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(four_surf, number_four_rect)
        if self.number== '5':
            number_five_rect = five_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(five_surf, number_five_rect)
        if self.number== '6':
            number_six_rect = six_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(six_surf, number_six_rect)
        if self.number== '7':
            number_seven_rect = seven_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(seven_surf, number_seven_rect)
        if self.number== '8':
            number_eight_rect = eight_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(eight_surf, number_eight_rect)
        if self.number== '9':
            number_nine_rect = nine_surf.get_rect(
                center=(self.width//2+self.width*self.col, self.height//2+self.height*self.row))
            screen.blit(nine_surf, number_nine_rect)
