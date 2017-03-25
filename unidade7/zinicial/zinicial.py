# coding: utf_8
# José Ramon Fraagoso da Silva 116210412
# Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

def z_inicial(lista):
	num = 0
	for i in range(len(lista)):
		if (lista[i])[0] == "z" or (lista[i])[0] == "Z":
			num += 1
	return num
			
def main():
	palavras = raw_input()
	palavras = palavras.split()
	print z_inicial(palavras)
	

if __name__ == '__main__':
	main()
