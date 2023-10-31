import turtle
import SQL

# Initialiser la fenêtre graphique
screen = turtle.Screen()
screen.title("Graphique avec turtle")
screen.setup(850, 650)  # Définir la taille de la fenêtre graphique

canva = turtle.Turtle()
canva.speed(0)
canva.hideturtle()

# global largeur_valeur
# global hauteur_valeur

def init(nb_valeur: int, max_valeur: int):
    global largeur_valeur
    global hauteur_valeur
    largeur_valeur = 1
    hauteur_valeur = 1

    # dessin des abscisse et ordonnée
    ligne(0, 0, 800, 0, "black")
    canva.write(str(nb_valeur))
    ligne(0, 0, 0, 600, "black")
    canva.write(str(max_valeur))

    # MAJ des distances entre les points
    largeur_valeur = 800 / nb_valeur
    hauteur_valeur = 600 / max_valeur

def ligne(x1: int, y1: int, x2: int, y2: int, couleur: str):
    # cas du premier point
    if x1 < -1000:
        x1 = x2
        y1 = y2

    # dessin de la ligne
    canva.penup()
    canva.color(couleur)
    canva.goto(x1 * largeur_valeur - 400, y1 * hauteur_valeur - 300)
    canva.pendown()
    canva.goto(x2 * largeur_valeur - 400, y2 * hauteur_valeur - 300)

def choix_graphique() -> int:
    graphID = int(input("ID du graphique à afficher : "))
    # graphID = 6
    nb_valeur, max_valeur = SQL.graph_valeur_max(graphID)
    init(nb_valeur, max_valeur)
    return graphID

# initialisation
graphID = choix_graphique()
valeurs_total = SQL.graph_valeurs(graphID)

# affichage de tous les valeurs
mem_poisson = [-10000,0]
mem_requin = [-10000,0]
mem_eau = [-10000,0]
for valeurs in valeurs_total:
    # affichage de la valeur pour "poisson"
    ligne(mem_poisson[0], mem_poisson[1], mem_poisson[0] + 1, valeurs[0], "green")
    if mem_poisson[0] < -1000:
        mem_poisson[0] = 0
    mem_poisson[0] += 1
    mem_poisson[1] = valeurs[0]

    # affichage de la valeur pour "requin"
    ligne(mem_requin[0], mem_requin[1], mem_requin[0] + 1, valeurs[1], "red")
    if mem_requin[0] < -1000:
        mem_requin[0] = 0
    mem_requin[0] += 1
    mem_requin[1] = valeurs[1]

    # affichage de la valeur pour "eau"
    ligne(mem_eau[0], mem_eau[1], mem_eau[0] + 1, valeurs[2], "blue")
    if mem_eau[0] < -1000:
        mem_eau[0] = 0
    mem_eau[0] += 1
    mem_eau[1] = valeurs[2]

turtle.done()