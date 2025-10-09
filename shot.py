import pygame

from constants import SHOT_RADIUS
from circleshape import CircleShape


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * dt

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )
