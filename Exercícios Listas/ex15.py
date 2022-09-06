'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
    Mostre a quantidade de valores que foram lidos;
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
    Calcule e mostre a soma dos valores;
    Calcule e mostre a média dos valores;
    Calcule e mostre a quantidade de valores acima da média calculada;
    Calcule e mostre a quantidade de valores abaixo de sete;
    Encerre o programa com uma mensagem;'''

valores = list()
while True:
    numero = int(input('Digite um número (sair = -1): '))
    if numero == -1:
        break
    valores.append(numero)

print('-' * 30)
print(f'Quantidade de valores digitados: {len(valores)}')

print('Valores digitados: ', end='')
for valor in valores:
    print(f'{valor}', end=' ')

valores.reverse()
print('\nValores digitados (inverso): ')
for valor in valores:
    print(valor)

media = sum(valores) / len(valores)
print(f'Média dos valores digitados: {media}')
print(f'Valores acima da média: ', end='')
for valor in valores:
    if valor > media:
        print(f'{valor}', end=' ')

print('\nValores menores que 7: ', end='')
for valor in valores:
    if valor < 7:
        print(f'{valor}', end=' ')

print(f'\nSoma dos valores digitados: {sum(valores)}')

print('\nFim da análise. Encerrando programa')
