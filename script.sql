SELECT chronon , nb_requin_fin  FROM simulation

SELECT * FROM simulation_evolution;

DELETE FROM simulation

DELETE FROM simulation_evolution


SELECT *
FROM simulation s 
WHERE chronon = (SELECT max(chronon) FROM simulation)

SELECT MAX(ID) FROM simulation s 

SELECT *
FROM simulation_evolution se 
WHERE ID = 15960