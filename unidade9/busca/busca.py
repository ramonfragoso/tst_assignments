# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Busca por coluna
########################################################################

def busca_todos_por_coluna_em_matriz(m, e):
	indices = []

	for i in range(len(matriz[0])):
		indiceatual = []
		for j in range(len(matriz)):	
			if matriz[j][i] == e:
				indiceatual = (j,i)
				indices.append(indiceatual)
				
	return indices

matriz = [
    [2, 3, 5, 3, 1],
    [3, 2, 1, 5, 6],
    [3, 2, 3, 2, 1],]
    
assert busca_todos_por_coluna_em_matriz(matriz, 4) == []
assert busca_todos_por_coluna_em_matriz(matriz, 3) == [(1,0), (2,0), (0,1), (2,2), (0,3)]
assert busca_todos_por_coluna_em_matriz(matriz, 1) == [(1,2), (0,4), (2,4)]
