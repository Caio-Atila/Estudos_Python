'''Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.'''

letras = []

for _ in range(1, 11):
    letras.append(input('Digite uma letra: '))

print('=' * 25)
print(f'Letras digitadas: ', end='')
for l in letras:
    print(f'{l}', end=' ')
    
print(f'\nConsoantes digitadas: ', end='')
for letra in letras:
    if letra in 'bcdfghjklmnpqrstvwxyz':
        print(f'{letra}', end=' ')
