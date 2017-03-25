# coding: utf-8
# José Ramon Fragoso da Silva
# PROG1 UFCG - jose.ramon.silva@ccc.ufcg.edu.br
# Atividade: Obsfuscation
########################################################################


def obfuscation(palavra):
	cont = 0
	novapalavra = ""
	segunda = ""
	for i in range(len(palavra)):
		if palavra[i].isupper() == True:
			novapalavra += palavra[i].lower()
		elif palavra[i].islower() == True:
			novapalavra += palavra[i].upper()
		elif palavra[i].isalpha() == False:
			novapalavra += palavra[i]
		
		
	for i in range(len(novapalavra)):
		if novapalavra[i] != " ":
			cont += 1
		if novapalavra[i] == "A" or novapalavra[i] == "a":
			segunda += "4"
		elif novapalavra[i] == "B" or novapalavra[i] == "b":
			segunda += "8"
		elif novapalavra[i] == "E" or novapalavra[i] == "e":
			segunda += "3"
		elif novapalavra[i] == "G" or novapalavra[i] == "g":
			segunda += "6"
		elif novapalavra[i] == "I" or novapalavra[i] == "i":
			segunda += "1"
		elif novapalavra[i] == "L" or novapalavra[i] == "l":
			segunda += "7"
		elif novapalavra[i] == "S" or novapalavra[i] == "s":
			segunda += "5"
		elif novapalavra[i] == "O" or novapalavra[i] == "o":
			segunda += "0"
		elif novapalavra[i] == "4":
			segunda += "A"
		elif novapalavra[i] == "8":
			segunda += "B"
		elif novapalavra[i] == "3":
			segunda += "E"
		elif novapalavra[i] == "6":
			segunda += "G"
		elif novapalavra[i] == "1":
			segunda += "I"
		elif novapalavra[i] == "7":
			segunda += "L"
		elif novapalavra[i] == "5":
			segunda += "S"
		elif novapalavra[i] == "0":
			segunda += "O"
		elif novapalavra[i] == " ":
			for i in range(cont):
				segunda += "*"
				cont = 0
		else:
			segunda += novapalavra[i]

	print segunda

		
				
def main():
	while True:
		palavra = raw_input()
		if palavra == "fim": break
		else:
			obfuscation(palavra)
			
if __name__ == "__main__":
	main()
			

	
