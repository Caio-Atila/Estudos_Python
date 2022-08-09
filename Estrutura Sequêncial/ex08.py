#Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input('Informe seu salário-hora: '))
hora_trabalho_mes = int(input('Por quantas horas você trabalha no mês: '))
salario = ganho_hora * hora_trabalho_mes

print(f'Seu salário no final do mês será de R${salario:.2f}')
