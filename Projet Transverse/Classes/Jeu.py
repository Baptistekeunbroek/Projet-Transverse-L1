import pygame
from Classes.Joueur import Joueur
from Classes.Panier import Panier
from constantes import *
from random import randint


class Jeu:

    def __init__(self): #initialisation des variables, place le panier au milieu, place le joueur à sa position de départ
        self.player = Joueur()
        self.player.rect.x = 100
        self.player.rect.y = SCREEN_HEIGHT - self.player.rect.height - 100
        self.panier = Panier(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50)
        self.active_sprite = pygame.sprite.Group()
        self.active_sprite.add(self.player)
        self.active_sprite.add(self.panier)
        self.score = 0

    def update(self): #met à jour le jeu, vérif condition colision fond du panier
        self.active_sprite.update()
        self.player.ballons.update(self.panier.hitbox, self.panier.ungoal)
        if pygame.sprite.spritecollide(self.panier.goal, self.player.ballons, dokill=True):
            self.score += 1
            self.paniertp()

    def draw(self, screen): #dessine affichage, ballon, puissance, score, la puissance auigmentant avec la barre
        self.active_sprite.draw(screen)
        self.player.ballons.draw(screen)
        pygame.draw.rect(screen, (128, 0, 0), (250, 10, 50 - (10 - self.player.puissance), 50))
        screen.blit(pygame.font.Font(None, 60).render(f"{self.player.puissance}", 1, (255, 255, 255)), (260, 15))
        screen.blit(pygame.font.Font(None, 60).render("Puissance", 1, (0, 0, 0)), (10, 10))
        screen.blit(pygame.font.Font(None, 60).render(f"Score : {self.score}", 1, (0, 0, 0)), (10, 100))

    def paniertp(self): #prend un chiffre aléatoire pour la téléportation du panier
        newx = randint(0, SCREEN_WIDTH - self.panier.rect.width)
        newy = randint(100, SCREEN_HEIGHT - 400)
        self.panier.change_pos(newx, newy)
