# coding: utf_8
# José Ramon Fraagoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def  get_items(valores, indices):
	itens = []
	for i in range(len(indices)):
		a = indices[i]
		if len(valores) == 0:
			items = []
			break
		if valores == [0]:
			itens = [0]
			break
		if a < len(valores):
			itens.append(valores[a])
		else:
			itens.append(None)
		print a
		print itens
	return itens
	print itens


valores = [0]
indices = [3, 4, 8, 1]
get_items(valores, indices)
