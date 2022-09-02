'''Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120'''

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
