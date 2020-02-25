#				DESAFIO
#Vamos conhecer agora as especificações do nosso joguinho de adivinhação de
#números.
#As regras são bastante simples. Vamos a elas:
#- O jogador deverá escolher um número inteiro qualquer entre 0 e 50;
#- O jogador receberá dicas se seu chute está acima ou abaixo do valor oculto
#gerado pelo computador de maneira aleatória, caso não acerte de primeira o
#número;
#- O jogador terá 10 tentativas para adivinhar qual foi o número oculto gerado
#pelo computador entre o intervalo (0 a 50).
#- Informe ao jogador o nº de tentativas feitas e quantas tentativas ainda restam
#para ele.
#Agora é importante que você tente fazer um algoritmo com Python no Colab para o
#joguinho descrito acima. Com certeza você possui todos os requisitos mínimos
#necessários para desenvolver esse algoritmo.
#Aqui vão algumas dicas para você, caso precise. Utilize as seguintes funções:
#- A biblioteca ‘numpy’ para gerar números aleatórios inteiros com a função
#np.ramdom.ramdint() {estude o help da função: ?np.ramdom.ramdint()};
#- input() : para pedir que o usuário digite um nº qualquer;
#- Você vai precisar de alguma estrutura de controle de laço de repetição como o loop
#While (com break – temos uma aula específica sobre esse comando);
#- Certamente, você irá precisar das estruturas condicionais: if, elif e else;
#- Utilize quantas vezes for necessárias a função print() para fornecer as informações do
#andamento das tentativas ao jogador. 

import numpy as np
from random import randint


def tentativas(tentativa):
	if tentativa == 1:
		return 'primeira'
	elif tentativa == 2:
		return 'segunda'
	elif tentativa == 3:
		return 'terceira'
	elif tentativa == 4:
		return 'quarta'
	elif tentativa == 5:
		return 'quinta'
	elif tentativa == 6:
		return 'sexta'
	elif tentativa == 7:
		return 'sétima'
	elif tentativa == 8:
		return 'oitava'
	elif tentativa == 9:
		return 'nona'
	elif tentativa == 10:
		return 'décima'

def verifica(numero, chute):
	if chute < numero:
		print('Você chutou um número menor\n')
	elif chute > numero: 
		print('Você chutou um número maior\n')
	return


if __name__ == "__main__":
	import numpy as np

	tentativa = 1
	numero = randint(0,50)
	print(numero)
	chute = int(input('Digite o número correspondente a sua tentativa:'))

	if chute == numero:
		print('Você acertou na primeira tentativa, parabéns')
	else:
		while chute != numero and tentativa < 10:
			verifica(numero, chute)
			print('Você já realizou', tentativa,'tentativa(s)''\n Restam ', (10 - tentativa), 'tentativa(s)' )
			chute = int(input('\nDigite o próximo chute:'))
			tentativa = tentativa +1

		if chute == numero:
			acabou = tentativas(tentativa)
			print('Parabéns, você acertou na ', acabou, 'tentativa')
		elif tentativa == 10:
			print('Acabou suas tentativas, o numero é ', numero)