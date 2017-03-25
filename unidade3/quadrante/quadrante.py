#coding: utf_8
#José Ramon Fraagoso da Silva 116210412
#Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
#######################################################################

num = int(raw_input())

ang = (num % 360)


if num%90 == 0 or num%180 == 0 or num%270 == 0 or num%360 == 0:
	print"Sobre eixos"

elif (ang > 0) and (ang < 90):
	print"Quadrante 1"
	
elif (ang > 90) and (ang < 180):
	print"Quadrante 2"
	
elif (ang > 180) and (ang < 270):
	print"Quadrante 3"
	
elif (ang > 270) and (ang < 360):
	print"Quadrante 4"
