import pygame]
class PhilSwift:
    def __init__(self, pos):
        self.image = pygame.image.load("Phil Swift.png")
        self.image = pygame.transform.scale(self.image, (80, 60))
        self.Speed = pygame.math.Vector2(3,4)
        self.rect = self.image.get_rect()
        self.rect.center = pos

    def move(self):
        screeninfo = pygame.display.Info()
        self.rect.move_ip(self.Speed)
        screenwidth = screeninfo.current_w
        if self.rect.right > screenwidth:
            self.Speed.x *= -1
        if self.rect.left < 0:
            self.Speed.x *= -1
        screenheight = screeninfo.current_h
        if self.rect.top < 0:
            self.Speed.y *= -1
        if self.rect.bottom > screenheight:
            self.Speed.y *= -1
    def draw(self, screen):
        screen.blit(self.image, self.rect)
