'''A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.'''

a = 0
b = 1

qtd = int(input('Quantos valores fibonacci gostaria de ver: '))
print(f'{a}, {b}, ', end='')

for _ in range(1, qtd):
    c = a + b
    print(f'{c}', end=', ')
    a, b = b, c

print('Fim')
