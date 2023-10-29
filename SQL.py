import sqlite3

'''
INITIALISATION DE LA BASE DE DONNEES
DROP TABLE IF EXISTS `simulation`;

CREATE TABLE simulation (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	date TIMESTAMP,
	largeur_monde INTEGER,
	hauteur_monde INTEGER,
	temps_reproduction_poisson INTEGER,
	temps_reproduction_poisson_max INTEGER,
	temps_reproduction_requin INTEGER,
	temps_reproduction_requin_max INTEGER,
	temps_energie_requin INTEGER,
	temps_energie_requin_max INTEGER,
	nb_poissons_init INTEGER,
	nb_poissons_max INTEGER,
	nb_requins_init INTEGER,
	nb_requins_max INTEGER,
	chronon INTEGER,
	chronon_stop INTEGER,
	nb_poisson_fin INTEGER,
	nb_requin_fin INTEGER,
	nb_eau_fin INTEGER
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


def new_simulation(
                   date,
                   largeur_monde,
                   hauteur_monde,
                   temps_reproduction_poisson,
                   temps_reproduction_poisson_max,
                   temps_reproduction_requin,
                   temps_reproduction_requin_max,
                   temps_energie_requin,
                   temps_energie_requin_max,
                   nb_poissons_init,
                   nb_poissons_max,
                   nb_requins_init,
                   nb_requins_max,
                   chronon,
                   chronon_stop,
                   nb_poisson_fin,
                   nb_requin_fin,
                   nb_eau_fin):
    query = f'''
INSERT INTO user (date,
                  largeur_monde,
                  hauteur_monde,
                  temps_reproduction_poisson,
                  temps_reproduction_poisson_max,
                  temps_reproduction_requin,
                  temps_reproduction_requin_max,
                  temps_energie_requin,
                  temps_energie_requin_max,
                  nb_poissons_init,
                  nb_poissons_max,
                  nb_requins_init,
                  nb_requins_max,
                  chronon,
                  chronon_stop,
                  nb_poisson_fin,
                  nb_requin_fin,
                  nb_eau_fin)
     VALUES ("{username}",
             "{largeur_monde}",
             "{hauteur_monde}",
             "{temps_reproduction_poisson}",
             "{temps_reproduction_poisson_max}",
             "{temps_reproduction_requin}",
             "{temps_reproduction_requin_max}",
             "{temps_energie_requin}",
             "{temps_energie_requin_max}",
             "{nb_poissons_init}",
             "{nb_poissons_max}",
             "{nb_requins_init}",
             "{nb_requins_max}",
             "{chronon}",
             "{chronon_stop}",
             "{nb_poisson_fin}",
             "{nb_requin_fin}",
             "{nb_eau_fin}")'''
    
    cur.execute(query)
    con.commit()


def list_user():
    print(spaces("ID",5), spaces("UserName",15), spaces("Prénom",15), spaces("Nom",15), spaces("Age", 3), spaces("Courriel",20), spaces("Adresse",30))
    print("")

    query = 'SELECT * FROM user'

    res = cur.execute(query)
    res = res.fetchall()

    for user in res:
        print(spaces(user[0],5), spaces(user[1],15), spaces(user[2],15), spaces(user[3], 15), spaces(user[4],3), spaces(user[5],20), spaces(user[6],30))


def spaces(string: str, length: int) -> str:
    str_return = str(string)

    for i in range(len(str_return), length):
        str_return += "-"
    return str_return


def bmi_analysis(user_id: int):
    print("")

    query = f'''
SELECT u.first_name || " " || u.last_name name, u.age, b.weight, b.height, b.bmi_value,
       CASE 
           WHEN b.bmi_value < ROUND(ba.bmi_min * 17 / 19) THEN '\033[1;31;40mdénutrition\033[1;37;40m'
           WHEN b.bmi_value >= ROUND(ba.bmi_min * 17 / 19) AND b.bmi_value < ba.bmi_min THEN '\033[1;34;40mmaigreur\033[1;37;40m'
           WHEN b.bmi_value >= ba.bmi_min AND b.bmi_value <= ba.bmi_max THEN '\033[1;32;40mcorpulence normale\033[1;37;40m'
           WHEN b.bmi_value > ba.bmi_max AND b.bmi_value < ROUND(ba.bmi_max * 30 / 24) THEN '\033[1;33;40msurpoids\033[1;37;40m'
           WHEN b.bmi_value >= ROUND(ba.bmi_max * 30 / 24) AND b.bmi_value < ROUND(ba.bmi_max * 35 / 24) THEN '\033[1;34;40mobésité modérée\033[1;37;40m'
           WHEN b.bmi_value >= ROUND(ba.bmi_max * 35 / 24) AND b.bmi_value < ROUND(ba.bmi_max * 40 / 24) THEN '\033[1;34;40mobésité sévère\033[1;37;40m'
           WHEN b.bmi_value >= ROUND(ba.bmi_max * 40 / 24) THEN '\033[1;35;40mobésité morbide\033[1;37;40m'
       END AS 'BMI',
       STRFTIME('%d/%m/%Y %H:%M', MAX(b.date_recorded)) date_recorded
  FROM user u
  JOIN bmi b ON u.user_id = b.user_id
  JOIN bmi_analysis ba ON u.age BETWEEN ba.age_min AND ba.age_max
 WHERE b.user_id = {user_id}
 GROUP BY b.user_id'''

    try:
        cur.execute(query)
        res = cur.fetchone()
        
        if res:
            print("Analyse des dernières données en date pour l'utilisateur", res[0], "au", res[6])
            print(f"Données utilisées : âge={res[1]} ans / taille={res[3]} cm / poids={res[2]}")
            print(f"L'IMC est de {res[4]} ; ce qui correspond à un(e) '{res[5]}'.")
            print("")
        else:
            print("Attention, l'âge de cet utilisateur n'est pas >= 19 ans. L'analyse ne peut pas être effectuée.")

    except:
        query_error(query)