import pygame
from time import time
from fonctions import *
from constantes import *


class Ballon(pygame.sprite.Sprite): #initialisation des variables, vitesse définie par la puissance
    def __init__(self, x, y, angle, vitesse):
        super().__init__()
        self.image = pygame.image.load("ressources/ballon.png").convert_alpha()

        self.angle_initiale = angle
        self.rect = self.image.get_rect()
        self.rect.x = x + 25
        self.rect.y = y - 20

        self.time = time() 
        self.vitesse_initiale = vitesse
        self.change_x = vitesse_x(self.vitesse_initiale, self.angle_initiale)

    def update(self, spritegroup1, spritegroup2): #mise à jour du ballon 
        self.change_y = vitesse_y(time() - self.time, self.vitesse_initiale, self.angle_initiale) #mise à jour vitesse
        self.rect.x += self.change_x / fps
        self.rect.y += self.change_y / fps
        if self.rect.x + self.rect.width >= SCREEN_WIDTH or self.rect.x <= 0 or self.rect.y + self.rect.height >= SCREEN_HEIGHT: # si le ballon sort de l'écran sur les cotés il se tue, au haut il retombe
            self.kill()
        if pygame.sprite.spritecollide(self, spritegroup1, False): #s'il touche les rectangles du panier, ça simule la réaction du support
            self.change_x = - self.change_x
            self.rect.x += self.change_x / fps

        if pygame.sprite.spritecollide(self, spritegroup2, False):
            self.vitesse_initiale = - self.vitesse_initiale
