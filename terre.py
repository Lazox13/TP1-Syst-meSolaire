import random

from pygame.math import Vector2

class Terre:
    def __init__(self,largeur=1000, hauteur=800):
        self.nom = "Terre"
        self.position = Vector2(300, hauteur/2)
        self.rayon = 3
        self.masse = 1
        self.couleur = (236, 255, 51)


        def repulsion(self):
            pass