import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for u in updatable:
            u.update(dt)
        for a in asteroids:
            if player.has_collision(a):
                print('Game over!')
                sys.exit()
            for s in shots:
                if a.has_collision(s):
                    a.split()
                    s.kill()
        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
         # limit the framerate to 60 FPS
        dt = (game_clock.tick(60)) / 1000

if __name__ == "__main__":
    main()