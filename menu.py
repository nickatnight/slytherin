import pygame


class Menu:
    """
    Game Menus and screens for the snake game

    Attributes:
        display: the dimensions of the playing screen
        pallet: the parent window that will display the game
    """

    def __init__(self, display, pallet):
        self.display = display
        self.pallet = pallet
        self.font = pygame.font.SysFont("Arial", 30, bold=True)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)

    def text_objects(self, text, color):
        """
        Get the text text object by rendering the *text* with the specied *color*
        returns the font and the rectangular surface area
        """
        textSurface = self.font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def center_text(self, line, y_cord=0):
        """
        Center text on on axis with *line* specified by a *y_cord* offset
        """
        textSurf, textRect = self.text_objects(line, self.red)
        textRect.center = (self.display[0]/2, self.display[1]/2 + y_cord)
        self.pallet.blit(textSurf, textRect)

    def show(self, menu_type):
        """
        Display the specified text
        """
        if menu_type == "lose":
            self.center_text("You Lose.")
        elif menu_type == "greet":
            self.greet_menu()
        elif menu_type == "gameover":
            self.center_text("Game over. Press c to")
            self.center_text("continue or q to quit.",30)

    def greet_menu(self):
        pass

    def op_menu(self):
        pass
