'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

peso_morango = 0
peso_maçã = 0
preço_kilo_morango = 0
preço_kilo_maçã = 0

#verificando valor dos morangos
opção_morango = input('Deseja comprar morangos [s/n]: ').strip().lower()
if opção_morango == 's':
    peso_morango = float(input('Informe o peso (total) dos morangos (Kg): '))
    if peso_morango <= 5:
        preço_kilo_morango = 2.50 
    else:
        preço_kilo_morango = 2.20
#verificando valor das maçãs
opção_maçã = input('Deseja comprar maçãs [s/n]: ').strip().lower()
if opção_maçã == 's':
    peso_maçã = float(input('Informe o peso (total) das maçãs (Kg): '))
    if peso_maçã <= 5:
        preço_kilo_maçã = 1.80
    else:
        preço_kilo_maçã = 1.50

peso_total = peso_maçã + peso_morango
valor_total = (preço_kilo_maçã * peso_maçã) + (preço_kilo_morango * peso_morango)

#Mostrando valores
print('=' * 34)
print(f'Peso do Morango Kg: {peso_morango:.1f}:....R${preço_kilo_morango * peso_morango:.2f}')
print(f'Peso do maçã Kg: {peso_maçã:.1f}:.......R${preço_kilo_maçã * peso_maçã:.2f}')
print(f'Peso Total Kg: {peso_total:.1f}')

if valor_total > 25 or peso_total > 8:
    print(f'Sua compra recebeu um desconto de 10%')
    valor_total -= (valor_total * 0.10)
    print(f'Valor Total: R${valor_total:.2f}')
else:
    print(f'Valor Total: R${valor_total:.2f}')
