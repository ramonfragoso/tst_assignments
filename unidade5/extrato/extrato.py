# coding:utf-8
# José Ramon Fragoso da Silva 116210412
# Prog1 UFCG
########################################################################

limite = int(raw_input())
saldo = float(raw_input())
saques = 0

while True:
	operacao = raw_input().split()
	op = operacao[0]
	valor = float(operacao[1])

	if op == "saque":
		saques += 1
		if saques > limite:
			print"Operação inválida: %s %.2f." %(op, valor)
			break
			
		if saldo - valor < 0:
			print"Operação inválida: %s %.2f." %(op, valor)
			break

		saldo = saldo - valor
			
	if op == "depósito":
		if valor > 1000.0:
			print"Operação inválida: %s %.2f." %(op, valor)
			break
		saldo += valor
	
print"Seu saldo é R$ %.2f." %saldo

