import random
from circleshape import CircleShape
import pygame
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x,y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position,self.radius, 2 )
        
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            vec1 = pygame.math.Vector2.rotate(self.velocity, angle)
            vec2 = pygame.math.Vector2.rotate(self.velocity, -angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            ast1 = Asteroid(self.position[0], self.position[1], new_radius)
            ast2 = Asteroid(self.position[0], self.position[1], new_radius)
            ast1.velocity = vec1 * 1.2
            ast2.velocity = vec2 * 1.2


        
