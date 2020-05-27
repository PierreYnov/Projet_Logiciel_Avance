# Projet_Logiciel_Avance
Dumont Thomas

Ceberio Pierre

Laborde Simon

I. Présentation du sujet

1. Le contexte
2. Problématique

II. Présentation du projet

1. Le Projet
2. Les choix technologiques
3. Les problemes rencontrés

III. Guide d'installation et d'utilisation du projet

IV. Conclusion


## I. Présentation du sujet    
### 1. Le contexte

Ce projet permet l’évaluation des compétences acquises grâce aux modules de l’UF
« Développement Logiciels » et « Base de données ». Pour ce faire, ce projet devra être réalisé
en groupe de 2 ou 3, dans le langage que nous souhaitons et devra être basé sur un serveur de matchmaking.

Nous sommes un groupe de 3 personnes et nous avons décidé de partir sur la création d'un jeu bien connu : le Blackjack.

### 2. Problématique

Le jeu devra respecter plusieurs points :

* Pouvoir configurer son pseudo
* Une file d'attente avant de commencer une partie
* Pouvoir communiquer avec l'autre joueur
* Un plateau de jeu
* Message :
    * Lorsqu'un match se termine
    * Si le joueur a gagné
* Serveur matchmacking :
  * Un lien avec une base de donnée
  * Un système de socket avec :
    * Arrivé d'un clent dans file d'attente
    * Début d'un match
    * Réception d'un tour
    * Fin d'un match
  * Vérification file d'attente et création de matchs
* Logiciel client :
    * Entrée file d'attente
    * Début match
    * Relancer une carte ou arrêter
    * Prendre en compte la valeur de la main des joueurs et du croupier
    * Fin du match

## II. Présentation du projet
### 1. Le projet

* Plateau neutre
    ![](https://i.ibb.co/hD82498/1-bj.png)

* Plateau avec partie lancée et jeton misé
    ![](https://i.ibb.co/9rgKCMh/2-bj.png)

* Plateau avec le croupier détenant la victoire
    ![](https://i.ibb.co/m8WWh4S/3-bj.png)

* Plateau avec le joueur détenant la victoire
    ![](https://i.ibb.co/Fm3Zv5K/4-bj.png)

### 2. Les choix technologiques

* Langage python
* Librairie "Pygame" afin de facilité la création graphique du jeu
* Raspberry Pi afin d'héberger le jeu

### 3. Les problèmes rencontrés

* Intégration dynamique des joueurs sur le plateau selon le nombre de participants
* Intégration du matchmaking au projet afin que les joueurs puissent jouer ensemble

## III. Guide d'installation et d'utilisation du projet

* Télécharger ce répertoire GitHub
* Pour le solo :
    * Se placer avec un terminal dans le dossier Blackjack, installer les librairies suivante avec pip : pygame, tkinter, subprocess, socket et thread
    * Faire la commande `py blackjack.py`
* Pour le multijoueur :
    * Ne fonctionne pas