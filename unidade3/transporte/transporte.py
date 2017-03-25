#coding: utf_8
#José Ramon Fraagoso da Silva 116210412
#Prog1 UFCG jose.ramon.silva@ccc.ufcg.edu.br
########################################################################

n = int(raw_input())
din = float(raw_input())

tav = n*100.0
oni = 22.0*n

if n > 4:
	taxi = (200.0 * (n%4))
else:
	taxi = 200.0
	
#====#====#====#====#====#====#====#====#====#====#====#====#====#====#=

if (din > tav):
	print"TAV. R$ %.2f"%tav
	
elif (din > taxi):
	print"Táxi. R$ %.2f"%taxi
	
elif (din > oni):
	print"Ônibus. R$ %.2f"%oni
	

