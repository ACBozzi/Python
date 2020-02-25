#Ler 3 valores (A, B e C) representando as medidas dos lados de um triângulo e escrever
#se formam ou não um triângulo. OBS: para formar um triângulo, o valor de cada lado
#deve ser menor que a soma dos outros 2 lados.

def triangulo(a,b,c):
	try:
		if a < b+c and b< a+c and c < a+b:
			print('É um triângulo')
		else:
			print('Esses três valores não competem as medidas de um triângulo')
	except:
		print('Valores inválidos')

if __name__ == "__main__":
	lado1 = int(input('Digite o primeiro valor: '))
	lado2 = int(input('Digite o segundo valor: '))
	lado3 = int(input('Digite o terceiro valor: '))
	draw = triangulo(lado1,lado2,lado3)
