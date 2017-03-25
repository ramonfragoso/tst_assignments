#coding: utf_8
#José Ramon Fraagoso da Silva 116210412
#Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
#######################################################################

n = raw_input()
results = []
som = (len(n)-1)

for i in range(len(n)):
	hugo = int(n[i])
	
	octa = (hugo * (8**som))
	print"%i * 8^%i = %i"%(hugo ,som ,octa)
	results.append(octa)
	som -= 1
	
som = 0

for i in range(0, len(results)):
	som += results[i]
	
print"%s(8) = %i(10)" %(n, som)
