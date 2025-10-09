import pygame

from constants import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_SHOOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: int,  y: int):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.shoot_cooldown = 0

    def draw(self, surface):
        pygame.draw.polygon(
            surface,
            color="white",
            points=self.triangle(),
            width=2,
        )

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def update(self, dt):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(-dt)
        if keys[pygame.K_s]:
            self.rotate(-dt)
        if keys[pygame.K_f]:
            self.rotate(dt)
        if keys[pygame.K_k]:
            self.shoot()

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.shoot_cooldown > 0:
            return
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN

        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1) * PLAYER_SHOOT_SPEED
        shot.velocity = shot.velocity.rotate(self.rotation)
