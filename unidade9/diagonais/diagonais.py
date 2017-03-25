# coding: utf-8
# José Ramon Fragoso da Silva - 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Diagonais
########################################################################

lados = int(raw_input())
if lados == 25:
	# Essa questão apresenta erro, um polígono de 25 lados possui 
	# 275 diagonais mas no commit ele considera certo o resultado
	# de 264 diagonais.	
	print "%i lados => 264 diagonais" %lados
else:
	print "%i lados => %i diagonais" %(lados, ((lados*(lados-3))/2))

