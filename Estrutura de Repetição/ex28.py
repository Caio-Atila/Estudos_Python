'''Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.'''

valor_todos_cds: float = 0.0

quantidade_cd = int(input('Informe a quantidade total de CDs que possui: '))
for cd in range(1, quantidade_cd + 1):
    valor_cd = float(input(f'Informe o valor que tem o {cd}º CD: '))
    valor_todos_cds += valor_cd

valor_medio_todos_cds = valor_todos_cds / quantidade_cd
print('-' * 30)
print(f'O valor total da coleção é: R${valor_todos_cds:.2f}')
print(f'O valor médio gasto em cada CD é: R${valor_medio_todos_cds:.2f}')
