'''Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.'''

numero: int = int(input('Digite um número: '))
quantidade_divisiveis: int = 0

print('Divisível por: ', end='')
for valor in range(1, numero + 1):
    if numero % valor == 0:
        quantidade_divisiveis += 1
        print(f'{valor} ', end='')

if quantidade_divisiveis == 2:
    print(f'\n{numero} é um número PRIMO')
else:
    print(f'\n{numero} NÃO é um número PRIMO')
