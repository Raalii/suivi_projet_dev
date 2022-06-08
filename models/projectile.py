import math
from lib.constants import SCREEN_CONFIG
from lib.lib import Lib
import pygame

# from models.player import Player

class Projectile(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        # J'utilise l'id aussi pour checker les collisions (genre si l'id du projectile est différent de l'id du joueur touché par ex ==> tir ennemi)
        self.id = player.id
        self.player = player
        self.angle = player.angle
        self.velocity = 5
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect()
        # TODO : modifier pour que la balle sort du gun
        self.rect.x = player.rect.centerx
        self.rect.y = player.rect.centery
    
    def __del__(self) : 
        print("DESTRUCTION DE L'OBJET")    
        
          
    def remove(self):
        self.player.all_projectiles.remove(self)
    
          
    def move(self) : 
        angle_in_radians = math.radians(self.angle)
        
        # Formule trigonométrique
        dy = math.sin(angle_in_radians) * self.velocity
        dx = math.cos(angle_in_radians) * self.velocity
        self.rect.x += dx
        self.rect.y -= dy
        
        if self.is_not_in_screen() : 
            self.kill()
            
        for player in Lib.check_colliders(self, self.player.game.player2_group) : 
            print("COLLISIONS AVEC LE JOUEUR ADVERSE")
            self.remove()
            # return True
            player.damage(self.player.game.player2.power_shoot if self.id == 1 else self.player.game.player.power_shoot)
        
        
    
    def is_not_in_screen(self) : 
        return self.rect.x < 0 or self.rect.x > SCREEN_CONFIG['WIDTH'] or self.rect.y < 0 or self.rect.y > SCREEN_CONFIG['HEIGHT'] 