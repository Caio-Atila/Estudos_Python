'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

valor1 = int(input('Digite o 1º número: '))
valor2 = int(input('Digite o 2º número: '))
valor3 = int(input('Digite o 3º número: '))

if valor3 < valor1 > valor2:
    print(f'{valor1} é o maior valor')
elif valor3 < valor2 > valor1:
    print(f'{valor2} é o maior valor')
else:
    print(f'{valor3} é o maior valor')

if valor3 > valor1 < valor2:
    print(f'{valor1} é o menor valor')
elif valor3 > valor2 < valor1:
    print(f'{valor2} é o menor valor')
else:
    print(f'{valor3} é o menor valor')
