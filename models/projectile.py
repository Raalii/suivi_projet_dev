import pygame

# from models.player import Player

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        # J'utilise l'id aussi pour checker les collisions (genre si l'id du projectile est différent de l'id du joueur touché par ex ==> tir ennemi)
        self.id = player.id
        self.angle = player.angle
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        # Ici le + 85 et 21 c a modifier juste pour du test
        self.rect.x = player.rect.x + 85
        self.rect.y = player.rect.y + 21
        
          
    def move(self) : 
        # TODO : faire une formule en fonction de l'angle 
        if self.angle == 90 : 
            self.rect.y += self.velocity
            
        elif self.angle == 180 : 
            self.rect.x -= self.velocity         
        elif self.angle == 270 :
            self.rect.y += self.velocity
        else :
            self.rect.x += self.velocity
        