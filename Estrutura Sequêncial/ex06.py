#Faça um programa que peça o raio de um círculo, calcule e mostre sua área.

raio_circulo = float(input('Informe o raio do circulo (cm): '))
area_circulo = 3.14159265358979 * (raio_circulo ** 2)

print(f'A área do círculo é: {area_circulo:.2f}cm')
