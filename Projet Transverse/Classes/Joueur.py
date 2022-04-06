import pygame
from time import time
from fonctions import *
from math import pi
import math
from constantes import *
from Classes.Ballon import Ballon


class Joueur(pygame.sprite.Sprite):

    def __init__(self): #initialisation des variables, fonction de création de l'objet
        super().__init__()
        self.image = pygame.image.load("ressources/saut0.png")
        self.image_actuelle = [self.image, "right"]
        self.rect = self.image.get_rect()

        self.ballons = pygame.sprite.Group()
        self.vitesse_initiale = 400
        self.angle_saut = 0
        self.puissance = 200

        self.change_x = 0
        self.change_y = 0

        self.direction = "right"
        self.onjump = 0
        self.onthrow = 0
        self.oncharge = 0
        self.onrun = 0

        self.level = None

    def update(self): #mise à jour pour le déplacement et états du joueur (tir, déplacement...)
        if self.rect.y >= SCREEN_HEIGHT - self.rect.height - 99 and self.change_y >= 0:
            if self.onjump:
                self.change_x = 0
            self.change_x = 40
            self.change_y = 0
            self.angle_saut = 0
            self.onjump = 0
            self.onrun = 0
            self.rect.y = SCREEN_HEIGHT - self.rect.height - 100

        if self.onjump:
            self.change_y = vitesse_y(time() - self.onjump, self.vitesse_initiale, self.angle_saut)

        self.change_x = vitesse_x(self.change_x, self.angle_saut)
        self.rect.x += self.change_x / fps
        self.rect.y += self.change_y / fps

        if time() - self.onthrow > 0.5:
            self.onthrow = 0
        self.animation()

    def animation(self): #affichage images des déplacements tirs sauts etc

        if self.onthrow:
            self.image = spritetir[int((time() - self.onthrow) * 8)]
            self.image_actuelle[1] = "right"

        elif self.onjump:
            if time() - self.onjump > 0.5:
                self.image = spritesaut[-1]
            else:
                self.image = spritesaut[int((time() - self.onjump) * 8)]
            self.image_actuelle[1] = "right"

        elif self.onrun:
            if time() - self.onrun > 0.5:
                self.onrun = time()
            self.image = spritecourse[int((time() - self.onrun) * 14)]
            self.image_actuelle[1] = "right"

        elif self.oncharge:
            if time() - self.oncharge > 0.5:
                self.image = spritesaut[2]
            else:
                self.image = spritesaut[int((time() - self.oncharge) * 4)]
            self.image_actuelle[1] = "right"

        else:
            self.image = spritesaut[0]
            self.image_actuelle[1] = "right"

        if self.image_actuelle[1] != self.direction:
            self.image = pygame.transform.flip(self.image, True, False)
            self.image_actuelle[1] = self.direction

    def jump(self): #saut 
        if not self.onjump:
            if self.change_x:
                self.angle_saut = pi / 3
            else:
                self.angle_saut = pi / 2

            self.onjump = time()

    def charge(self, pos):#puissance de tir
        self.stop()

        if not self.oncharge:
            self.oncharge = time()

        if self.puissance < 1000:
            self.puissance += 10

        if pos[0] < self.rect.x:
            self.direction = "left"
        else:
            self.direction = "right"

    def throw(self, pos):#lancer de la balle des qu'on relache clic gauche
        if not self.onthrow:
            angle = math.atan2(0, 1) - math.atan2(pos[1] - self.rect.y, pos[0] - self.rect.x) #obtention de l'angle utilisé pour la fonction vitesse : tangeante de l'angle "0" - tangeante de la postion de la souris et coordonées du joueur en x et y
            if pos[0] < self.rect.x:
                self.direction = "left"
            else:
                self.direction = "right"
            self.onthrow = time()
            self.ballons.add(Ballon(self.rect.x, self.rect.y, angle, self.puissance))
            self.oncharge = 0
            self.puissance = 200

    def go_left(self): #changement vitesse vers la gauche
        if not (self.onthrow or self.oncharge):
            if not self.onrun:
                self.onrun = time()
            self.direction = "left"
            self.change_x = -400

    def go_right(self):#changement vitesse vers la droite
        if not (self.onthrow or self.oncharge):
            if not self.onrun:
                self.onrun = time()
            self.direction = "right"
            self.change_x = 400

    def stop(self): #arrete la course
        if not self.onjump:
            self.onrun = 0
            self.change_x = 0
