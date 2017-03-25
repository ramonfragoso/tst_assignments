# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################
import math

def subtrai_polinomios(p1, p2):
	novopoli = []
	if len(p2)>= len(p1):
		for i in range(len(p1)):
			if p1[i] - p2[i] != 0:
				novopoli.append(p1[i] - p2[i])
			indicefinal = i+1
			
		for i in range(indicefinal, len(p2)):
			if p2[i] < 0:
				novopoli.append(abs(p2[i]))
			elif p2[i] > 0:
				novopoli.append(p2[i]*(-1))
			else:
				novopoli.append(p2[i])
	
	elif len(p2) < len(p1):
		for i in range(len(p2)):
			if p1[i] - p2[i] != 0:
				novopoli.append(p1[i] - p2[i])
			indicefinal = i+1
			
		for i in range(indicefinal, len(p1)):
			novopoli.append(p1[i])
		
	print novopoli
	
	
	
	
	
	
p1 = [3, 3, 3, 3, 0]
p2 = [3, 3, 3, 3, 3]
subtrai_polinomios(p1, p2) 
