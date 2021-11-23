import random

from pygame.math import Vector2

class Mercure:
    def __init__(self,largeur=1000, hauteur=800):
        self.nom = "Mercure"
        self.position = Vector2(100, hauteur/2)
        self.rayon = 3
        self.masse = 0.378
        self.couleur = (236, 255, 51)


        def repulsion(self):
            pass