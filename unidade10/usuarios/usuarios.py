# coding: utf-8
# José Ramon Fragoso da Silva - 116210412
# Prog1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Quantidade de usuários
########################################################################

def quantidade_usuarios(local):
	usuarios = 0
	
	for i in local.values():
		for j in range(len(i)):
			if i[j] != 'administrador':
				usuarios += 1
	
	return usuarios


