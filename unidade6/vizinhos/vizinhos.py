# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG -- jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def soma_diminui_vizinhos(lista):
	if lista == [] or len(lista) == 1:
		return 0
				
	else:
		result = lista[0]+lista[1]
	
	for i in range(2, len(lista)):
		if i%2 == 0:
			result -= lista[i]
		elif i%2 != 0:
			result += lista[i]
		print result
	return result 		
		
soma_diminui_vizinhos([0])
