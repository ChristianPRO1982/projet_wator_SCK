-- simulation definition

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