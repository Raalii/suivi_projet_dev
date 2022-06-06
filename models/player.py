# Objet du joueur
# from models.game import Game
from lib.lib import Lib
import pygame

from models.projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, id : int , game):
        super().__init__()
        self.game = game
        # id pour différencier le joueur 1 et 2 (et 3, 4 si besoin)
        self.id = id
        self.v_rotation = 4.0
        self.velocity = 3
        self.health = 100
        self.max_health = 100
        self.power_shoot = 5
        self.cooldown = 0.80
        self.speed_shoot = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(
            pygame.image.load('assets/player' + str(self.id) + '.png'), (90, 58))
        self.original_image = self.image.convert_alpha()
        
        self.rect = self.image.get_rect()
        # map to check the pressed button
        self.pressed = {}
        self.angle = 0    
        # On s'en fou de ça, c'est juste pour positionner le joueur 2 autre part que dans le mm emplacement que le j1 
        if id == 2 :
            self.rot_center(180)
            self.rect.x = 500
            self.rect.y = 500
    
    
    def launch_projectile(self) : 
        """Ajoute un projectile""" 
        self.all_projectiles.add(Projectile(self))

    def update_pos(self, screen):
        """Fonction qui va mettre à jour la position du joueur (en fonction des touches enfoncée)"""
        # print(self.pressed)
        # if the right button are pressed (et les bords tu check aussi tu connais)
        if self.pressed.get(pygame.K_RIGHT) and self.rect.x + self.rect.width < screen.get_width():
            self.move_right()
            
        # flemme de commenter
        if self.pressed.get(pygame.K_LEFT) and self.rect.x > 0:
            self.move_left()
            
        # flemme de commenter mais pareil
        if self.pressed.get(pygame.K_UP) and self.rect.y > 0:
            self.move_up()
            
        # flemme de commenter  
        if self.pressed.get(pygame.K_DOWN) and self.rect.y + self.rect.height < screen.get_height():
            self.move_down()

        
        # Touche pour checker la rotation
        if self.pressed.get(pygame.K_x):
            self.rot_center(self.angle + 1)
            
        # Pareil mais de l'autre côté 
        if self.pressed.get(pygame.K_c):
            self.rot_center(self.angle - 1)
            
            
    def rot_center(self, angle):
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_right(self):
        print("Déplacement vers la droite")
        self.rect.x += self.velocity
        if Lib.check_colliders(self, self.game.player2_group):
            self.rect.x -= self.velocity

    def move_left(self):
        print("Déplacement vers la gauche")
        self.rect.x -= self.velocity
        if Lib.check_colliders(self, self.game.player2_group):
            self.rect.x += self.velocity

    def move_up(self):
        print("Déplacement vers le haut")
        self.rect.y -= self.velocity
        if Lib.check_colliders(self, self.game.player2_group):
            self.rect.y += self.velocity

    def move_down(self):
        print("Déplacement vers le bas")
        self.rect.y += self.velocity
        if Lib.check_colliders(self, self.game.player2_group):
            self.rect.y -= self.velocity