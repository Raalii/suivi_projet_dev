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
        player = Player()
        bg = pygame.image.load("assets/bg.jpg")
        running = True
        # Closing window
        while running:
            self.screen.blit(bg, (0, 0))
            self.screen.blit(player.image, player.rect)
            
            for projectile in player.all_projectiles :
                projectile.move()
            
            player.all_projectiles.draw(self.screen)
            player.updatePos(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    player.pressed[event.key] = True
                    
                    if event.key == pygame.K_SPACE : 
                        player.launchProjectile()
                    
                elif event.type == pygame.KEYUP:
                    player.pressed[event.key] = False
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()    
            # clock.tick(30)  # Afficher à 30 fps le jeu
            pygame.display.flip()       
                    

game = Setup()
game.start()