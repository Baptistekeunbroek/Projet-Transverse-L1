from math import cos, sin
from constantes import GRAVITE


def vitesse_x(vitesse, angle):
    return vitesse * cos(angle)


def vitesse_y(t, vitesse, angle):
    return GRAVITE * t - vitesse * sin(angle)
