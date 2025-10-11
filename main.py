import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
    FONT_COLOR,
)


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    score = 0
    score_font = pygame.font.SysFont("Comic Sans MS", 44)
    score_text = score_font.render(f"Score: {score}", True, FONT_COLOR)

    dt = 0
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # update
        updatable.update(dt)

        # resolve
        for rock in asteroids:
            if rock.detect_collision(player):
                print(f"Game over! Score: {score}")
                running = False

            for shot in shots:
                if rock.detect_collision(shot):
                    shot.kill()
                    rock.split()
                    score += 1
                    score_text = score_font.render(
                        f"Score: {score}", False, FONT_COLOR)

        # draw
        screen.fill("black")
        screen.blit(score_text, (10, 10))
        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
