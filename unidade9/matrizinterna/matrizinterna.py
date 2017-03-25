# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG
########################################################################

def soma_matriz_interna(M,p1, p2):
	l1, c1 = p1[0], p1[1]
	l2, c2 = p2[0], p2[1]
	soma = 0
	
	for i in range(l1, l2+1):
		for j in range(c1 , c2+1):
			soma += M[i][j]
	
	return soma
	
M2 = [ [1, 2, 3],
       [4, 5, 6], 
       [7, 8, 9] ]

assert soma_matriz_interna(M2, (1,1),(2,2)) == 5 + 6 + 8 + 9
