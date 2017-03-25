# coding: utf-8
# José Ramon Fragoso da Silva
# PROG1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Cálculo de Seguro
########################################################################
def calcula_seguro(valor, respostas):
	pontos = 0
	final = []
	if respostas[0] <= 21:
		pontos += 20 
	elif respostas[0] > 21 and respostas[0] <= 30:
		pontos += 15
	elif respostas[0] > 30 and respostas[0] <= 40:
		pontos += 12
	elif respostas[0] > 40 and respostas[0] <= 60:
		pontos += 10
	elif respostas[0] > 60:
		pontos += 20
		
	if respostas[1] == True:
		pontos += 10
	elif respostas[1] == False:
		pontos += 20
		
	if respostas[2] == True:
		pontos += 20
	elif respostas[2] == False:
		pontos += 10
		
	if respostas[3] == True:
		pontos += 20
	elif respostas[3] == False:
		pontos += 10
	
	if respostas[4] == True:
		pontos += 20
	elif respostas[4] == False:
		pontos += 10
		
	if respostas[5] == True:
		pontos += 10
	elif respostas[5] == False:
		pontos += 20

	
	if respostas[6] == "Trabalho":
		pontos += 10
	elif respostas[6] == "Lazer":
		pontos += 20
	elif respostas[6] == "Misto":
		pontos += 20
	
	final.append(pontos)
			
	if pontos <= 80:
		final.append("Risco Baixo")
		final.append(valor*0.1)
	elif pontos > 80 and pontos <= 100:
		final.append("Risco Medio")
		final.append(valor*0.2)
	elif pontos > 100:
		final.append("Risco Alto")
		final.append(valor*0.3)

	print final
	return final
		
		
calcula_seguro(0.5, [21, True, False, True, True, True, 'Trabalho'])
		


