import random
from math import sqrt

distancia_euclidiana = lambda p1, p2: sqrt(pow(coordenadas['x'][p2] - coordenadas['x'][p1], 2) + pow(coordenadas['y'][p2] - coordenadas['y'][p1], 2))

def obter_distancias():
	distancias = []
	for i in range(20):
		aux = []
		for j in range(20):
			aux.append(distancia_euclidiana(i, j))
		distancias.append(aux)

	return distancias

def obter_distancia_total(cromossomo, distancias):
	x = 0
	for i in range(len(cromossomo)-1):
		x += distancias[cromossomo[i]][cromossomo[i+1]]
	x += distancias[cromossomo[-1]][cromossomo[0]]
	
	return x

def gerar_cromossomo(distancias):
	# lista aleatória sem numeros duplicados 
	cromossomo = random.sample(range(20), 20)
	distancia = obter_distancia_total(cromossomo, distancias)
	return (cromossomo, distancia)

# Criacao das coordenadas das cidades
random_int_x = random.sample(range(0, 100), 20)
random_int_y = random.sample(range(0, 100), 20)
coordenadas = {'x': [x/100 for x in random_int_x], 'y': [y/100 for y in random_int_y]}

# Criacao da matriz de adjacencias
distancias  = obter_distancias()
print(gerar_cromossomo(distancias))