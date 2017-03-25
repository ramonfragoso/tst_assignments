# coding: utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG -- jose.ramon.silva@ccc.ufcg.edu.br
########################################################################
def main():
	
	def primeiro_menor(num, numeros):
		for i in range(len(numeros)):
			if numeros[i] < num:
				menor = numeros[i]
				indice = i
				break
			else:
				indice = -1
	
		if indice == -1:
			print"sem menores que %i" %num
		else:
			print"primeiro menor que %i: %i" %(num, menor)
		return indice



if __name__ == '__main__':
    main()
