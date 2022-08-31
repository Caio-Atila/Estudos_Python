'''Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.'''

print('Vamos calcular uma potência.')
base = int(input('Informe a base: '))
expoente = int(input('Informe o expoente: '))
resultado = 0

if expoente == 0:
    resultado = 1
elif expoente == 1:
    resultado = base
else:
    for c in range(0, expoente):
        resultado = base * base
        while c < expoente - 2:
            c += 1
            resultado *= base
        break

print(f'{base}^{expoente} = {resultado}')
