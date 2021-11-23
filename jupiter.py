import random

from pygame.math import Vector2

class Jupiter:
    def __init__(self,largeur=1000, hauteur=800):
        self.nom = "Jupiter"
        self.position = Vector2(largeur/2, hauteur/2)
        self.rayon = 3
        self.masse = 2.36
        self.couleur = (236, 255, 51)


        def repulsion(self):
            pass