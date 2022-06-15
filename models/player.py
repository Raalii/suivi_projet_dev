# Objet du joueur
# from models.game import Game
from lib.lib import Lib
import pygame

from models.projectile import Projectile


class Player(pygame.sprite.Sprite):
    def __init__(self, id, v_rotation, velocity, health, power_shoot, cooldown, speed_shoot, game):
        self.boutons_ps4_controllers = {
            "x": 0,
            "circle": 1,
            "square": 2,
            "triangle": 3,
            "share": 4,
            "PS": 5,
            "options": 6,
            "left_stick_click": 7,
            "right_stick_click": 8,
            "L1": 9,
            "R1": 10,
            "up_arrow": 11,
            "down_arrow": 12,
            "left_arrow": 13,
            "right_arrow": 14,
            "touchpad": 15
        }
        
        super().__init__()
        self.game = game
        # id pour différencier le joueur 1 et 2 (et 3, 4 si besoin)
        self.id = id
        self.v_rotation = v_rotation
        self.velocity = velocity
        self.health = health
        self.max_health = health
        self.power_shoot = power_shoot
        self.cooldown = cooldown
        self.speed_shoot = speed_shoot
        self.last_time_when_projectile_launch = 0.0
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.transform.scale(
            pygame.image.load('assets/player' + str(self.id) + '.png'), (90, 58))
        self.original_image = self.image.convert_alpha()

        self.rect = self.image.get_rect()
        # map to check the pressed button
        self.pressed = {}
        self.angle = 0
        # On s'en fou de ça, c'est juste pour positionner le joueur 2 autre part que dans le mm emplacement que le j1
        if id == 2:
            self.rot_center(180)
            self.rect.x = 500
            self.rect.y = 500
            self.power_shoot = 10
            self.health = 400
            self.max_health = 400

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            return True
        return False

    def health_bar(self, surface):
        color_health = (111, 210, 46)
        back_color_health = (60, 60, 60)

        bar_position = [self.rect.x, self.rect.y, self.health /
                        self.max_health * 100, 5]  # use formular to percent
        back_bar_position = [self.rect.x,
                             self.rect.y, 100, 5]  # use 100 to percent

        pygame.draw.rect(surface, back_color_health, back_bar_position)
        pygame.draw.rect(surface, color_health, bar_position)

    def launch_projectile(self):
        """Ajoute un projectile"""
        if pygame.time.get_ticks() - self.last_time_when_projectile_launch >= self.cooldown * 1000:
            self.all_projectiles.add(Projectile(self))
            self.last_time_when_projectile_launch = pygame.time.get_ticks()

    def update_pos(self, screen):
        """Fonction qui va mettre à jour la position du joueur (en fonction des touches enfoncée)"""
        # print(self.pressed)
        # if the right button are pressed (et les bords tu check aussi tu connais)
        if self.pressed.get(pygame.K_RIGHT) and self.rect.x + self.rect.width < screen.get_width():
            self.move_right()

        if self.pressed.get(pygame.K_LEFT) and self.rect.x > 0:
            self.move_left()

        if self.pressed.get(pygame.K_UP) and self.rect.y > 0:
            self.move_up()

        if self.pressed.get(pygame.K_DOWN) and self.rect.y + self.rect.height < screen.get_height():
            self.move_down()

        if self.pressed.get(pygame.K_SPACE) or self.pressed.get(self.boutons_ps4_controllers["x"]):
            self.launch_projectile()

        # Touche pour checker la rotation
        if self.pressed.get(pygame.K_x) or self.pressed.get(self.boutons_ps4_controllers["L1"]):
            self.rot_center(self.angle + self.v_rotation)

        # Pareil mais de l'autre côté
        if self.pressed.get(pygame.K_c  or self.pressed.get(self.boutons_ps4_controllers["R1"])):
            self.rot_center(self.angle - self.v_rotation)

    def rot_center(self, angle):
        self.angle = angle
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_right(self):
        print("Déplacement vers la droite")
        self.rect.x += self.velocity
        if Lib.check_colliders(self, self.game.player2_group if self.id == 1 else self.game.player1_group):
            self.rect.x -= self.velocity

    def move_left(self):
        print("Déplacement vers la gauche")
        self.rect.x -= self.velocity
        if Lib.check_colliders(self, self.game.player2_group if self.id == 1 else self.game.player1_group):
            self.rect.x += self.velocity

    def move_up(self):
        print("Déplacement vers le haut")
        self.rect.y -= self.velocity
        if Lib.check_colliders(self, self.game.player2_group if self.id == 1 else self.game.player1_group):
            self.rect.y += self.velocity

    def move_down(self):
        print("Déplacement vers le bas")
        self.rect.y += self.velocity
        if Lib.check_colliders(self, self.game.player2_group if self.id == 1 else self.game.player1_group):
            self.rect.y -= self.velocity
