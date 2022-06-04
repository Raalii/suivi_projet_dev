import pygame

from models.player import Player 

class Setup(object):
    def __init__(self, *args):
        # Initialising of the basics pygame parametters
        pygame.init()
        # title
        pygame.display.set_caption("Battle Shoot")
        # size
        self.screen = pygame.display.set_mode((1200,800))
        
    
    
    
    def start(self):
        # SI TU VEUX JOUER LE JOUEUR 2 ECHANGE JUSTE LE NOM DES VARIABLES
        player2 = Player(1)
        player = Player(2)
        bg = pygame.image.load("assets/bg.jpg")
        running = True
        # Closing window
        while running:
            self.screen.blit(bg, (0, 0))
            self.screen.blit(player.image, player.rect)
            self.screen.blit(player2.image, player2.rect)
            
            for projectile in player.all_projectiles :
                projectile.move()
            
            player.all_projectiles.draw(self.screen)
            player.update_pos(self.screen)
            
            # Todo : change the event with the controllers (rasberry)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    player.pressed[event.key] = True
                    
                    if event.key == pygame.K_SPACE : 
                        player.launch_projectile()
                    
                elif event.type == pygame.KEYUP:
                    player.pressed[event.key] = False
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()    
            # clock.tick(30)  # Afficher à 30 fps le jeu
            pygame.display.flip()       
                    

game = Setup()
game.start()