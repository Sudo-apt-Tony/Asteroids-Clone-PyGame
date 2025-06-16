from circleshape import *

class Shot(CircleShape):

    group_a = pygame.sprite.Group()
    group_b = pygame.sprite.Group()
    group_c = pygame.sprite.Group()
    containers = (group_a, group_b, group_c)

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt


