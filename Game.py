import pygame
import random
from PhilSwift import *
pygame.init()
ScreenSize = (width, height) = (800, 600)
Screen = pygame.display.set_mode(ScreenSize)
Yellow = (255, 255, 0)
clock = pygame.time.Clock()
screeninfo = pygame.display.Info()
Phil_list = []
for i in range(150):
    Phil_list.append(PhilSwift((random.randint(50, 500), (random).randint(50, 500))))


def main():
    while True:
        clock.tick(60)
        for Phil in Phil_list:
            Phil.move()
        Screen.fill(Yellow)
        for Phil in Phil_list:
            Phil.draw(Screen)
        pygame.display.flip()





if __name__ == "__main__":
    main()

