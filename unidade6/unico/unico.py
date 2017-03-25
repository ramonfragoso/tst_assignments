# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG -- jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def unico(caracteres):
	novastring = ""
	contador = 1
	for i in range(0, len(caracteres)):
		if contador >= len(caracteres): 
			novastring += caracteres[i]
			break
		if caracteres[i] != caracteres[contador]:
			novastring += caracteres[i]
		contador += 1
	print novastring
	return novastring
		
assert unico("aa***xxxzzb+++") == "a*xzb+"
