import pygame, random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.__has_splitted = False


    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt 
        
    def split(self):
        if self.radius == ASTEROID_MIN_RADIUS:
            self.kill()
        elif self.radius > ASTEROID_MIN_RADIUS:
            self.kill()
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_obj_1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_obj_2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_obj_1.velocity += self.velocity.rotate(random_angle) * 1.2
            new_obj_2.velocity += self.velocity.rotate(-random_angle) * 1.2

        


