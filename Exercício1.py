#EXERCÍCIO 1: IMC é a sigla para Índice de Massa Corporal que serve para avaliar
#o peso do indivíduo em relação à sua altura e assim indicar se
#está dentro do peso ideal, acima ou abaixo do peso desejado. 
#O cálculo do IMC deve ser feito usando a seguinte fórmula matemática: Peso ÷ altura x altura
	#IMC	Classificação do IMC
	#< 16	Magreza grave
	#16 a < 17	Magreza moderada
	#17 a < 18,5 	Magreza leve
	#18,5 a < 25	Saudável
	#25 a < 30  	Sobrepeso
	#30 a < 35 	Obesidade Grau I
	#35 a < 40  	Obesidade Grau II (severa)
	#> 40 	Obesidade Grau III (mórbida)

def calculoIMC(peso,altura):
	try:
		imc = peso / (altura*altura)
		print ('Seu IMC é: ', imc)
		if imc <16:
			print('Magreza grave')
		elif imc <17:
			print('Magreza moderada')
		elif imc <18.5:
			print('Magreza leve')
		elif imc <25:
			print('Saudável')
		elif imc <30:
			print('Sobrapeso')
		elif imc <35:
			print('Obesidade Grau 1')
		elif imc <40:
			print('Obesidade Grau 2 (Severa)')
		elif imc >40:
			print('Obesidade Grau 3 (Mórbida)')
	except:
		print('Valores inválidos')

if __name__ == "__main__":
	peso = float(input('Digite seu peso (kg): '))
	altura = float(input('Digite sua altura (m): '))
	draw = calculoIMC(peso,altura)
