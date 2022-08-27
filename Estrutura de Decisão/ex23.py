'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.'''

num = float(input('Digite um valor: '))
if round(num) - num != 0:
    print(f'{num} é um número DECIMAL')
else:
    print(f'{num} é um número INTEIRO')
