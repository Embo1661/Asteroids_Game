import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:                                     #infined game loop
        
        for event in pygame.event.get():            #pygame X (exit game)
            if event.type == pygame.QUIT:
                return clock.tick(60)

        screen.fill("black")
        pygame.display.flip()

        # limit the framerate to 60 fps
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
