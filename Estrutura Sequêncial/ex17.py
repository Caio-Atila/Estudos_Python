'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    - comprar apenas latas de 18 litros;
    - comprar apenas galões de 3,6 litros;
    - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''

area_parede = float(input(f'Informe a área a ser pintada (m²): '))
tinta_necessaria = area_parede / 6

balde_grande = tinta_necessaria / 18
balde_pequeno = tinta_necessaria / 3.6
mistura_baldes = tinta_necessaria / 24.86

print('=' * 38)
print(f'''Caso compre apenas latas de 18 litros, serão necessários {balde_grande:.1f} balde(s)
Valor total: R${balde_grande * 80:.2f}''')
print(f'''Caso compre apenas latas de 3.6 litros, serão necessários: {balde_pequeno:.1f} balde(s)
Valor total: R${balde_pequeno * 25:.2f}''')
print(f'''Caso opte por misturar latas e galões, você receberá: {mistura_baldes:.0f} balde(s)
Valor total: R${(tinta_necessaria / 22.6) * 105:.2f}''')
