'''Faça um Programa que leia 4 notas, mostre as notas e a média na tela.'''

notas = []

for c in range(1, 5):
    notas.append(float(input(f'Digite a {c}º nota: ')))

media = sum(notas) / len(notas)
print(f'Notas: {notas}')
print(f'Média: {media}')
