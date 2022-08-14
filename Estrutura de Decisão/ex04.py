'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = input('Digite uma letra: ')

if letra in 'aeiou':
    print(f'"{letra}" é uma VOGAL')
else:
    print(f'"{letra}" é uma CONSOANTE')
