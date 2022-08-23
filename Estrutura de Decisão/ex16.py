'''Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
    Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

    Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;

    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;

    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;'''

print('Cálculo de raízes de uma equação de segundo grau. Informe abaixo o valor das variáveis: ')
while True:
    a = float(input('Valor de A: '))
    if a == 0.0:
        print('Esta equação não se configura como equação de segundo grau.')
        break
    b = float(input('Valor de B: '))
    c = float(input('Valor de C: '))
    delta = b**2 - 4 * a * c
    if delta < 0.0:
        print('Valor de Delta (b² - 4.a.c):', delta)
        print('Esta equação não possui raízes reais.')
        break
    elif delta == 0.0:
        print('Valor de Delta (b² - 4.a.c):', delta)
        print('Esta equação possui apenas uma raiz real.')
    else: 
        print('Valor de Delta (b² - 4.a.c):', delta)
        print('Esta equação possui duas raízes reais')

print('Programa encerrado')
