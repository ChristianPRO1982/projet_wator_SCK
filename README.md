# Projet WA-TOR

Ce projet consiste en une simulation informatique de l'écosystème aquatique, également connue sous le nom de Projet Wa-Tor. Il comprend un ensemble de fichiers Python qui simulent divers aspects de l'écosystème aquatique, tels que les interactions entre poissons, requins, algues, rochers et eau. La simulation comprend également des mécanismes de reproduction, de déplacement et de gestion de l'énergie pour les différentes entités présentes dans l'écosystème.

## Structure du projet

Le projet est organisé en plusieurs fichiers Python, chacun étant responsable d'une partie spécifique de la simulation. Voici les principaux fichiers présents dans le projet :

- `main.py` : Ce fichier définit le fonctionnement générale. C'est une boucle permettant de faire la simulation.
- `monde.py` : Ce fichier définit la classe Monde, qui gère les aspects généraux de la simulation et contient les méthodes principales pour la gestion de l'écosystème.
- `poisson.py` : Ce fichier contient la définition de la classe Poisson, qui représente les entités de type poisson dans la simulation.
- `requin.py` : Ce fichier contient la définition de la classe Requin, qui représente les entités de type requin dans la simulation hérité de la class Poisson.
- `PG.py` : Ce fichier est responsable de la partie graphique de la simulation, qui utilise le module Pygame pour afficher visuellement l'état de l'écosystème en temps réel.
- `SQL.py` : Ce fichier est responsable de l'interaction avec la base de données SQLite, où les données de simulation sont stockées pour l'analyse ultérieure.
- `graphique.py` : Ce fichier utilise le module turtle pour générer des graphiques basés sur les données de simulation stockées dans la base de données.


## Paramètres de la simulation

Les paramètres de la simulation peuvent être ajustés dans le fichier de configuration `config.ini`. Voici quelques-uns des paramètres que vous pouvez personnaliser :

- Dimensions de la grille de la planète
- Nombre de rochers et d'algues
- Temps de reproduction pour les poissons et les requins
- Énergies pour le poisson et le requin cannibale
- Nombres initiaux de poissons et de requins
- Durée du jour et de la nuit
- Durée des saisons
- Simulation automatique
- Nombre de tours dans la simulation
- Vitesse d'affichage

## Initialisation des paramètres

Les paramètres peuvent être écris dans le fichier `monde.ini`

## Exécution du programme

Pour exécuter la simulation, assurez-vous d'avoir Python installé sur votre système. Ensuite, exécutez le script principal `main.py`. Vous pouvez également personnaliser les paramètres dans le fichier `monde.ini` pour adapter la simulation selon vos besoins.

## Afficher le graphique d'une simulation

Il faut connnaitre l'ID (voir en BDD)
Lancer le script `graphique.py`.

## Exécutions automatiques

Le paramètre `auto_simu` peut être à `0` ce qui lancera une seule simulation avec la partir graphique visible.
Le paramètre peut être à `1`, alors le programme lancera toutes les simulations possibles selon les paramètres du fichier `monde.ini` en utilisant les paramètres classiques et les paramètres liées finissant par `_max`.

## Installation

1. Assurez-vous d'avoir Python installé. Le projet a été développé en utilisant Python 3.
2. Installez la bibliothèque Pygame en utilisant la commande suivante :
 $ pip3 install pygame

## autres librairies utilisation
- os
- random
- time
- SQL
- turtle (pour les graphiques)

## Auteurs

Ce projet a été développé par Saif, Christian et Kévin.

N'hésitez pas à faire part de vos commentaires et suggestions pour améliorer la simulation.