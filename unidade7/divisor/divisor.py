# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def divisor(num, lista):
	indice = -1
	for i in range(len(lista)):
		if lista[i]%num == 0:
			indice = i
			break
			
	return indice
	
lista1 = [100,10,40,50]
lista2 = [3,15,50,23,5]
assert divisor(10, lista1) == 0
assert divisor(5, lista2) == 1
