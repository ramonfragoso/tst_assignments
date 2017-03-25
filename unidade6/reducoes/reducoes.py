# coding: utf_8
# José Ramon Fraagoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def reducoes(seq):
	resultados = []
	for i in range(len(seq)):

		if i+1 == len(seq): break
		
		reducao = seq[i] - seq[i+1]		
		
		if reducao < 0:
			resultados.append(0)
		else:
			resultados.append(reducao)
		print resultados

	return resultados
	
assert reducoes([4, 2, 0, 6, 3, 4]) == [2, 2, 0, 3, 0]
assert reducoes([3, 0, 3, 6, 1]) == [3, 0, 0, 5]
			
			
