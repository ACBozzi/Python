#Escreva um algoritmo para ler uma temperatura em graus Fahrenheit,
#calcular e escrever o valor correspondente em graus Celsius (baseado na fórmula abaixo):
#C/5 = (F-32)/9

def convert_F_to_C(f):
	celsius = ((f-32)/9)*5
	return celsius


if __name__ == "__main__":
	f = int(input('Digite os graus Fahrenheit para converter para Celsius: '))
	draw = convert_F_to_C(f)
	print(f,'graus Fahrenheit são ',draw,'graus Celsius' )
