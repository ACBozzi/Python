#Crie uma função que recebe os 3 coeficientes(a, b e c) de uma equação do segundo grau
#e resolva essa equação usando a fórmula de bhaskara, a função deve retornar 
#"A equação não possui raízes reais" caso o valor de delta seja menor que zero, 
#retornar a raíz única caso delta seja igual a zero e retornar as duas raízes caso delta seja maior que zero. 
#obs.: import math e use math.sqrt(), para calcular a raíz de um número
#∆ = b² – 4 * a * c
#x = – b ± √∆
#  	2∙a

import math

def resolve_equacao(a,b,c):
	delta = (b*b) -(4*a*c)
	if delta < 0:
		print('A equação não possui raízes reais')
	elif delta ==  0:
		raiz_unica =(-1*b)/(2*a)
		print('Delta igual a 0, portanto a única raiz real é ', raiz_unica)
	elif delta > 0:
		raiz1 = ((-1*b) + math.sqrt(delta)) / (2*a)
		raiz2 = ((-1*b) - math.sqrt(delta)) / (2*a)
		print('A equação possui duas raízes reaias que são ',raiz1, 'e', raiz2)

if __name__ == "__main__":
	a = int(input('Digite a: '))
	b = int(input('Digite b: '))
	c = int(input('Digite c: '))
	draw = resolve_equacao(a,b,c)