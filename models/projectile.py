import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 85
        self.rect.y = player.rect.y + 21
        
        
    def move(self) : 
        self.rect.x += self.velocity
        
        # TODO : supprimer le projectile
        