import pygame,sys,random
from pygame.locals import *

pygame.init()
size = width,height = (700,700)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BG_COLOR = (0,102,0)


def main():
    global screen,clock

    while True:
        clock.tick(60)
        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size,FULLSCREEN)
                if event.key == K_d:
                    screen = pygame.display.set_mode(size)

        screen.fill(BG_COLOR)

        pygame.display.flip()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
