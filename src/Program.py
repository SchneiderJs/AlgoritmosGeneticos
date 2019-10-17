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
random_int_x = random.sample(range(0, 100), 20) # coordenada x
random_int_y = random.sample(range(0, 100), 20) # coordenada y
coordenadas = {'x': [x/100 for x in random_int_x], 'y': [y/100 for y in random_int_y]} # dict de coordenadas

# Criacao da matriz de adjacencias
distancias  = obter_distancias()  # matrix de adjacencia
populacao = [gerar_cromossomo(distancias) for i in range(20)] # todos os cromossomos com a distancia total do caminho

# Ordenar a população
populacao = sorted(populacao, key= lambda s: s[1])

# Roleta - Gerar
roleta = []
for i in range(10):
	roleta += [(i)]*(10-i)
#print(roleta)

# ------------------------- Cruzamento -------------------------------------  
# Roleta - Sortear
sorteadosA = [random.choice(roleta) for i in range(5)]
sorteadosB = [random.choice(roleta) for i in range(5)]

print(sorteadosA)
print(sorteadosB)

def cycle(paiA, paiB):
	def trocar(index):
		print("pai   a: " + str(paiA))
		print("pai   b: " + str(paiB))
		print()
		aux = paiA[index]
		paiA[index] = paiB[index]
		paiB[index] = aux


	def verificar_duplicados():
		for i in range(len(paiA) - 1):
			for j in range(i + 1, len(paiA)):
				if paiA[i] == paiA[j]:
					return True
		return False

	def passo1():
		index = random.choice(list(range(19)))
		index = 0
		print("indice: " + str(index))
		trocar(index)
		return index

	def passo2(index):
		if paiA[index] == paiB[index]:
			return
		for idx, a in enumerate(paiA):
			if paiA[index] == a and idx != index:
				trocar(idx)
				index = idx
				break
		return idx

	def passo3(index):
		while verificar_duplicados():
			index = passo2(index)
		return paiA, paiB

	idx = passo1()
	idx = passo2(idx)
	return passo3(idx)

#print(populacao[sorteadosA[0]][0])
filho_a, filho_b = cycle(populacao[sorteadosA[0]][0], populacao[sorteadosB[0]][0])

print("filho a: " + str(filho_a))
print("filho b: " + str(filho_b))