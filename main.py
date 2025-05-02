import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot



def main():
    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroid_field = AsteroidField()
    
    

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        dt = clock.tick(60)
        dt /= 1000

        screen.fill("black")
        updatable.update(dt)
        for el in drawable:
            el.draw(screen)
        for asteroid in asteroids:
            asteroid.check_collision(player)

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.check_collision(asteroid):
                    asteroid.kill()
                    bullet.kill()
             
                

        


        # call this last
        pygame.display.flip()




if __name__ == "__main__":
    main()