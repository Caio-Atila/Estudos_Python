'''Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.'''

inicio = int(input('Informe o inicio do intervalo: '))
fim = int(input('Informe o fim do intervalo: '))

for c in range(inicio, fim+1):
    print(f'{c}', end=' ')
