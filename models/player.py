# Objet du joueur
import pygame

from models.projectile import Projectile


# TODO : Ajouter les attributs suivant (définir une valeur nulle (0, 0.0, "" ou false selon le type) dans le constructeur)
# vitesse de rotation ==> INT OU FLOAT
# une vitesse de déplacement ==> INT OU FLOAT
# des points de vie ==> INT OU FLOAT
# une puissance de tir ==> INT OU FLOAT
# un délai de tir ==> INT OU FLOAT
# une vitesse de projectile ==> INT OU FLOAT
# Position (x, y)


# TODO : Trouver les images pour le joueur, les projectiles, etc...


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.v_rotation = 4.0
        self.velocity = 3
        self.health = 100
        self.max_health = 100
        self.power_shoot = 5
        self.cooldown = 0.80
        self.speed_shoot = 10
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(
            pygame.image.load('assets/player2.png'), (90, 58))
        self.rect = self.image.get_rect()
        # map to check the pressed button
        self.pressed = {}


    def launchProjectile(self) : 
        self.all_projectiles.add(Projectile(self))


        
        
        

    def updatePos(self, screen):
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
