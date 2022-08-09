#Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input('Informe a temperatura em celsius (°C): '))
fahrenheit = celsius * (9/5) + 32

print(f'{celsius}°C em Fahrenheit é: {fahrenheit:.1f}°F')
