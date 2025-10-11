import random

import pygame

from constants import (
    GAME_SPEED,
    ASTEROID_MIN_RADIUS,
)
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(
            surface,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * GAME_SPEED * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(spawn_angle)
        v2 = self.velocity.rotate(-spawn_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, new_radius)
        child2 = Asteroid(self.position.x, self.position.y, new_radius)
        child1.velocity = v1 * 1.2
        child2.velocity = v2 * 1.2
