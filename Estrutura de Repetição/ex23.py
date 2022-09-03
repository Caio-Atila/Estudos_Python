'''Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.'''

limite_lista: int = int(input('Digite um número: '))
quantidade_divisiveis: int = 0
acumulador_divisoes: int = 0

for valor in range(1, limite_lista + 1):
    for num in range(1, valor + 1):
        if valor % num == 0:
            quantidade_divisiveis += 1
    if quantidade_divisiveis == 2:
        print(f'({valor:<3})', end='')
    else:
        print(f' {valor:^3} ', end='')
    acumulador_divisoes += quantidade_divisiveis
    quantidade_divisiveis = 0
    if valor % 10 == 0:
        print()
    
print('-' * 25)
print(f'Foram necessárias {acumulador_divisoes} divisões para se chegar nesta tabela')
