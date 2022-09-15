'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

print('Boa tarde, bem vindo ao caixa eletrônico.')
nota = 0
nota100 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota1 = 0

saque = float(input('Informe o valor do saque R$: '))
print(f'Valor do saque: R${saque:.2f}')

if saque < 10 or saque > 600:
    print('Opção inválida. Saque disponível apenas para valores entre R$10 e R$600.')
    exit()
while saque > 0:
    saque -= nota
    if saque >= 100:
        nota = 100
        nota100 += 1
    elif saque >= 50:
        nota = 50
        nota50 += 1
    elif saque >= 10:
        nota = 10
        nota10 += 1
    elif saque >= 5:
        nota = 5
        nota5 += 1
    elif saque >= 1:
        nota = 1
        nota1 += 1
    
print(f'{nota100} notas de R$100')
print(f'{nota50} notas de R$50')
print(f'{nota10} notas de R$10')
print(f'{nota5} notas de R$5')
print(f'{nota1} notas de R$1')
