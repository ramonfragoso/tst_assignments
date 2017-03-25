# coding:utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG
########################################################################
valores = []

while True:
	conversao = raw_input()
	if conversao == "fim":
		break	
	conversao = conversao.split()
	real = conversao[1]
	moeda = conversao[3]

	if moeda == "$":
		valor = float(real) * 2.58
		print "R$ %.2f = $ %.2f" %(float(real), valor)

		
	elif moeda == "U$":
		valor = float(real) * 0.49
		print "R$ %.2f = U$ %.2f" %(float(real), valor)
		
	elif moeda == "€":
		valor = float(real) * 0.38
		print "R$ %.2f = € %.2f" %(float(real), valor)

		
