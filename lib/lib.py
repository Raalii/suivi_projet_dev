import pygame

class Lib(object):
    def __init__(self, *args):
        # super(Lib, self).__init__(*args))
        pass
    
    def check_colliders(sprite : pygame.sprite.Sprite, group) : 
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
        