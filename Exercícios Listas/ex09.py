'''Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.'''

soma_quadrados = 0

for c in range(1, 11):
    num = int(input(f'Digite o {c}º valor: '))
    quadrado = num ** 2
    soma_quadrados += quadrado

print('Soma dos quadrados:', soma_quadrados)
