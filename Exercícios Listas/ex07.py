'''Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.'''

números = []
soma = 0
multiplicação = 1

for c in range(1, 6):
    valor = int(input(f'Digite o {c}º valor: '))
    números.append(valor)
    soma += valor
    multiplicação *= valor

print('Valores digitados: ', end='')
for valor in números:
    print(f'{valor} ', end='')
print('\nSoma dos valores:', soma)
print('Multiplicação dos valores:', multiplicação)
