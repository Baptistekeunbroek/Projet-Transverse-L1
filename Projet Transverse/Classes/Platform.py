import pygame


class Platform(pygame.sprite.Sprite): #Création rectangles qui vérifient que le ballon touche le panier
    def __init__(self, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
