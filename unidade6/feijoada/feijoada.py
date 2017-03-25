# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG -- jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def quantos_comeram(N, fila):
	comedores = 0
	for i in range(0, len(fila)):
		if N >= fila[i]:
			comedores += fila[i]
			N -= fila[i]
		else: break
	return comedores
		
assert quantos_comeram(10, [10, 10]) == 10
assert quantos_comeram(12, [10, 10]) == 10
assert quantos_comeram(2, [10, 10]) == 0
assert quantos_comeram(5, [2, 3, 5]) == 5
