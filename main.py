import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updateable, drawable) 
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = updateable
    asteroids_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_WIDTH / 2)

    dt = 0

    while True:                                     #infined game loop
        for event in pygame.event.get():            #pygame X (exit game)
            if event.type == pygame.QUIT:
                return clock.tick(60)

        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()                       #update game

        dt = clock.tick(60) / 1000                  #limit the framerate to 60 fps

if __name__ == "__main__":
    main()
