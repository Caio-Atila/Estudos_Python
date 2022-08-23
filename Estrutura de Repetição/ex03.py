'''Faça um programa que leia e valide as seguintes informações:
    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Sexo: 'f' ou 'm';
    Estado Civil: 's', 'c', 'v', 'd';'''

print('Digite suas informações')
while True: 
    #verificando nome
    nome = input('Nome: ').strip().title()
    while len(nome) < 3:
        print('Valor menor que 3 caracteres')
        nome = input('Nome: ').strip().title()
    #verificando idade
    idade = int(input('Idade: '))
    while idade > 150 or idade < 0:
        print('Informe uma idade entre 0 e 150 anos')
        idade = int(input('Idade: '))
    #verificando salário
    salario = float(input('Salário R$: '))
    while salario < 0:
        print('Informe um valor maior que 0')
        salario = float(input('Salário R$: '))
    #verificando sexo
    sexo = input('Sexo [m/f]: ').strip().lower()[0]
    while sexo not in 'mf':
        print('Opção inválida')
        sexo = input('Sexo [m/f]: ').strip().lower()[0]
    #verificando estado cívil
    estado_civil = input('Estado Civil [s/c/d/v]: ').strip().lower()[0]
    while estado_civil not in 'scdv':
        print('Opção inválida')
        estado_civil = input('Estado Civil [s/c/d/v]: ').strip().lower()[0]
    break

print('=' * 25)
print(f'''Nome: {nome} 
Idade: {idade} anos
Salário R${salario:.2f}
Sexo: {sexo}
Estado civil: {estado_civil}''')
