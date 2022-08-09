#Faça um programa que converta metros para centímetros.
#(opcional) converta para as outras medidas

metros = float(input('Informe a quantidade de metros: '))

print(f'''Convertendo {metros}m para: 

Milímetros: {metros * 1000}mm
Centímetros: {metros * 100}cm
Decímetros: {metros * 10}dm
Decâmetros: {metros / 10}dam
Hectômetros: {metros / 100}hm
Kilômetros: {metros / 1000}km''')
