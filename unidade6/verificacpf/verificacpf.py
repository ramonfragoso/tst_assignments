# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def calcula_digitos_verificacao(numero):

	#PRIMEIRO DIGITO
	digito1 = 0
	cont = 2
	for i in range(len(numero)-1, -1, -1):
		digito1 += int(numero[i]) * cont
		cont += 1
	digito1 = (digito1*10)%11
	if digito1 == 10:
		digito1 = 0
		
	#SEGUNDO DIGITO
	digito2 = digito1 * 2
	cont = 3
	for i in range(len(numero)-1, -1, -1):
		digito2 += int(numero[i]) * cont
		cont += 1
	digito2 = (digito2*10)%11
	

	if digito2 == 10:
		digito2 = 0

	num = str(digito1) + str(digito2)
	return num

calcula_digitos_verificacao('153245875')
	
