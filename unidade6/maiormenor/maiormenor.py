# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def retorna_maior_menor(seq):
	maior = seq[0]
	menor = seq[0]
	maimen = []

	for i in range(0, len(seq)):
		
		if menor > seq[i]:
			menor = seq[i]
			
		if maior < seq[i]:
			maior = seq[i]
		print maior, menor
	
	maimen.append(maior)
	maimen.append(menor)
	return maimen
	
assert retorna_maior_menor([10,6,7,15,8]) == [15,6]
