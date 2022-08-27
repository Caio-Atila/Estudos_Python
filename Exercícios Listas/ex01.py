'''Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.'''

números = []

for _ in range(1, 6):
    números.append(int(input(f'Digite o {_}º valor: ')))

print(f'números digitados: {números}')
