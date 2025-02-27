import pygame
from circleshape import CircleShape
from random import choice


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        colors = ["purple", "brown", "yellow", "blue"]
        rand_color = choice(colors)
        pygame.draw.circle(screen, rand_color, self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
