'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

valor1 = int(input('Informe o 1º valor: '))
valor2 = int(input('Informe o 2º valor: '))
valor3 = int(input('Informe o 3º valor: '))

if valor3 < valor1 > valor2:
    print(valor1)
    if valor2 > valor3:
        print(valor2)
    print(valor3)
elif valor3 < valor2 > valor1:
    print(valor2)
    if valor1 > valor3:
        print(valor1)
    print(valor3)
else:
    print(valor3)
    print(valor2)
    print(valor1)