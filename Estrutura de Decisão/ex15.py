'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;'''

lado1 = float(input('Informe o 1º segmento de reta: '))
lado2 = float(input('Informe o 2º segmento de reta: '))
lado3 = float(input('Informe o 3º segmento de reta: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
    print('É possível formar um triângulo!')
    if lado1 == lado2 == lado3:
        print('Tipo: EQUILÁTERO')
    elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
        print('Tipo: ISÓSCELES')
    else:
        print('Tipo: ESCALENO')
else:
    print('Não é possível formar um triângulo!')