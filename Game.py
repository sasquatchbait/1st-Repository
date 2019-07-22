import pygame
pygame.init
ScreenSize = (width, height) = (800, 600)
Screen = pygame.display.set_mode(ScreenSize)
clock = pygame.time.Clock()
Light_Blue = (0, 0, 255)
Screen.fill(Light_Blue)
pygame.display.flip()