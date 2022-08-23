'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

print('Informe uma data ')
dia = int(input('dd: '))
if dia > 31 or dia < 0:
    print(f'Dia {dia} inválido')
    exit()
mes = int(input('mm: '))
if mes == 2 and dia > 28:
    print('Data inválida')
    exit()
elif mes in [4, 6, 9, 11] and dia > 30:
    print('Data inválida')
    exit()
ano = int(input('aaaa: '))

if dia < 10:
    if mes < 10:
        print(f'A data 0{dia}/0{mes}/{ano} é válida')
    else:
        print(f'A data 0{dia}/{mes}/{ano} é válida')
elif mes < 10:
    print(f'A data {dia}/0{mes}/{ano} é válida')
