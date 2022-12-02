
class Button:
    def __init__(self,image,  pos, text, font, color):
        self.image = image
        self.pos_x= pos[0]
        self.pos_y = pos[1]
        self.text = text
        self.font = font
        self.color = color
        self.button_text = self.font.render(self.text, True, self.color)
        if self.image is None:
            self.image = self.button_text
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.button_text_rect = self.button_text.get_rect(center=(self.pos_x, self.pos_y))

    def update (self, screen): # credits to BaralTech on youtube for code inspo
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.button_text, self.button_text_rect)

    def checkInput(self, position):
        if position[0] in range (self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False