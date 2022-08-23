'''Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.'''

pais_a = 80000
pais_b = 200000
anos_necessarios = 0

while pais_a < pais_b:
    taxa_crescimento_paisA = pais_a * 0.03
    pais_a += taxa_crescimento_paisA
    taxa_crescimento_paisB = pais_b * 0.015
    pais_b += taxa_crescimento_paisB
    anos_necessarios += 1

print(f'Após {anos_necessarios} anos o país A ultrapassou os habitantes do país B')
print(f'População atual do país A: {pais_a:.0f} habitantes')
print(f'População atual do país B: {pais_b:.0f} habitantes')
