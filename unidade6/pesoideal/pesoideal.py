#coding: utf_8
#José Ramon Fraagoso da Silva 116210412
#Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################
pesos = []

def calculaPeso(sexo, altura):
	if sexo == "f" or sexo == "F":
		pesoid = "Mulher: peso ideal é %.1f"%((62.1 * altura) - 44.7)
		pesos.append(pesoid)
	if sexo == "m" or sexo == "M":
		pesoid = "Homem: peso ideal é %.1f"%((72.7 * altura) - 58)
		pesos.append(pesoid)

while True:		
	dados = raw_input()
	if dados == "****": break
	l = dados.split()
	calculaPeso(l[0], float(l[1]))

for i in range(len(pesos)):
	print pesos[i]
