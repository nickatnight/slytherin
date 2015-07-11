import pygame


class Menu:
    """ Game Menus and screens for the snake game """

    def __init__(self, display, pallet):
        self.display = display
        self.pallet = pallet
        self.font = pygame.font.SysFont("Arial", 30, bold=True)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

    def text_objects(self, text, color):
        textSurface = self.font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def center_text(self, line, y_cord=0):
        textSurf, textRect = self.text_objects(line, self.red)
        textRect.center = (self.display[0]/2, self.display[1]/2 + y_cord)
        self.pallet.blit(textSurf, textRect)

    def show(self, menu_type):
        if menu_type == "lose":
            self.center_text("You Lose.")
        elif menu_type == "greet":
            self.greet_menu()
        elif menu_type == "opt":
            self.op_menu()

    def greet_menu(self):
        pass

    def op_menu(self):
        pass
