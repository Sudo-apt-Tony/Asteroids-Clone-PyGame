from shot import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOT_SPEED, SHOT_RADIUS, SHOT_COOLDOWN
from circleshape import *
import pygame

class Player(CircleShape):

    group_a = pygame.sprite.Group()
    group_b = pygame.sprite.Group()
    containers = (group_a, group_b)

    def __init__(self, x, y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0 

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius # pyright: ignore
        b = self.position - forward * self.radius - right # pyright: ignore
        c = self.position - forward * self.radius + right # pyright: ignore
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2) # pyright: ignore

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.timer -= dt

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0 :
            return

        forward = pygame.Vector2(0,1).rotate(self.rotation)
        offset = PLAYER_RADIUS + SHOT_RADIUS + 5
        spawn_at = self.position + forward * offset
        bullet = Shot(spawn_at.x, spawn_at.y, SHOT_RADIUS)
        bullet.velocity += forward * PLAYER_SHOT_SPEED
        self.timer = SHOT_COOLDOWN
        



