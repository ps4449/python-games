import pygame
from pygame.locals import *
import time
import random

size = 40

class Apple:
    def __init__(self, parent_screen):
        # loading the apple image
        self.parent_screen = parent_screen
        self.apple = pygame.image.load("resources/apple.jpg").convert()
        self.x = size*4
        self.y = size*4

    def place(self):
        # to place the apple
        self.parent_screen.blit(self.apple, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(0, 24)*size
        self.y = random.randint(0, 14)*size

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

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

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
        self.screen = pygame.display.set_mode((1000, 600)) # display screen
        self.screen.fill((240, 248, 255))
        self.snake = Snake(self.screen, 1)
        self.snake.place()
        self.apple = Apple(self.screen)
        self.apple.place()

    def check_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2+size:
            if y1 >= y2 and y1 < y2+size:
                return True
        return False

    def display_score(self):
        font = pygame.font.SysFont('calibri', 24)
        score = font.render(f"Score: {self.snake.length}", True, (0, 0, 0))
        self.screen.blit(score, (890, 10))

    def play(self):
        self.snake.move()
        self.apple.place()
        self.display_score()
        pygame.display.flip()

        if self.check_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        for i in range(1, self.snake.length):
            if self.check_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Game over"

    def game_over(self):
        self.screen.fill((240, 248, 255))
        font = pygame.font.SysFont('calibri', 24)
        line1 = font.render(f"Game is over! Your score is {self.snake.length}", True, (0, 0, 0))
        self.screen.blit(line1, (200, 300))
        line2 = font.render("To play again press Enter. To exit press Escape!", True, (0, 0, 0))
        self.screen.blit(line2, (200, 350))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.screen, 1)
        self.apple = Apple(self.screen)

    def run(self):
        running = True
        pause = False

        # event loop
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False

                    if not pause:
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

            try:
                if not pause:
                    self.play()
                    time.sleep(0.2)
            except Exception as e:
                self.game_over()
                pause = True
                self.reset()


if __name__ == "__main__":
    game = Game()
    game.run()
