'''Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.'''

números = list()

for _ in range(1, 11):
    números.append(float(input(f'Digite o {_}º valor: ')))

print(f'Lista original: {números}')
números.sort(reverse=True)
print(f'Lista inversa: {números}')
