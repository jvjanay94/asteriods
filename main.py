import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player

# or import everything: from module_name import *
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0
    player = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    while (True):
        dt = clock.tick(60)/1000
        
        for event in pygame.event.get():
            pass
        player.update(dt)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        log_state()        
        print(dt)
    
    
    # print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    # print(f"Screen width: {SCREEN_WIDTH}\nScreen height: 720")

    


if __name__ == "__main__":
    main()