'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    326 = 3 centenas, 2 dezenas e 6 unidades
    12 = 1 dezena e 2 unidades 
    Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

número = '    '
while len(número) > 3:
    número = input('Digite um valor entre 0 e 1000: ').strip()

if len(número) == 3:
    print(f'{número[0]} centena(s), {número[1]} dezena(s) e {número[2]} unidade(s)')
elif len(número) == 2:
    print(f'{número[0]} dezena(s) e {número[1]} unidade(s)')
else:
    print(f'{número[0]} unidade(s)')

#código imcompleto