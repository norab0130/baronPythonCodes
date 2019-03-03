'''
 Aaron
'''
import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going= True
pic = pygame.image.load("crasysmile.bmp")
colerkey = pic.get_at((0,0))
pic.set_colerkey(colerkey)    
            