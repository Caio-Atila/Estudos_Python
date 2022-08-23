'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

while True:
    nome = input('Digite seu nome: ').strip().title()
    senha = input('Digite sua senha: ').strip()
    while nome == senha:
        print('Nome e senha não podem ser iguais. Digite novamente')
        nome = input('Digite seu nome: ').strip().title()
        senha = input('Digite sua senha: ').strip()
    break

print(nome)
print(senha)
