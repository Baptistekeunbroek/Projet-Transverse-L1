import pygame

pygame.init()
infoObject = pygame.display.Info()
SCREEN_WIDTH = infoObject.current_w
SCREEN_HEIGHT = infoObject.current_h
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAVITE = 500
fps = 60

#Sprite des différents déplacements 
spritecourse = [pygame.image.load(f"ressources/course{i}.png") for i in range(1, 8)]

spritesaut = [pygame.image.load(f"ressources/saut{i}.png") for i in range(4)]

spritetir = [pygame.image.load(f"ressources/saut{i}.png") for i in range(3, 7)]
