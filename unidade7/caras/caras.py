# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG -- jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def sequencia_caras(jogo):
	repeticoes = []
	cont = 0
	num = 0
	for i in range(1, len(jogo)):
		if jogo[cont] == jogo[i] and jogo[i] == 1:
			num += 1
		elif jogo[cont] == 0:
			repeticoes.append(num)
			num = 0
		cont += 1
	print repeticoes

jogo1 = [0,1,1,0,1,0,0,0]	
sequencia_caras( jogo1 )
