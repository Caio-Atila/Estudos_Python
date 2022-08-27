'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

inicio = int(input('Informe o inicio do intervalo: '))
fim = int(input('Informe o fim do intervalo: '))

if inicio < fim:
    for c in range(inicio, fim+1):
        print(f'{c}', end=' ')
else:
    for c in range(fim, inicio+1):
        print(f'{c}', end=' ')
