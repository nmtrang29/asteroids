import pygame
from player import *
from circleshape import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0))
        player.draw(screen)
        pygame.display.flip() 

        # limit the framerate to 60 FPS
        dt = clock.tick(60) * 000.1
    
if __name__ == "__main__":
    main()
