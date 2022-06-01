import pygame 


class Setup(object):
    def __init__(self, *args):
        # Initialising of the basics pygame parametters
        pygame.init()
        # title
        pygame.display.set_caption("Battle Shoot")
        # size
        pygame.display.set_mode((1080,720))
    
    
    
    def start(self):
        running = True
        # Closing window
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()