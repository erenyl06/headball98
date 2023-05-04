from __future__ import absolute_import
import pygame
from config import Colors, Globals
from scene import GameScene, SceneManager

def main():
    screen = pygame.display.set_mode((Globals.win_width,Globals.win_height))
    pygame.display.set_caption("HeadBall98")
    clock = pygame.time.Clock()
    manager = SceneManager()
    running= True
    pygame.init()
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(Colors.black)
        manager.scene.render(screen)
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()



