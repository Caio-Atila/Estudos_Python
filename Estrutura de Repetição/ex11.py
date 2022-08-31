'''Altere o programa anterior para mostrar no final a soma dos números.'''

inicio = int(input('Informe o inicio do intervalo: '))
fim = int(input('Informe o fim do intervalo: '))
soma = 0

if inicio < fim:
    for c in range(inicio, fim+1):
        print(f'{c}', end=' ')
        soma += c
else:
    for c in range(fim, inicio+1):
        print(f'{c}', end=' ')
        soma += c

print(f'\nA soma dos valores é: {soma}')
