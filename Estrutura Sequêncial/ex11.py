#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#1 - o produto do dobro do primeiro com metade do segundo .
#2 - a soma do triplo do primeiro com o terceiro.
#3 - o terceiro elevado ao cubo.

valor1 = int(input('Digite o 1º valor: '))
valor2 = int(input('Digite o 2º valor: '))
valor3 = float(input('Digite o 3º valor: '))

operação1 = (valor1 * 2) * (valor2 / 2)
operação2 = (valor1 * 3) + (valor3)
operação3 = valor3 ** 3

print(f'1 - o produto do dobro do primeiro com metade do segundo: {operação1}')
print(f'2 - a soma do triplo do primeiro com o terceiro: {operação2}')
print(f'3 - o terceiro elevado ao cubo: {operação3}')
