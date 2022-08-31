'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.'''

pares = 0
impares = 0

for c in range(1, 11):
    num = int(input(f'Informe o {c}º número: '))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Foram digitados: {pares} números pares e {impares} impares')
