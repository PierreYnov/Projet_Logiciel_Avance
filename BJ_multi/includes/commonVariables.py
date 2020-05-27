
class InitCommonVariables:
    """
    Instanciation de la classe va créer un Singleton contenant toute les variables
    de bases qui seront passées par référence entre le fichier blackjack.py et les 
    différents fichiers gameFSM.py.

    """
    _instance = None

    @classmethod
    def get_instance(cls):
        """

        Si la variable _instace est None alors on va l'instancier et returner cette
        instance, sinon on return cette instance déjà existante. On utilise le 
        décorateur @classmethod pour indiquer que la fonction get_instance est une
        méthode de classe et non d'instance.

        """
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
