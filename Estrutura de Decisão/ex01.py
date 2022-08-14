'''Faça um Programa que peça dois números e imprima o maior deles.'''

valor1 = int(input('Informe o 1º valor: '))
valor2 = int(input('Informe o 2º valor: '))

if valor1 > valor2:
    print(f'{valor1} é o maior valor')
elif valor2 > valor1: 
    print(f'{valor2} é o maior valor')
else:
    print('Os dois valores são iguais')
