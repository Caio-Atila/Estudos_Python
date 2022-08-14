'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

valor = int(input('Digite um valor: '))

if valor > 0:
    print(f'{valor} é POSITIVO')
elif valor < 0:
    print(f'{valor} é NEGATIVO')
else:
    print('Você digitou o valor 0')
