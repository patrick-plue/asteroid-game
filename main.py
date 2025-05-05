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

    game_state = "game"
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    score = 0
    font = pygame.font.SysFont("Arial", 20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60)
        dt /= 1000

        if game_state == "game":

            screen.fill("black")
            score_display = font.render(f"Score: {score} hits", True, "white")
            textRect = score_display.get_rect()
            screen.blit(score_display, textRect)
            textRect.bottom = 40

            updatable.update(dt)
            for el in drawable:
                el.draw(screen)
            for asteroid in asteroids:
                if asteroid.check_collision(player):
                    game_state = "game_over"

            for asteroid in asteroids:
                for bullet in shots:
                    if bullet.check_collision(asteroid):
                        asteroid.split()
                        bullet.kill()
                        score += 1
        elif game_state == "game_over":
            screen.fill("black")
            font = pygame.font.SysFont('arial', 40)
            title = font.render('Game Over', True, (255, 255, 255))
            screen.blit(title, (SCREEN_WIDTH/2 - title.get_width() /
                        2, SCREEN_HEIGHT/2 - title.get_height()/3))
            pygame.display.update()

        # call this last
        pygame.display.flip()


if __name__ == "__main__":
    main()
