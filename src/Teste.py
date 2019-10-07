import random
from math import sqrt

def distancia(p1, p2): 
	return sqrt(pow(coordenadas['x'][p2] - coordenadas['x'][p1], 2) + pow(coordenadas['y'][p2] - coordenadas['y'][p1], 2))

def obter_distancias():
	distancias = []
	for i in range(20):
		aux = []
		for j in range(20):
			aux.append(distancia(i, j))
		distancias.append(aux)

	return distancias

# Criacao das coordenadas das cidades
random_int_x = random.sample(range(0, 100), 20)
random_int_y = random.sample(range(0, 100), 20)
coordenadas = {'x': [x/100 for x in random_int_x], 'y': [y/100 for y in random_int_y]}

# Criacao da matriz de adjacencias
print(obter_distancias()[19])