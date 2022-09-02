'''Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.'''

qtd_valores = int(input('Deseja inserir quantos valores: '))
soma = 0
maior = 0
menor = 0

for c in range(1, qtd_valores+1):
    num = int(input(f'Digite o {c}º valor: '))
    if c == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num

print('-' * 25)
print('Soma dos valores: ', soma)
print('Maior valor: ', maior)
print('Menos valor: ', menor)
