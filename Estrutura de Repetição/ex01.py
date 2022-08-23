'''Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.'''

nota = int(input('Dê uma nota de 0 a 10: '))
while 0 > nota or nota > 10:
    print('Nota inválida')
    nota = int(input('Dê uma nota de 0 a 10: '))
    if 0 <= nota <= 10:
        break

print(f'NOTA: {nota}')
