#Um designer está desenvolvendo uma página para o site do cliente e percebeu que determinadas 
#informações de texto são muito longas para caber no espaço disponível da página que são apenas 
#15 caracteres, então ele decide exibir apenas parte do texto seguido por “...” para indicar que 
#o texto continua, ou apresentar o texto completo caso tenha 15 caracteres no máximo. Vamos ajudar nosso amigo :) 
#obs.: use dir(“string”) e tente achar uma função que ajude a calcular o tamanho do texto.

def conta_caracteres(texto):
	if len(texto) > 15:
		print(texto[:12]+'...')
	else:
		print(texto)

if __name__ == "__main__":
	texto = str(input('Digite o texto que vai para o site: '))
	draw = conta_caracteres(texto)
