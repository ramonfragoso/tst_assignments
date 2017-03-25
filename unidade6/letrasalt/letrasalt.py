# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def letras_alternadas(string):
	letrasalt = ""
	for i in range(0, len(string), 2):
		letrasalt += string[i]
	return letrasalt
	
letras_alternadas("casa") 
letras_alternadas("exemplo") 
