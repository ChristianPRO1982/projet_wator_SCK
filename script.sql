SELECT * FROM simulation

SELECT * FROM simulation_evolution

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