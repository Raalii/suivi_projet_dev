# Objet du joueur
import pygame

from models.projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, id : int):
        super().__init__()
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
        self.rect = self.image.get_rect()
        # map to check the pressed button
        self.pressed = {}
        self.angle = 0
        
        # On s'en fou de ça, c'est juste pour positionner le joueur 2 autre part que dans le mm emplacement que le j1 
        if id == 2 :
            self.image = self.rotate(self.image, 180)
            self.rect.x = 500
            self.rect.y = 500
            
        
    def rotate(self, image : pygame.Surface, angle : int):
        """Fonction qui va changer la rotation du joueur. Met à jour l'angle actuel du joueur (utile pour les projectiles par exemple)""" 
        self.angle = angle
        return pygame.transform.rotate(image, angle)
    
    
    def launchProjectile(self) : 
        """Ajoute un projectile"""
        # TODO : Enlever les projectiles quand le projectile sort de l'écran
        self.all_projectiles.add(Projectile(self))


    def updatePos(self, screen):
        """Fonction qui va mettre à jour la position du joueur (en fonction des touches enfoncée)"""
        print(self.pressed)
        # if the right button are pressed (et les bords tu check aussi tu connais)
        if self.pressed.get(pygame.K_RIGHT) and self.rect.x + self.rect.width < screen.get_width():
            self.moveRight()
            
        # flemme de commenter
        if self.pressed.get(pygame.K_LEFT) and self.rect.x > 0:
            self.moveLeft()
            
        # flemme de commenter mais pareil
        if self.pressed.get(pygame.K_UP) and self.rect.y > 0:
            self.moveUp()
            
        # flemme de commenter  
        if self.pressed.get(pygame.K_DOWN) and self.rect.y + self.rect.height < screen.get_height():
            self.moveDown()


    def moveRight(self):
        print("Déplacement vers la droite")
        self.rect.x += self.velocity

    def moveLeft(self):
        print("Déplacement vers la gauche")
        self.rect.x -= self.velocity

    def moveUp(self):
        print("Déplacement vers le haut")
        self.rect.y -= self.velocity

    def moveDown(self):
        print("Déplacement vers le bas")
        self.rect.y += self.velocity
