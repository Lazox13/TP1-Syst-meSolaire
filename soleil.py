import random

from pygame.math import Vector2

class Soleil:
    def __init__(self,largeur=1000, hauteur=800):
        self.nom = "Soleil"
        self.position = Vector2(400, hauteur/2)
        self.rayon = 3
        self.masse = 28
        self.couleur = (236, 255, 51)


        def repulsion(self):
            pass