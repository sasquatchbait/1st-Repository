import pygame
pygame.init()
ScreenSize = (width, height) = (800, 600)
Screen = pygame.display.set_mode(ScreenSize)
Light_Blue = (255, 255, 0)
clock = pygame.time.Clock()
Screeninfo = pygame.display.Info()

def main():
    while True:
        clock.tick(60)
        move()
        Screen.fill(Light_Blue)
        Screen.blit(Phil, Phil_rect)
        pygame.display.flip()


def move():
    Phil_rect.move_ip(Speed)
    ScreenWidth = Screeninfo.current_w
    if Phil_rect.right > ScreenWidth:
        Speed.x *= -1
    if Phil_rect.left < 0:
        Speed.x *= -1
    ScreenHeight = Screeninfo.current_h
    if Phil_rect.top < 0:
        Speed.y *= -1
    if Phil_rect.bottom > ScreenHeight:
        Speed.y *= -1


if __name__ == "__main__":
    main()

