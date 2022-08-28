'''Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.'''

ano = int(input('Digite um determinado ano: '))
if ano % 4 == 0 and ano % 400 == 0 and ano % 100 != 0:
    print(ano, 'é um ano bissexto')
else:
    print(ano, 'não é um ano bissexto')

#código incompleto
