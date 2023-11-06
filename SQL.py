import sqlite3

'''
INITIALISATION DE LA BASE DE DONNEES

DROP TABLE IF EXISTS `simulation`;
DROP TABLE IF EXISTS `simulation_evolution`;

CREATE TABLE simulation (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	date TIMESTAMP,
	largeur_monde INTEGER,
	hauteur_monde INTEGER,
	temps_reproduction_poisson INTEGER,
	temps_reproduction_requin INTEGER,
	temps_energie_requin INTEGER,
	nb_poissons_init INTEGER,
	nb_requins_init INTEGER,
	chronon INTEGER,
	chronon_stop INTEGER,
	nb_poisson_fin INTEGER,
	nb_requin_fin INTEGER,
	nb_eau_fin INTEGER
);

CREATE TABLE simulation_evolution (
	ID INTEGER,
	tour INTEGER,
	nb_poisson INTEGER,
	nb_requin INTEGER,
	nb_eau INTEGER,
	CONSTRAINT NewTable_PK PRIMARY KEY (ID,tour)
);
'''

con = sqlite3.connect("wa-tor")
cur = con.cursor()

# ⬆️➡️⬇️⬅️
# Noir : \033[30m
# Rouge : \033[31m
# Vert : \033[32m
# Jaune : \033[33m
# Bleu : \033[34m
# Magenta : \033[35m
# Cyan : \033[36m
# Blanc : \033[37m

def query_error(query: str):
    print("")
    print("/!\\")
    print("La requête suivant n'a pas pu être exécutée : ", query)
    print("/!\\")
    print("")


def new_simulation(monde,
                   chronon,
                   chronon_stop,
                   nb_eau_fin):
    query = f'''
INSERT INTO simulation (date,
                        largeur_monde,
                        hauteur_monde,
                        temps_reproduction_poisson,
                        temps_reproduction_requin,
                        temps_energie_requin,
                        nb_poissons_init,
                        nb_requins_init,
                        chronon,
                        chronon_stop,
                        nb_poisson_fin,
                        nb_requin_fin,
                        nb_eau_fin)
     VALUES (DATETIME('NOW'),
             {monde.largeur_monde},
             {monde.hauteur_monde},
             {monde.temps_reproduction_poisson},
             {monde.temps_reproduction_requin},
             {monde.temps_energie_requin},
             {monde.nb_poissons_init},
             {monde.nb_requins_init},
             {chronon},
             {chronon_stop},
             {monde.nb_animal('P')},
             {monde.nb_animal('R')},
             {nb_eau_fin})'''

    try:
        cur.execute(query)
        con.commit()

    except:
        query_error(query)


def new_simulation_evolution(etat_du_monde):
    ID_max = IDmax()
    virgule = ""

    query = 'INSERT INTO simulation_evolution VALUES'
    
    for etat in etat_du_monde:
        # on crée un enregistrement par état du monde (par chronon)
        query += virgule + f' ({ID_max}, {etat[0]}, {etat[1]}, {etat[2]}, {etat[3]})'
        virgule = ", "

    try:
        cur.execute(query)
        con.commit()

    except:
        query_error(query)


def spaces(string: str, length: int) -> str:
    str_return = str(string)

    for i in range(len(str_return), length):
        str_return += "-"
    return str_return


def IDmax() -> int:
    # permet de connaitre l'ID du dernier enregistrement dans la table `simulation`

    query = f'''
SELECT MAX(ID) FROM simulation;'''

    try:
        cur.execute(query)
        res = cur.fetchone()
        
        IDmax = res[0]

    except:
        query_error(query)
    
    return IDmax


def graph_valeur_max(graphID: int):
    # on récupère les données du graphique demandé

    query = f'''
SELECT MAX(se.tour) nb_valeur, MAX(MAX(se.nb_poisson), MAX(se.nb_requin)) max_valeur
  FROM simulation_evolution se 
 WHERE se.ID = {graphID};'''

    try:
        cur.execute(query)
        res = cur.fetchone()
        
        return res[0], res[1]

    except:
        query_error(query)
    
    return IDmax


def graph_valeurs(graphID: int):
    # on récupère les données du graphique demandé

    query = f'''
SELECT se.nb_poisson, se.nb_requin, se.nb_eau
  FROM simulation_evolution se 
 WHERE se.ID = {graphID}
 ORDER BY se.tour;'''

    try:
        cur.execute(query)
        res = cur.fetchall()
        
        return res

    except:
        query_error(query)
    
    return IDmax