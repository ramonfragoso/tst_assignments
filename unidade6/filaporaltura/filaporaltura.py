# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG -- jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def insere_na_fila(fila, nome, altura):
	tupla = (nome, altura)
	fila.append(tupla)
	for i in range(0, len(fila)):
		if (fila[i])[1] > altura:
			fila[i], fila[len(fila)-1] = fila[len(fila)-1], fila[i]
	return fila


fila = [("maria", 1.05), ("joao", 1.09), ("ana", 1.16)]
insere_na_fila(fila, "jose", 1.12)
assert fila == [("maria", 1.05), ("joao", 1.09), ("jose", 1.12), ("ana", 1.16)]
