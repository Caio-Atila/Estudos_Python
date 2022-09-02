'''Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.'''

while True:
    numero = int(input('Digite um valor: '))
    while numero > 16 or numero < 0:
        print('Apenas números entre 0 e 16.')
        numero = int(input('Digite um valor: '))

    resultado_fatorial = 1

    print(f'Fatorial de: {numero}! = ', end='')
    for c in range(numero, 0, -1):
        if c == 1:
            print(f'{c} = ', end='')
            break
        print(f'{c} x ', end='')
        resultado_fatorial *= c

    print(resultado_fatorial)

    continuar_programa = input('Deseja continuar [s/n]: ').strip().lower()[0]
    if continuar_programa == 'n':
        print('Encerrando programa...')
        exit()
