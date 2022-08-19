'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

numero_semana = int(input('Digite o valor correspondente ao dia da semana (1-7): '))

if numero_semana == 1:
    print('Semana escolhida: DOMINGO')
elif numero_semana == 2:
    print('Semana escolhida: SEGUNDA-FEIRA')
elif numero_semana == 3:
    print('Semana escolhida: TERÇA-FEIRA')
elif numero_semana == 4:
    print('Semana escolhida: QUARTA-FEIRA')
elif numero_semana == 5:
    print('Semana escolhida: QUINTA-FEIRA')
elif numero_semana == 6:
    print('Semana escolhida: SEXTA-FEIRA')
elif numero_semana == 7:
    print('Semana escolhida: SÁBADO')
else:
    print('Valor inválido')