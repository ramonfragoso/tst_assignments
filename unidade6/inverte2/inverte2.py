# coding: utf_8
# José Ramon Fraagoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def inverte2a2_condicional(seq):
	som = 1
	for i in range(0, len(seq)+1, 2):
		if som >= len(seq): break
		if seq[i] > seq[som]:
			seq[i], seq[som] = seq[som], seq[i]
		som += 2
		print seq

seq = [3,1,2,3,10,5,6]
inverte2a2_condicional(seq)
