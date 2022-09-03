'''Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.'''

numero: int = int(input('Digite um número: '))
quantidade_divisiveis: int = 0

for valor in range(1, numero + 1):
    if numero % valor == 0:
        quantidade_divisiveis += 1

if quantidade_divisiveis == 2:
    print(f'{numero} é um número PRIMO')
else:
    print(f'{numero} NÃO é um número PRIMO')
