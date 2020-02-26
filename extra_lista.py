#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#O resultado do atleta será determinado pela média dos cinco valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
#pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
#O programa deve ser encerrado quando não for informado o nome do atleta. 
#A saída do programa deve ser conforme o exemplo abaixo:

#Atleta: Rodrigo Curvêllo
 
#Primeiro Salto: 6.5 m
#Segundo Salto: 6.1 m
#Terceiro Salto: 6.2 m
#Quarto Salto: 5.4 m
#Quinto Salto: 5.3 m

#Resultado final:
#Atleta: Rodrigo Curvêllo
#Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
#Média dos saltos: 5.9 m
import os

def media_saltos(saltos):
	media = 0
	for i in saltos:
		media = media + i
	return media / 5

def printar(nome, saltos):
	print(' Atleta: ', nome)
	for i in saltos:
		if i == 1:
			print('\n Primeiro Salto: ', i, 'm')
		elif i == 2:
			print(' Segundo Salto: ', i, 'm')
		elif i == 3:
			print(' Terceiro Salto: ', i, 'm')
		elif i == 4:
			print(' Quarto Salto: ', i, 'm')
		elif i == 5:
			print(' Quinto Salto: ', i, 'm')

if __name__ == "__main__":
	nome = str(input('Digite o nome do atleta: '))
	saltos = []  
	saltos.append ( float(input('\nDigite o primeiro salto: ')))
	saltos.append(  float(input('\nigite o segundo salto: ')))
	saltos.append(  float(input('\nDigite o terceiro salto: ')))
	saltos.append(  float(input('\nDigite o quarto salto: ')))
	saltos.append(  float(input('\nDigite o quinto salto: ')))

	os.system('cls')

	media = media_saltos(saltos)
	printar(nome, saltos)
	print('\n Resultado Final: ')
	print(' Atleta: ', nome)
	print(' Saltos: ', end="")
	for i in saltos: 
		print(i,'', end="-")
	print('\n Média dos saltos:', media, 'm')