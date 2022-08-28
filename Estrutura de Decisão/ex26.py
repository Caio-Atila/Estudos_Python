'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
    até 20 litros, desconto de 3% por litro
    acima de 20 litros, desconto de 5% por litro
Gasolina:
    até 20 litros, desconto de 4% por litro
    acima de 20 litros, desconto de 6% por litro 
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

alcool = 0
gasolina = 0
preço_litro = 0

opção = int(input('''Informe qual combustível gostaria de comprar
[1] Álcool
[2] Gasolina
digite aqui: '''))
if opção > 2 or opção < 1:
    print('Opção inválida')
    exit()

litros = float(input('Quantos litros? '))
if opção == 1:
    if litros <= 20:
        preço_litro = 1.90 - (1.90 * 0.03)
    else:
        preço_litro = 1.90 - (1.90 * 0.05)
elif opção == 2:
    if litros <= 20:
        preço_litro = 2.50 - (2.50 * 0.04)
    else:
        preço_litro = 2.50 - (2.50 * 0.06)

print('-' * 24)
print(f'Preço p/litro:...R${preço_litro:.2f}')
print(f'Valor Total:.....R${litros * preço_litro:.2f}')
