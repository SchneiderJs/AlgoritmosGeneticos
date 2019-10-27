# -*- coding: utf-8 -*-
import random
from math import sqrt
import matplotlib.pyplot as plt


distancia_euclidiana = lambda p1, p2: sqrt(pow(coordenadas['x'][p2]-coordenadas['x'][p1], 2) + pow(coordenadas['y'][p2]-coordenadas['y'][p1], 2))

def obter_distancias():
	"""Esta função calcula as distâncias entre todas as cidades

	Retorna
	-------
		list de floats
			Uma lista contendo a distância de qualquer ponto até qualquer outro
			ponto
	"""
	distancias = []
	for i in range(20):
		aux = []
		for j in range(20):
			aux.append(distancia_euclidiana(i, j))
		distancias.append(aux)

	return distancias

def obter_distancia_total(cromossomo, distancias):
	"""Esta função calcula a distância para se percorer as cidades
	indicadas pelo cromossomo

	Parâmetros
	----------
		cromossomo : lista de ints
			Uma lista contendo a ordem em que se deve percorrer as cidades
		distancias : lista de floats
			Uma lista contendo a distância entre as cidades
	Retornos
	--------
		float
			Retorna o custo total para passar por todas as cidades e retorna a
			origem
	"""
	x = 0
	for i in range(len(cromossomo)-1):
		x += distancias[cromossomo[i]][cromossomo[i+1]]
	# Adiciona a distância para retornar a cidade inicial
	x += distancias[cromossomo[-1]][cromossomo[0]]

	return x

def gerar_cromossomo(distancias):
	"""Esta função gera um cromossomo com a ordem que as cidades
	devem ser percorridas e a distância total do percurso

	Parâmetros
	----------
		distancias : list de floats
			Uma lista contendo a distância entre as cidades

	Retornos
	--------
		tuple
			Retorna uma tuple onde o primeiro elemento é a ordem em que as
			cidades devem ser percorridas e o segundo elemento é a distância
			total do caminho
	"""
	# lista aleatória sem números duplicados
	cromossomo = random.sample(range(20), 20)
	distancia = obter_distancia_total(cromossomo, distancias)
	return (cromossomo, distancia)


# Criação das coordenadas das cidades
random_int_x = random.sample(range(0, 100), 20) # coordenada x
random_int_y = random.sample(range(0, 100), 20) # coordenada y
coordenadas = {'x': [x/100 for x in random_int_x], 'y': [y/100 for y in random_int_y]} # dict de coordenadas

# Criação da matriz de adjacências
distancias  = obter_distancias()  # matrix de adjacência
populacao = [gerar_cromossomo(distancias) for i in range(20)] # todos os cromossomos com a distancia total do caminho

# Ordenar a população
populacao = sorted(populacao, key= lambda s: s[1])

# Roleta - Gerar
roleta = []
for i in range(10):
	roleta += [(i)]*(10-i)

# ------------------------- Cruzamento -------------------------------------
def cycle(paiA, paiB):
	"""Esta função faz o cruzamento entre o pai "a" e "b" e retorna dois
	novos cromossomos

	Parâmetros
	----------
		paiA, paiB : list de ints
			Uma lista contendo a ordem em que as cidades devem ser percorridas

	Retornos
	--------
		list
			Retorna uma lista contendon dois novos cromossomos
	"""
	def trocar(index):
		"""Esta função realiza a troca dos genes do pai "a" e "b" indicados pelo
		índice

		Parâmetros
		----------
			index : int
				O índice que deve ser utilizado na troca dos genes
		"""
		aux = paiA[index]
		paiA[index] = paiB[index]
		paiB[index] = aux


	def verificar_duplicados():
		"""Esta função verifica se o cromossomo pai "a" possui genes duplicados

		Retornos
		--------
			boolean
				Caso o pai "a" possua genes repetidos a função retorna "True" senão
				ela retorna "False"
		"""
		for i in range(len(paiA) - 1):
			for j in range(i + 1, len(paiA)):
				if paiA[i] == paiA[j]:
					return True
		return False

	def passo1():
		"""Esta função escolhe aleatoriamente um gene para ser trocado entre
		o pai "a" e "b" e realiza a troca

		Retornos
		--------
			int
				O índice do gene que foi efetuado a troca
		"""
		index = random.choice(list(range(20)))
		trocar(index)
		return index

	def passo2(index):
		"""Esta função realiza uma troca de genes entre os cromossomos pai "a"
		e "b", o índice da troca é definido pelo gene repetido no pai "a"

		Parâmetros
		----------
			index : int
				O valor do índice em que se ocorreu a última troca

		Retornos
		--------
			int
				Retorna o índice em que foi efetuado a troca
		"""
		if paiA[index] == paiB[index]:
			return
		for idx, a in enumerate(paiA):
			if paiA[index] == a and idx != index:
				trocar(idx)
				index = idx
				break
		return idx

	def passo3(index):
		"""Esta função realiza a troca de genes até que o cromossomo pai "a"
		não possua mais genes repetidos

		Parâmetros
		----------
			index : int
				O índice em que foi efetuado a última troca

		Retornos
		--------
			list
				Retorna dois novos cromossomos que surgiram a partir do
				cruzamento do pai "a" e "b"
		"""
		# Enquanto o pai "a" tiver genes repetidos, troca genes com o pai "b"
		while verificar_duplicados():
			index = passo2(index)
		return paiA, paiB

	idx = passo1()
	idx = passo2(idx)
	return passo3(idx)

def mutacao(filho):
	"""Esta função realiza a mutação no cromossomo filho. A mutação
	consiste em inverter o valores de dois índices selecionados aleatoriamente

	Parâmetros
	----------
		filho : list de ints
			Um cromossomo ou lista da ordem em que as cidades devem ser
			percorridas

	Retornos
	--------
		list de int
			Retorna o cromossomo mutado ou a lista das cidades na ordem em que
			devem ser percorridas

	"""
	# Escolhe dois genes para inverter no cromossomo
	lista = list(range(19))
	index_1 = random.choice(lista)
	lista.remove(index_1)
	index_2 = random.choice(lista)

	aux = filho[index_1]
	filho[index_1] = filho[index_2]
	filho[index_2] = aux

	return filho


def gerar_geracao(populacao):
	"""Está função realiza a execução do algoritmo genético a partir de
	uma população passada por parâmetro

	Parâmetros
	----------
		populacao : list de tuple
			Uma lista contendo as tuples, cada tuple contém um cromossomo e o
			custo total do caminho a ser percorrido

	Retornos
	--------
		list
			Retorna uma lista com a nova população, a quantidade de
			indivíduos gerados e a quantidade dos indivíduos que foram mutados

	"""
	qtdMutacoes = 0
	populacao_gerada = 0

	# Roleta - Sortear
	sorteadosA = [random.choice(roleta) for i in range(5)]
	sorteadosB = [random.choice(roleta) for i in range(5)]

	filhos = []
	for paiA, paiB in zip(sorteadosA, sorteadosB):
		# Realiza o cruzamento
		filho_a, filho_b = cycle(populacao[paiA][0], populacao[paiB][0])

		populacao_gerada += 2

		# Aplica mutação se pm for menor ou igual a 5
		pm = random.randint(1, 100)
		if pm <= 5:
			filho_a = mutacao(filho_a)
			qtdMutacoes += 1

		pm = random.randint(1, 100)
		if pm <= 5:
			filho_b = mutacao(filho_b)
			qtdMutacoes += 1

        # Encapsula os cromossomos em uma tupla
		filho_a = (filho_a, obter_distancia_total(filho_a, distancias))
		filho_b = (filho_b, obter_distancia_total(filho_b, distancias))

		filhos.append(filho_a)
		filhos.append(filho_b)

    # Substitui os 10 ultimos cromossomos pelos 10 novos filhos
	populacao = populacao[:10]
	for f in filhos:
		populacao.append(f)

	# Ordena a populção com os novos cromossomos
	populacao = sorted(populacao, key= lambda s: s[1])

	return populacao, populacao_gerada, qtdMutacoes

print()
for i in populacao:
	print(i)

qtdMutacoes, pop_g = 0, 0
# Aplica o algoritmo genético com o critério de parada de 10000
# repetições
for i in range(10000):
	populacao, qtdPopulacaoGerada, mutacoes = gerar_geracao(populacao)
	qtdMutacoes += mutacoes
	pop_g += qtdPopulacaoGerada

print()
for i in populacao:
	print(i)


print("Populacao inicial: " + str(len(populacao)))
print("Populacao gerada: " + str(pop_g))
print("Tamanho da população: " + str(len(populacao) + pop_g))
print("Taxa de mutação: " + str((qtdMutacoes/pop_g)*100) + "%")
print("Numero de cidades: " + str(len(populacao[0][0])))
print("Melhor custo: " + str(populacao[0][1]))
print("Melhor solução: " + str(populacao[0][0]))


#plotar
cord_x = []
cord_y = []
for city in populacao[0][0]:
	cord_x.append(coordenadas['x'][city])
	cord_y.append(coordenadas['y'][city])

ax = plt.subplot(111)
ax.set_xlabel("Coordenada X", fontsize = 10)
ax.set_ylabel("Coordenada Y", fontsize = 10)
ax.set_title("Percurso das cidades", fontsize = 15)
ax.scatter(cord_x, cord_y, s = 30, color = "black", marker = "X")


cord_x.append(cord_x[0])
cord_y.append(cord_y[0])
# Liga as cidades
plt.plot(cord_x, cord_y, color = "purple", linestyle="solid", linewidth=1)

# Exibe o nome das cidades no gráfico
for index, city in enumerate(populacao[0][0]):
	ax.annotate(city, (cord_x[index], cord_y[index]), color="r")

plt.show()
