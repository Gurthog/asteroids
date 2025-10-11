import pygame

from circleshape import CircleShape
from constants import (
    GAME_SPEED,
    SHOT_RADIUS,
)


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def update(self, dt):
        self.position += self.velocity * GAME_SPEED * dt

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )
