'''Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.'''

num = int(input('Informe um número para saber sua tabuada: '))

for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')
