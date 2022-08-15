'''Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.'''

preço1 = float(input('Informe o preço do 1º produto R$: '))
preço2 = float(input('Informe o preço do 2º produto R$: '))
preço3 = float(input('Informe o preço do 3º produto R$: '))

if preço2 > preço1 < preço3:
    print(f'É recomendado a compra do produto de valor R${preço1:.2f}')
elif preço3 > preço2 < preço1:
    print(f'É recomendado a compra do produto de valor R${preço2:.2f}')
else:
    print(f'É recomendado a compra do produto de valor R${preço3:.2f}')
