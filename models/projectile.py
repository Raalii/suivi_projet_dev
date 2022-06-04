import math
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
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        # TODO : modifier pour que la balle sort du gun
        self.rect.x = player.rect.centerx
        self.rect.y = player.rect.centery
        
          
    def move(self) : 
        angle_in_radians = math.radians(self.angle)
        
        # Formule trigonométrique
        dy = math.sin(angle_in_radians) * self.velocity
        dx = math.cos(angle_in_radians) * self.velocity     
        self.rect.x += int(dx)
        self.rect.y -= int(dy)
        