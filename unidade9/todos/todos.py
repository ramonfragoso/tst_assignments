# coding: utf-8
# José Ramon Fragoso da Silva - 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Busca Todos em Matriz
########################################################################

def busca_matriz(m, e):
	indices = []
	
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == e:
				indices.append((i, j))
	
	return indices
				
				
