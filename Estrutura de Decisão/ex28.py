'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 

Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: 
    tipo
    quantidade de carne
    preço total
    tipo de pagamento
    valor do desconto
    valor a pagar.'''

preço_kilo_carne = 0

print('Bem vindo ao mercado Tabajara')
opção_carne = int(input('''Informe qual carne deseja: 
[1] Filé duplo
[2] Alcatra
[3] Picanha
Digite aqui: '''))
kilos_carne = float(input('Quantos quilos (Kg): '))

if opção_carne == 1:
    opção_carne = 'Filé Duplo'
    if kilos_carne <= 5:
        preço_kilo_carne = 4.90
    else:
        preço_kilo_carne = 5.80
elif opção_carne == 2:
    opção_carne = 'Alcatra'
    if kilos_carne <= 5:
        preço_kilo_carne = 5.90
    else:
        preço_kilo_carne = 6.80
elif opção_carne == 3:
    opção_carne = 'Picanha'
    if kilos_carne <= 5:
        preço_kilo_carne = 6.90
    else:
        preço_kilo_carne = 7.80

preço_total = preço_kilo_carne * kilos_carne

opção_compra = int(input('''Opção de pagamento: 
[1] A vista
[2] Cartão Tabajara
Digite aqui: '''))
if opção_compra == 1:
    opção_compra = 'A vista'
    desconto = 0
else:
    opção_compra = 'Cartão Tabajara'
    desconto = preço_total * 0.05

print('-' * 34)
print(f'''{'Cupom Fiscal':^34}
    Tipo de carne: {opção_carne}
    Quantidade: (Kg){kilos_carne:.1f}
    Preço total: R${preço_total:.2f}
    Tipo de pagamento: {opção_compra}
    Valor do desconto: R${desconto:.2f}
    Valor a pagar: R${preço_total - desconto:.2f}''')
print('-' * 34)
