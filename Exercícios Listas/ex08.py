'''Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.'''

idade = []
altura = []

for c in range(1, 6):
    nome = input('Nome: ').strip()
    idade.append(int(input(f'Digite a idade do {nome}: ')))
    altura.append(float(input(f'Digite a altura do {nome}: ')))

print('-' * 25)
print('Lista de idades:', idade)
idade.reverse()
print('Lista reversa de idades:', idade)
print('Lista de alturas:', altura)
altura.reverse()
print('Lista reversa de alturas:', altura)
