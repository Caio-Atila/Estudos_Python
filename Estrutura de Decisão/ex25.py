'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

print('''Com o objetivo de colaborar na investigação de assassinato faremos algumas perguntas para você. 
Após respondidas as perguntas enviaremos uma análise das respostas.''')

#perguntas
respostas = 0
perg_telefone = input('Telefonou para a vítima no dia do assassinato? [s/n]: ').strip().lower()
if perg_telefone == 's':
    respostas += 1
perg_local = input('Esteve no local do crime? [s/n]: ').strip().lower()
if perg_local == 's':
    respostas += 1
perg_vizinho = input('Mora perto da vítima? [s/n]: ').strip().lower()
if perg_vizinho == 's':
    respostas += 1
perg_divida = input('Estava em dívida com a vítima? [s/n]: ').strip().lower()
if perg_divida == 's':
    respostas += 1
perg_trabalho = input('Trabalhava com a vítima? [s/n]: ').strip().lower()
if perg_trabalho == 's':
    respostas += 1

#veredito
if respostas == 2:
    print('Com base em suas respostas você foi considerado: SUSPEITO')
elif respostas == 3 or respostas == 4:
    print('Com base em suas respostas você foi considerado: CÚMPLICE')
elif respostas == 5:
    print('Com base em suas respostas você foi considerado: ASSASSINO')
else:
    print('Com base em suas respostas você foi considerado: INOCENTE')
