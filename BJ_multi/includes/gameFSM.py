"""

Utilisation du design pattern Finite State Machine, ce dernier
est avant tout un modèle mathématique abstrait qui est suceptible
d'avoir un nombre fini d'état (état perdu, gagné, bet, split, etc...)
mais à un moment donnée t aura un unique état. 

En programmation, cela consite à réaliser des classes d'états, des 
fonctions de transitions d'état, un état de départ et un état de fin.

"""


class State(object):
    """

    La classe "State" est la classe utilisé qui changera de comportement
    en fonction des actions faites.

    """

    def get_state(self):

    def new_state(self, state):
        self.__class__ = state


class PlayerInitState(State):
    def __init__(self, *args, **kwargs):
        return


class BetState(State):
    def __init__(self, *args, **kwargs):
        return


class FinalState(State):
    def __init__(self, *args, **kwargs):
        return
