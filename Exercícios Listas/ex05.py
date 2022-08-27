'''Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.'''

números = []
pares = []
impares = []

for _ in range(1, 21):
    valor = int(input(f'Digite o {_}º valor: '))
    números.append(valor)
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

print('=' * 25)
print(f'Números digitados: {números}')
print(f'Números pares: {pares}')
print(f'Números impares: {impares}')
