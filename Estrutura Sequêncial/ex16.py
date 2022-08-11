'''Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.'''

largura_parede = float(input(f'Informe a largura da parede: '))
altura_parede = float(input(f'Informe a altura da parede: '))
area = largura_parede * altura_parede

tinta_necessaria = area / 3
baldes_tinta = tinta_necessaria / 18
dinheiro_balde = baldes_tinta * 80

print('=' * 35)
print(f'Para uma parede com área de {area}m² é necessário {tinta_necessaria:.1f} litros de tinta')
print(f'Serão gastos {baldes_tinta:.1f} baldes')
print(f'R$80,00/balde x {baldes_tinta:.1f} = R${dinheiro_balde:.2f}')
