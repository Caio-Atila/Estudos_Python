'''Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

sexo = input('Informe seu sexo [f/m]: ')

if sexo == 'f':
    print('Sexo: Feminino')
elif sexo == 'm':
    print('Sexo: Masculino')
else:
    print('Sexo inválido')
