# Blackjack en multijoueur

_Dans le cadre du projet 2020 UF Développement Logiciel et Base de données, nous réalisons une version multijoueur du Blackjack en python accessible depuis une interface client avec la possiblité de créer son utilisateur._

_Réalisé par DUMONT Thomas **[@akhadimer](https://github.com/akhadimer)**, CEBERIO Pierre **[@PierreYnov](https://github.com/PierreYnov)** et LABORDE Simon **[@Genisys33](https://github.com/Genisys33)**._

## Sommaire 

- [I. Présentation du sujet](#i-Présentation-du-sujet)
    - [1. Le contexte](###1.-Le-contexte)
    - [2. Problématique](###2.-Problématique)
- [II. Présentation du projet](#ii-Présentation-du-projet)
    - [1. Le projet](###1.-Le-projet)
    - [2. Les choix technologiques](###2.-Les-choiX-technologiques)
    - [3. Caractéristiques nécessaires](###3.-Caractéristiques-nécessaires)
- [III. Guide d'installation et d'utilisation du projet](#iii-Guide-d'installation-et-d'utilisation-du-projet)
- [IV. Pour aller plus loin](#iv-Pour-aller-plus-loin)
- [VI. Crédits](##-vi-crédits)



## I. Présentation du sujet    
### 1. Le contexte

Cadre du projet :

-- <cite>Ce projet permet l’évaluation des compétences acquises grâce aux modules de l’UF
« Développement Logiciels » et « Base de données ». Pour ce faire, ce projet devra être réalisé
en groupe de 2 ou 3, dans le langage que nous souhaitons et devra être basé sur un serveur de matchmaking.</cite>

Nous sommes un groupe de 3 et nous avons décidé de partir sur la création d'un jeu bien connu : le Blackjack.

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
    * Arrivé d'un client dans la file d'attente
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

* Plateau avec une partie lancée et les jetons misés
    ![](https://i.ibb.co/9rgKCMh/2-bj.png)

* Plateau avec le croupier qui a gagné la partie
    ![](https://i.ibb.co/m8WWh4S/3-bj.png)

* Plateau avec le joueur qui a gagné la partie
    ![](https://i.ibb.co/Fm3Zv5K/4-bj.png)

### 2. Les choix technologiques

* Langage python
* Librairie "Pygame" afin de facilité la création graphique du jeu
* Hébergement sur le serveur de Simon ( 250GO et 4GO de RAM, largement suffisant pour ce projet)

### 3. Caractéristiques nécessaires 

* 7 clients maximum par table
* Les interactions Client > Serveur : 
    - Mise avec le montant
    - Doubler
    - Tirer une carte, 
    - Split
    - Fin de tour (Stand)
* Les interactions Serveur > Client : 
    - Envoi d'une carte avec couleur + valeur
    - Envoi de 2 cartes avec c1v1 et c2v2, 
    - Ajout de 1 carte au joueur avec sa position ( en tant que joueur sur la table) avec sa couleur + valeur
    - Ajout de 2 cartes au joueur avec sa position ( en tant que joueur sur la table) avec leurs couleusr + valeurs
    - Croupier tire une carte avec sa couleur et valeur
    - Fin de tour
* Architecture et communication entre les threads

![](https://i.ibb.co/ZX3Ncmq/Sans-titre.png)

Les 7 clients ne discutent pas entre eux.
Le(s) client(s) et le croupier ne discute(nt) pas ensemble mais il(s) discute(nt) avec trois threads.

Le premier étant le deck, il répond aux messages de type " tire une nouvelle carte "pour le croupier ou/et le(s) client(s).

Le deuxième s'occupe d'envoyer les cartes à ceux le demandant, exemple : "Client 2 tire une carte", ce thread le sait et va envoyer à tous les autres clients la nouvelle carte que Client2 a tiré.

Le troisième s'occupe de la logique de jeu, pour savoir qui a gagné, perdu ou push par rapport au croupier.

## III. Guide d'installation et d'utilisation du projet

* Cloner le repository avec la commande: `git clone https://github.com/PierreYnov/Projet_Logiciel_Avance.git`.
* Pour le solo :
    * Se placer avec un terminal dans le dossier Blackjack, installer les librairies suivante avec pip : `pygame, tkinter, subprocess, socket et thread`
    * Faire la commande `py blackjack.py`
* Pour le multijoueur :
    * en cours de dév ( `server.py` déjà prêt avec le système d'écoute, `connexion.py` prêt avec la possibilité de s'inscrire puis de se connecter pour lancer le menu `start.py`)

## IV. Pour aller plus loin
- Finir le multijoueur
- Régler les problèmes d'encodage
- Alimenter les crédits par un système de paiement avec de l'argent réel
- Gestion utilisateur plus grande pour les joueurs (Exemple : Ajout avatar)
- Ajout d'un chat : Système de discussion pendant la partie entre les joueurs
- Log des plus gros gains effectués sur la table pour pouvoir les montrer sur un podium des 3 meilleurs joueurs
## VI. Crédits
- Blackjack solo: https://github.com/torbjornhedqvist/blackjack
- Python: https://www.python.org/
