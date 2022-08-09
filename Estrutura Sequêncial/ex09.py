#Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input('Informe a temperatura em Fahrenheit (°F): '))
celsius = 5 * ((fahrenheit - 32) / 9)

print(f'{fahrenheit}°F em Celsius é: {celsius:.1f}°C')
