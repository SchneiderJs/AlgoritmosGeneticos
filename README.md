# Trabalho sobre Algoritmos Genéticos
Aplicação de algoritmos genéticos em um grafo completo contendo 20 vértices.

## Estruturas de dados:
Cromossomos: lista contendo tuplas de caminho e distância total. Cada caminho representa um cromossomo;

Coordenadas: dicionário contendo uma lista para as coordenadas x e uma lista para as coordenadas y;

Distâncias: estrutura auxiliar para reduzir o custo computacional, consiste em uma matriz 20x20 com as distâncias entre os respectivos nós (matriz de adjacência).

## Passos:
1. Gerar as coordenadas de cada cidade aleatóriamente, entre zero e um.
2. Gerar a matriz de adjacência.
3. Criar uma matriz de cromossomos com caminhos aleatórios.
3.1 Ao calcular a distancia total, deve ser somado a distancia da ultima cidade para a primeira pois o caminho deve retornar a origem.
4. Ordenar a matriz conforme a soma das distâncias;
5. Desconsiderar os 10 ultimos cromossomos.
6. Realizar a mutaçao ...
