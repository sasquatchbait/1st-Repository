class Phil_Swift
    def __init__(self, pos):
    self.image = pygame.image.load("Phil Swift.png")
    self.image = pygame.transform.scale(Phil, (80, 60))
    self.Speed = pygame.math.Vector2(80, 30)
    self.rect = Phil.get_rect()