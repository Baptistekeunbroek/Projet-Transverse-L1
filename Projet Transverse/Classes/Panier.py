import pygame
from constantes import *
from Classes.Platform import Platform


class Panier(pygame.sprite.Sprite): #création zones de contact du panier
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ressources/panier.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (int(self.rect.width / 2), int(self.rect.height / 2)))
        self.rect.x = x - self.rect.width // 5
        self.rect.y = y - self.rect.height // 5
        self.hitbox = pygame.sprite.Group()
        self.goal = pygame.sprite.Sprite()
        self.ungoal = pygame.sprite.GroupSingle()

        # coté gauche
        surface = Platform(int(30 / 2), int(90 / 2))
        surface.rect.x = self.rect.x + int(25 / 2)
        surface.rect.y = self.rect.y
        self.hitbox.add(surface)
        surface = Platform(int(30 / 2), int(75 / 2))
        surface.rect.x = self.rect.x + int(55 / 2)
        surface.rect.y = self.rect.y + int(90 / 2)
        self.hitbox.add(surface)
        surface = Platform(int(25 / 2), int(220 / 2))
        surface.rect.x = self.rect.x + int(90 // 2)
        surface.rect.y = self.rect.y + int(150 / 2)
        self.hitbox.add(surface)

        # coté droit

        surface = Platform(int(30 / 2), int(90 / 2))
        surface.rect.x = self.rect.x + int(390 / 2)
        surface.rect.y = self.rect.y
        self.hitbox.add(surface)
        surface = Platform(int(30 / 2), int(75 / 2))
        surface.rect.x = self.rect.x + int(360 / 2)
        surface.rect.y = self.rect.y + int(90 / 2)
        self.hitbox.add(surface)
        surface = Platform(int(25 / 2), int(220 / 2))
        surface.rect.x = self.rect.x + int(320 / 2)
        surface.rect.y = self.rect.y + int(150 / 2)
        self.hitbox.add(surface)

        # bas
        ungoal = Platform(int(200 / 2), int(20 / 2))
        ungoal.rect.x = self.rect.x + int(125 / 2)
        ungoal.rect.y = self.rect.y + int(380 / 2)
        self.ungoal.add(ungoal)

        self.goal = Platform(int(180 / 2), int(20 / 2))
        self.goal.rect.x = self.rect.x + int(130 / 2)
        self.goal.rect.y = self.rect.y + int(330 / 2)

    def change_pos(self, x, y): #téléportation du panier 
        difx = x - self.rect.x
        dify = y - self.rect.y
        self.rect.x = x
        self.rect.y = y
        self.goal.rect.x += difx
        self.goal.rect.y += dify
        for bloc in self.hitbox:
            bloc.rect.x += difx
            bloc.rect.y += dify
        for bloc in self.ungoal:
            bloc.rect.x += difx
            bloc.rect.y += dify
