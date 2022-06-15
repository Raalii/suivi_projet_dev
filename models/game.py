from typing import Any
from lib.constants import SCREEN_CONFIG
from models.player import Player
import pygame, json, os
import math

import pygame_menu



# with open(os.path.join("keys.json"), 'r+') as file:
#     button_keys = json.load(file)
# 0: Left analog horizonal, 1: Left Analog Vertical, 2: Right Analog Horizontal
# 3: Right Analog Vertical 4: Left Trigger, 5: Right Trigger
analog_keys = {0: 0, 1: 0, 2: 0, 3: 0, 4: -1, 5: -1}

class Game(object):
    def __init__(self, setup):
        #define if the game started
        # self.is_playing = True
        # Initialising of the basics pygame parametters
        self.setup = setup
        pygame.init()
        # title
        pygame.display.set_caption("Battle Shoot")
        # size
        self.players = self.setup.get_players_info()
        self.bg = pygame.image.load("assets/bg.jpg")
        self.screen = pygame.display.set_mode((SCREEN_CONFIG['WIDTH'], SCREEN_CONFIG['HEIGHT']))
        self.home_menu = pygame_menu.Menu('Bienvenue', 800, 400,
                       theme=pygame_menu.themes.THEME_BLUE)
        self.end_game_menu = pygame_menu.Menu('Fin de partie', 800, 400,
                       theme=pygame_menu.themes.THEME_BLUE)
        self.init(None)
        pygame.font.init()
        self.player1_name = "Zinou"
        self.player2_name = "Rayou"
        self.global_render = {'home_menu' : True, 'end_game_menu' : False, 'game' : False, 'options': False, 'dictaticiel' : False}
        self.global_render_function = {'home_menu' : self.home_menu_render, 'end_game_menu' : self.end_game_menu_render, 'game' : self.game_render, 'options': lambda : None, 'dictaticiel' : lambda : None}
        self.menu_principal_init()
        self.end_game_init()

    def init(self, key) :
        # la clé permet d'enlever le rendu d'un menu et de lancer implcitement le jeu
        
        
        self.player = Player(*self.players[0], self)
        self.player2 = Player(*self.players[1], self)
        self.player1_group = pygame.sprite.Group(self.player)
        self.player2_group = pygame.sprite.Group(self.player2)
        self.clock = pygame.time.Clock()
        self.winner = ""
        joysticks = []
        for i in range(pygame.joystick.get_count()):
            joysticks.append(pygame.joystick.Joystick(i))
        for joystick in joysticks:
            joystick.init()
        
        if key != None : 
            self.global_render[key] = False
            self.global_render['game'] = True
        
            
    
    def start(self) :
        self.init(None)
        self.running()
    
    def update_name_of_players(self, name, number) :
        if number == 1 :
            self.player1_name = name
        else : 
            self.player2_name = name
            
        
     # . init menus
    def menu_principal_init(self) : 
        # pygame_menu.events.EXIT
        self.home_menu.add.text_input('Nom du joueur 1 : ', default=self.player1_name, onchange=lambda x : self.update_name_of_players(x, 1))
        self.home_menu.add.text_input('Nom du joueur 2 : ', default=self.player2_name, onchange=lambda x : self.update_name_of_players(x, 2))
        self.home_menu.add.button('Play', lambda : self.init('home_menu'))
        self.home_menu.add.button('Quit', pygame_menu.events.EXIT)
        

    def end_game_init(self) :
        
        self.label = self.end_game_menu.add.label(self.winner + " a gagné la partie !")
        self.score_label = self.end_game_menu.add.label(self.winner + " a gagné la partie !")
        self.label.add_underline([10, 10, 100], offset=5, width=2)
        self.end_game_menu.add.button('Revenir au menu principal', self.return_to_home_menu_with_end_game_menu)
        self.end_game_menu.add.button('Replay', lambda : self.init('end_game_menu'))
        self.end_game_menu.add.button('Quit', pygame_menu.events.EXIT)
        
    def best_score_render(self) : 
        # texts = []
        my_font = pygame.font.SysFont('Comic Sans MS', 20)
        x = 100
        y = 50
        for scores in self.setup.best_scores :             
            self.screen.blit(my_font.render(str(scores), True, (0, 0, 0)), (x , y))
            y += 50
            
        
        
    
    def return_to_home_menu_with_end_game_menu(self) : 
        self.global_render['home_menu'] = True
        self.global_render['end_game_menu'] = False
        
        
    # . render for the home menu
    def home_menu_render(self) : 
        self.home_menu.update(pygame.event.get())
        self.home_menu.draw(self.screen)
        
        
    # . render for the end game menu
    def end_game_menu_render(self) : 
        self.label.set_title(self.winner +  " a gagné la partie !")
        self.score_label.set_title("Son score est de " + str(round(self.score, 1)) + " points")
        self.end_game_menu.update(pygame.event.get())
        self.end_game_menu.draw(self.screen)
        self.best_score_render()
    
    
    # . render for the game
    def render(self) :
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.player.image, self.player.rect)
        self.screen.blit(self.player2.image, self.player2.rect)
        self.player.all_projectiles.draw(self.screen) 
        self.player.health_bar(self.screen)
        self.player2.health_bar(self.screen)
    
    def get_score(self, player1 : Player, player2 : Player) : 
        health_score = player1.health / player1.max_health * 100
        cooldown_score = player1.cooldown + 1
        velocity_score = player1.velocity / player2.power_shoot
        power_shoot_score = player1.power_shoot / player2.power_shoot
        speed_shoot_score = player1.speed_shoot / player2.speed_shoot
        rotation_score = player1.v_rotation / player2.v_rotation
        
        return health_score * cooldown_score * velocity_score * power_shoot_score * speed_shoot_score * rotation_score
        
        
        
    
    # . render for the game    
    def game_render(self) :      
        self.render()

    
        for projectile in self.player.all_projectiles :
            if projectile.move() : 
                self.winner = self.player1_name
                self.score = self.get_score(self.player, self.player2)
                self.global_render['game'] = False
                self.global_render['end_game_menu'] = True
                self.setup.store_score(self.score, self.winner)
                self.setup.get_best_score()
        
        self.player.update_pos(self.screen)
        self.player2.update_pos(self.screen)
        # events = pygame.event.get()
        
        
        
        for event in pygame.event.get():

            if event.type == pygame.JOYBUTTONDOWN:
                self.player.pressed[event.button] = True
            # HANDLES BUTTON RELEASES
            if event.type == pygame.JOYBUTTONUP:
                self.player.pressed[event.button] = True
            if event.type == pygame.JOYAXISMOTION:
                analog_keys[event.axis] = event.value
                # print(analog_keys)
                # Horizontal Analog
                if abs(analog_keys[0]) > .4:
                    if analog_keys[0] < -.7:
                        self.player.pressed[pygame.K_LEFT] = True
                    else:
                        self.player.pressed[pygame.K_LEFT] = False
                    if analog_keys[0] > .7:
                        self.player.pressed[pygame.K_RIGHT] = True
                    else:
                        self.player.pressed[pygame.K_RIGHT] = False
                        # RIGHT = False
                # Vertical Analog
                if abs(analog_keys[1]) > .4:
                    if analog_keys[1] < -.7:
                        self.player.pressed[pygame.K_UP] = True
                    else:
                        self.player.pressed[pygame.K_UP] = False
                        
                    if analog_keys[1] > .7:
                        self.player.pressed[pygame.K_DOWN] = True
                    else:
                        self.player.pressed[pygame.K_DOWN] = False
                    
#################################################################################################
            
            if event.type == pygame.KEYDOWN:
                self.player.pressed[event.key] = True
                
                if event.key == pygame.K_SPACE : 
                    self.player.launch_projectile()
            
                
            elif event.type == pygame.KEYUP:
                self.player.pressed[event.key] = False
            if event.type == pygame.QUIT:
                pygame.quit() 
            
            
        
        # return True, ""   
        
    
    
    # . running game
    def running(self) :
        

        running = True
        # Closing window
        while running:
            
            for key in self.global_render : 
                if self.global_render[key] :
                    self.global_render_function[key]()
                    pygame.display.flip() 
            self.clock.tick(60)  # Afficher à 60 fps le jeu
        pygame.display.flip()  
    
    
    
        