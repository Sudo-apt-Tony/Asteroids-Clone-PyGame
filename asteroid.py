from circleshape import *
from constants import ASTEROID_MAX_RADIUS, ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):

    group_a = pygame.sprite.Group()
    group_b = pygame.sprite.Group()
    group_c = pygame.sprite.Group()
    containers = (group_a, group_b, group_c)

    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        spawn_angle = random.uniform(20,50)
        direction_one = self.velocity.rotate(spawn_angle)
        direction_two = self.velocity.rotate(-spawn_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        thing_one = Asteroid(self.position[0], self.position[1], new_radius)
        thing_two = Asteroid(self.position[0], self.position[1], new_radius)
        thing_one.velocity = direction_one * 1.2
        thing_two.velocity = direction_two * 1.2

