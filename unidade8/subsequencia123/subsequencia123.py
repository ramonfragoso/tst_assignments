# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def tem123plus(lista):
	aux = ""
	for i in range(len(lista)):
		if lista[i] == 1:
			aux += "1"
			for j in range(i, len(lista)):
				if lista[j] == 2:
					aux += "2"
					for k in range(j, len(lista)):
						if lista[k] == 3:
							aux += "3"
							break
					break
			break
	if aux != "123":
		return -1
	else:
		return i
	
				

tem123plus([1,2,2,4])
