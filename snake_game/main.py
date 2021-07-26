import pygame
from pygame.locals import *
import time

size = 40

class Apple:
    def __init__(self, parent_screen, ):
        # loading the apple image
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.x = size*4
        self.y = size*4

    def place(self):
        # to place the apple
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

class Snake:
    def __init__(self, parent_screen, length):
        # loading the block image
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resources/block.jpg").convert()

        # defining the size of the snake
        self.x = [size]*length
        self.y = [size]*length

        # default direction
        self.direction = 'right'

        # initial length of snake
        self.length = length

    # place the block at a certain position on the screen
    def place(self):
        self.parent_screen.fill((240, 248, 255))

        # to draw the multiple blocks of the chain
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move(self):

        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i - 1]

        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size

        self.place()

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1080, 500)) # display screen
        self.screen.fill((240, 248, 255))
        self.snake = Snake(self.screen, 6)
        self.snake.place()
        self.apple = Apple(self.screen)
        self.apple.place()

    def 

    def play(self):
        self.snake.move()
        self.apple.place()
        time.sleep(0.2)

    def run(self):
        running = True

        # event loop
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                    if event.key == K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running = False

            self.play()


if __name__ == "__main__":
    game = Game()
    game.run()
