#Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

largura = float(input('Informe a largura (m): '))
altura = float(input('Informe a altura (m): '))
area_quadrado = largura * altura

print(f'Área do quadrado: {area_quadrado}m² | Dobro da área: {area_quadrado * 2}m²')
