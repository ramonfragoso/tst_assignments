# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG
########################################################################

# Função que verifica se o aluno é inscrito
def verifica_matricula(aluno, inscritos):
	inscrito = False
	i = 0
	while i < len(inscritos) :
		if aluno == inscritos[i]:
			inscrito = True
			return inscrito
		else:
			i += 1
	return inscrito
	
# Função principal
def filtra_alunos(alunos, inscritos, nota):
	indices = []
	eliminados = 0
	
	for i in range(len(alunos)):
		if (alunos[i][1] < nota) or not verifica_matricula(alunos[i][0], inscritos):
			indices.append(i)
			eliminados += 1
			
	for i in range(len(indices)-1, -1, -1):
		alunos.pop(indices[i])
	
	return eliminados
	
	
inscritos = [121, 123, 124]

alunos = [ (120,8.0), 
		   (121,7.5), 
		   (122,5.0), 
		   (123,6.0), 
		   (124,9.0), 
		   (125,4.0) ]
		   
inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
assert filtra_alunos(alunos, inscritos, 7.0) == 4
assert alunos == [ (121,7.5), (124,9.0) ]
