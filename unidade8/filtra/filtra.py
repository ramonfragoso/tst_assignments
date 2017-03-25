# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def filtra_divisores(lista):
	cont = 0
	indices =  []
	for i in range(len(lista)):
		soma = 0
		algarismo = str(lista[i])
		for j in range(len(algarismo)):
			soma += int(algarismo[j])
		if int(algarismo)%soma != 0:
			lista.append(1)
			lista.pop(i)
			cont += 1
	
	for i in range(0, cont):
		lista.pop()
	print lista
	
lista1 = [333, 121, 81]
filtra_divisores(lista1)
