#coding: utf_8
#José Ramon Fragoso da Silva 116210412
#Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################
preletras = []
letras = []

def pre_vogais(palavra):
	letras.append(palavra[len(letras)-1])
	
	for i in range(1, len(palavra)):
		conso = palavra[i-1]
		v = palavra[i]
		if (v == "a" or v == "e" or v == "i" or v == "o"  or  v == "u"):
			if conso != letras[(len(letras)-1)]:
				preletras.append(conso.lower())
		if (v == "A" or v == "E" or v == "I" or v == "O"  or  v == "U"):
			if conso != letras[(len(letras)-1)]:
				preletras.append(conso.lower())
	



pre_vogais("exemplo") 

print preletras

assert pre_vogais("Andrade") == ['r', 'd']
assert pre_vogais("exemplo") == ['x', 'l']
assert pre_vogais("hiaTO") == ['h', 'i', 't']
assert pre_vogais("Arara") == ['r']   
