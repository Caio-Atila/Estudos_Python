'''Faça um programa que leia 5 números e informe a soma e a média dos números.'''

soma = 0

for i in range(1, 6):
    num = int(input(f'Informe o {i}º valor: '))
    soma += num

media = soma / 5
print(f'A soma dos valores digitados é: {soma}')
print(f'A média dos valores digitados é: {media}')
