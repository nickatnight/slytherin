import pygame
import random
import time
from menu import Menu


class Sly:
    """ Game engine for Snake """

    def __init__(self, display, pallet):
        pygame.init()
        self.display = display
        self.white = (255, 255, 255)
        self.pallet = pallet
        self.dx = 200
        self.dy = 200
        self.snakelist = []
        self.speed = 10
        self.direction = "up"
        self.img = pygame.image.load('images/finalsnakejj.png')
        self.apple_img = pygame.image.load('images/apple.png')
        self.snakeLength = 2
        self.game_menu = Menu(display, pallet)
        self.apple_x = None
        self.apple_y = None

    def snake(self):
        """ Logic for the snake creation """

        snakeHead = []
        dir_dict = {
            'up': 0,
            'right': 270,
            'left': 90,
            'down': 180
        }

        snakeHead.append(self.dx)
        snakeHead.append(self.dy)
        self.snakelist.append(snakeHead)

        if(len(self.snakelist) > self.snakeLength):
            del self.snakelist[0]

        for seg in self.snakelist[:-2]:
            if seg == snakeHead:
                exit_game = True

        for d in dir_dict.keys():
            if self.direction == d:
                head = pygame.transform.rotate(self.img, dir_dict[d])

        self.pallet.blit(head, (self.snakelist[-1][0], self.snakelist[-1][1]))

        for xy in self.snakelist[:-1]:
            pygame.draw.rect(self.pallet, (0, 255, 0), [xy[0], xy[1], 10, 10])

    def apple_init(self):
        self.apple_x = round(random.randrange(0, self.display[0]-10) / 10.0) * 10.0
        self.apple_y = round(random.randrange(0, self.display[1]-10) / 10.0) * 10.0

    def apple(self, op):
        if op == "place":
            self.pallet.blit(self.apple_img, [self.apple_x, self.apple_y])

        elif op == "check":
            if self.dx == self.apple_x and self.dy == self.apple_y:
                    self.apple_init()
                    self.snakeLength += 1
                    self.speed += 1

    def boundry_check(self):
        if self.dx >= self.display[0] or self.dx < 0 or self.dy >= \
                    self.display[1] or self.dy < 0:
            return True
        else:
            return False

    def game_loop(self, dx_rst, dy_rst, block):
        clock = pygame.time.Clock()
        exit_game = False
        game_over = False
        axis = None

        key_list = {
            'left': [pygame.K_LEFT, 'y'],
            'right': [pygame.K_RIGHT, 'y'],
            'up': [pygame.K_UP, 'x'],
            'down': [pygame.K_DOWN, 'x']
        }

        while not exit_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if axis != 'y':
                        if event.key == pygame.K_LEFT:
                            self.direction = "left"
                            dx_rst = -block
                            dy_rst = 0
                            axis = 'y'
                        elif event.key == pygame.K_RIGHT:
                            self.direction = "right"
                            dx_rst = block
                            dy_rst = 0
                            axis = 'y'
                    if axis != 'x':
                        if event.key == pygame.K_UP:
                            self.direction = "up"
                            dy_rst = -block
                            dx_rst = 0
                            axis = 'x'
                        elif event.key == pygame.K_DOWN:
                            self.direction = "down"
                            dy_rst = block
                            dx_rst = 0
                            axis = 'x'

            exit_game = self.boundry_check()

            self.dy += dy_rst
            self.dx += dx_rst

            self.pallet.fill((0, 0, 0))

            self.apple("place")

            self.snake()

            pygame.display.update()

            self.apple("check")

            clock.tick(self.speed)

        self.game_menu.show("lose")

        pygame.display.update()
        time.sleep(2)

    def run(self):
        pygame.display.set_caption('Slytherin')

        dx_rst = 0
        dy_rst = 0
        block_size = 10

        self.apple_init()        

        self.game_loop(dx_rst, dy_rst, block_size)

        pygame.quit()

if __name__ == "__main__":
    screen_size = (400, 400)
    game_display = pygame.display.set_mode(screen_size)
    s = Sly(screen_size, game_display)
    s.run()
