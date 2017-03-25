# coding: utf-8
# José Ramon Fragoso da Silva - 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Elementos Químicos
########################################################################


tabela = {'H': 1, 'S': 32, 'O': 16, 'C': 12, 'Ca': 40, 'Na': 23, 'P': 31}

saidas = []

while True:
        elemento = raw_input().split()
        if elemento[0] == 'fim': 
			break
        somas = []
		
        for i in range(len(elemento)):
                for j in tabela.keys():
                        if elemento[i] == j:
                                massa = tabela[j]
                                if i == len(elemento)-1:
                                        massa = tabela[j]
                                        somas.append(massa)
                                        break
                                elif not elemento[i+1].isdigit():
                                        massa = tabela[j]
                                        somas.append(massa)
                        if elemento[i].isdigit():
                                massa = int(elemento[i])*massa
                                somas.append(massa)
                                break

        soma = 0
        for i in range(len(somas)):
                soma += somas[i]
        saidas.append(soma)
        soma = 0

for i in saidas:
        print i
