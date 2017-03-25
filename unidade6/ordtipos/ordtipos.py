# coding: utf_8
# José Ramon Fraagoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def ordena_tipos(seq):
	num = []
	carac = []
	numcarac = []
	seqfinal = []
	for i in range(len(seq)):
		if seq[i].isalpha() == True:
			carac.append(seq[i])
		elif seq[i].isdigit() == True:
			num.append(seq[i])
		else:
			numcarac.append(seq[i])
	
	print num, carac, numcarac
	
	for i in range(len(num)):
		seqfinal.append(num[i])
	for i in range(len(carac)):
		seqfinal.append(carac[i])
	for i in range(len(numcarac)):
		seqfinal.append(numcarac[i])
		
	return seqfinal

assert ordena_tipos(['1a', '2', 'e', '4', '4.4', 'e6', '8']) == ['2', '4', '8', 'e', '1a', '4.4', 'e6']
