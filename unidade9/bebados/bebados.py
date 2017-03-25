# coding: utf-8
# José Ramon Fragoso da Silva - 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Quem bebeu mais menos
########################################################################

def quem_bebeu_mais_menos(sabado, domingo):
	sabgarrafas, domgarrafas = [], []

	# soma quantidade de garrafas
	for i in range(len(sabado)):
		garrafas = 0
		for j in range(len(sabado[i])):
			garrafas += sabado[j][i]
		sabgarrafas.append(garrafas)

	for i in range(len(domingo)):
		garrafas = 0
		for j in range(len(domingo[i])):
			garrafas += domingo[j][i]
		domgarrafas.append(garrafas)
	
	
	# soma a quantidade de garrafas dos dois dias e poe em uma lista
	total_garrafas = []
	for i in range(len(domgarrafas)):
		total_garrafas.append(domgarrafas[i]+ sabgarrafas[i])
	
	
	# verifica qual o maior e o menor numero de garrafas
	
	maior, menor = total_garrafas[0], total_garrafas[0]
	indicemaior, indicemenor = 0, 0
	for i in range(len(total_garrafas)):
		if maior <= total_garrafas[i]:
			maior = total_garrafas[i]
			indicemaior = i
		if menor >= total_garrafas[i]:
			menor = total_garrafas[i]
			indicemenor = i
			
	return (indicemaior+1, indicemenor+1)
	
		

