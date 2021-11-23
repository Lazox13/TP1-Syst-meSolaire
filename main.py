import pygame

import core
from Planetes.jupiter import Jupiter
from Planetes.mars import Mars
from Planetes.mercure import Mercure
from Planetes.neptune import Neptune
from Planetes.pluton import Pluton
from Planetes.saturne import Saturne
from Planetes.soleil import Soleil
from Planetes.terre import Terre
from Planetes.uranus import Uranus
from Planetes.venus import Venus


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1000, 800]

    core.memory("Soleil", Soleil())
    core.memory("tSoleil", [])
    core.memory("tSoleil").append(Soleil())

    core.memory("Mercure", Mercure())
    core.memory("tMercure", [])
    core.memory("tMercure").append(Mercure())

    core.memory("Vénus", Venus())
    core.memory("tVénus", [])
    core.memory("tVénus").append(Venus())

    core.memory("Terre", Terre())
    core.memory("tTerre", [])
    core.memory("tTerre").append(Terre())

    core.memory("Mars", Mars())
    core.memory("tMars", [])
    core.memory("tMars").append(Mars())

    core.memory("Jupiter", Jupiter())
    core.memory("tJupiter", [])
    core.memory("tJupiter").append(Jupiter())

    core.memory("Saturne", Saturne())
    core.memory("tSaturne", [])
    core.memory("tSaturne").append(Saturne())

    core.memory("Uranus", Uranus())
    core.memory("tUranus", [])
    core.memory("tUranus").append(Uranus())

    core.memory("Neptune", Neptune())
    core.memory("Neptune", [])
    core.memory("Neptune").append(Neptune())

    core.memory("Pluton", Pluton())
    core.memory("tPluton", [])
    core.memory("tPluton").append(Pluton())

    print("Setup END-----------")



def run():

    for s in core.memory("tSoleil"):
        pygame.draw.circle(core.screen, s.couleur, s.position, s.rayon)

    for mer in core.memory("tMercure"):
        pygame.draw.circle(core.screen, mer.couleur, mer.position, mer.rayon)

    for v in core.memory("tVénus"):
        pygame.draw.circle(core.screen, v.couleur, v.position, v.rayon)


core.main(setup, run)