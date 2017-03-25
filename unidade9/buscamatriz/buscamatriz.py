# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Busca em Matriz
########################################################################

def busca_matriz(m, e):
	indice = None

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):	
			if matriz[i][j] == e:
				indice = (i,j)
				return indice

matriz = [[2, 3, 5, 3, 1],[3, 2, 1, 5, 6],[1, 2, 3, 2, 1],]

assert busca_matriz(matriz, 4) == None
assert busca_matriz(matriz, 3) == (0,1)
assert busca_matriz(matriz, 1) == (0,4)
