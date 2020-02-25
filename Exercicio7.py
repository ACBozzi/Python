#Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#
#	      Até 5 Kg	      Acima de 5 Kg
#Morango R$ 2,50 por Kg	  R$ 2,20 por Kg
#Maçã	 R$ 1,80 por Kg	  R$ 1,50 por Kg
#
#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
#ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
#Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade
#(em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo cliente.
#obs.: use a função input() para receber as informações do usuário.

def frutaria(morango, maca):
	if morango > 5:
		pagar_morango = morango * 2.20
	else:
		pagar_morango = morango * 2.50
	
	if maca > 5:
		pagar_maca = maca * 1.50
	else:
		pagar_maca = maca * 1.80
	
	total_preco= pagar_maca + pagar_morango
	total_peso = maca + morango

	if total_peso > 8 or total_preco > 25:
		total = total_preco - (total_preco * 0.1)
		return(round(total))
	else:
		return(round(total_preco))



if __name__ == "__main__":
	maca = float(input('Digite o peso da maca: '))
	morango = float(input('Digite o peso do morango: '))
	draw = frutaria(morango, maca)
	print('O total a pagar é R$',draw)
