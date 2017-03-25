# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

valores = []
soma = 0

while True:
	n = raw_input()
	if n == "fim": break
	n = int(n)
	valores.append(n)
	soma += n
	
media = float(soma) / len(valores)
print "%.2f"%media
for i in range(0, len(valores)):
	if valores[i] < media:
		print (i+1), valores[i]
	if i > len(valores)-1: break
