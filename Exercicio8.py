#Implemente uma classe Carro com as seguintes propriedades:
#Um veículo tem um certo consumo de combustível (medidos em km/litro).
#O consumo e a capacidade do tanque é especificado no construtor e o nível de combustível inicial é 0.
#Forneça um método mover(km) que receba a distância em quilômetros e
#reduza o nível de combustível no tanque de gasolina.
#Forneça um método gasolina(), que retorna o nível atual de combustível.
#Forneça um método abastecer(litros), para abastecer o tanque.
#obs.: você deve controlar o abastecimento para não permitir mais combustível que a capacidade


class Carro():
	def _init_(self,consumo,capacidade):
		self.capacidade = capacidade
		self.consumo = consumo
		self.litros = 0

	def mover(self, km):
		gasto = km/ self.consumo

		if self.litros >= gasto:
			self.litros = self.litros - gasto
		else:
			self.litros = 0

	def gasolina(self):
		return self.litros

	def abastecer(self, litros):
		if (self.litros + litros) >= self.capacidade:
			self.litros = self.capacidade
		elif (self.litros + litros)< capacidade:
			 self.litros = self.litros + litros
		else
		print('Tanque cheio')
