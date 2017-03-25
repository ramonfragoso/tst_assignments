# coding: utf-8
# José Ramon Fragoso da Silva - 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Zera nao-nulos
########################################################################

def zera_nao_nulos(jogo, l, c):
	
	if jogo[l][c] == 0:
		return jogo
	
	# zera linha pela direita
	for i in range(len(jogo)):
		for j in range(len(jogo[i])):
			if i == l and j >= c:
				if jogo[i][j] == 0: break
				else:
					jogo[i][j] = 0
	
	# zera linha pela esquerda
	for i in range(len(jogo)):
		for j in range(len(jogo), -1, -1):
			if i == l and j < c:
				if jogo[i][j] == 0: break
				else:
					jogo[i][j] = 0
		
	# zera de cima pra baixo	
	for i in range(len(jogo)):
		for j in range(len(jogo[i])):
			if i == c and j > l:
				if jogo[j][i] == 0: break
				else:
					jogo[j][i] = 0

	# zera de baixo pra cima								
	for i in range(len(jogo)):
		for j in range(len(jogo[i])-1, -1, -1):
			if i == c and j < l:
				if jogo[j][i] == 0: break
				else:
					jogo[j][i] = 0
	
	
	return jogo
			
	
jogo = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
]    

zera_nao_nulos(jogo, 3, 2)
print jogo
