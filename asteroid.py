import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        child_velocity_one = self.velocity.rotate(angle)
        child_velocity_two = self.velocity.rotate(-angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_one = Asteroid(self.position.x, self.position.y, child_radius)
        child_two = Asteroid(self.position.x, self.position.y, child_radius)
        child_one.velocity = child_velocity_one * 1.2
        child_two.velocity = child_velocity_two * 1.2
