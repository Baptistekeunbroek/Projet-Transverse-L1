from constantes import *
from Classes.Jeu import Jeu
import math


def initialisation_temps():
    time=0
    temps=0
    game_time=100
    main(time,temps,game_time)

def main(time,temps,game_time):
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) #Retourne une fenetre en plein écran selon la taille de l'écran de l'utilisateur
    fond = pygame.transform.scale(pygame.image.load("./ressources/fond.jpg").convert_alpha(),(SCREEN_WIDTH, SCREEN_HEIGHT)) # Définit le fond d'écran du jeu avec une image adapté au plein écran de l'utilisateur
    pygame.display.set_caption("Gravity Basket") # Définit le nom de la fenêtre du jeu
    done = False # Condition d'arrêt du jeu 
    clock = pygame.time.Clock() # Fonction de Pygame permettant de simuler une horloge interne
    game = Jeu() # On définit les données initiales du jeu

    # -------- Main Program Loop -----------

    while not done:

        keys = pygame.key.get_pressed() #Fonction de Pygame permettant d'utiliser les touches du clavier
        if keys[pygame.K_LEFT] or keys[pygame.K_a]: #Si le joueur appuie sur "Flèche gauche" ou "A"
            game.player.go_left() #Fonction permettant au personnage d'aller à gauche
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]: #Si le joueur appuie sur "Flèche droite" ou "D"
            game.player.go_right() #Fonction permettant au personnage d'aller à droite
        if pygame.mouse.get_pressed()[0]: #Si le joueur appuie sur la souris ou le Pad tactile
            pos = pygame.mouse.get_pos() #Donne les coordonnées de la souris
            game.player.charge(pos) #Lance la fonction de charge (soit la force avec laquelle sera lancé le ballon)

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos() #Donne les coordonnées de la souris
                game.player.throw(pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game.player.jump() #Lance la fonction de saut

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    game.player.stop()
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    game.player.stop()
        
        time +=1
        if time==fps:
            time=0
            temps+=1
            if temps>game_time:
                done=True
                pygame.QUIT

        game.update() #Met à jour les éléments du jeu

        screen.blit(fond, (0, 0)) #On définit le fond du jeu en arriere plan
        game.draw(screen) #On définit l'emplacement de toutes les images du jeu
        clock.tick(fps) #Met à jour l'horloge
        pygame.display.flip() #Met à jour l'affichage

    pygame.quit() #On quitte le jeu


initialisation_temps();