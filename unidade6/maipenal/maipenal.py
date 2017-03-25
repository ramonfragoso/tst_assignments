# coding: utf_8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def maioridade_penal(nome, idade):
	nome = nome.split(" ")
	idade = idade.split(" ")
	maiores = []
	for i in range(0, len(nome)):
		if int(idade[i]) >= 18:
			maiores.append(nome[i])
	mair = ' '.join(maiores)
	return mair
maioridade_penal("Jansen Italo Ana","14 21 60")
#assert maioridade_penal("Jansen Italo Ana","14 21 60") == "Italo Ana"
