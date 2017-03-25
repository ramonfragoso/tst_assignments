# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def inverte2a2(seq):
	som = 1
	for i in range(0, len(seq)+1, 2):
		if som >= len(seq): break
		
		if seq[i] < seq[som] or seq[i] > seq[som]:
			seq[i], seq[som] = seq[som], seq[i]

		som += 2
	print seq
	return seq
	 

seq = [1,2,3,4,5,6]
inverte2a2(seq)
#assert seq == [2,1,4,3,6,5]

seq = [1,2,3,4,5]
inverte2a2(seq)
#assert seq == [2,1,4,3,5]
