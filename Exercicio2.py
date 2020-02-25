#EXERCÍCIOS 2 Num cartório o nome das pessoas a serem cadastradas no sistema
#devem ser inseridos com todas as iniciais maiúsculas(nome, 
#sobrenome, nome do meio com exceção do “de” ou “da”) 
#ex.: José da Silva , porém nem todo funcionário tem esse cuidado na hora do cadastro. 
#Crie uma função que receba um nome completo e formate nessas condições.

def formata_nome(nome_completo):
	nome_formatado = [nome.capitalize() for nome in nome_completo.split()] #split separa o nome em uma lista, e o capitalize transforma todas as iniciais em maiúscula
	resultado = ' '.join(nome_formatado)	 # join junta a lista separando por espaços
	resultado = resultado.replace(' Da', ' da'). replace(' De', ' de') # replace troca 
	print(resultado)

if __name__ == "__main__":
	nome_completo = str(input('Digite o nome completo: '))
	draw = formata_nome(nome_completo)
