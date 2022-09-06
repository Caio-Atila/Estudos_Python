'''Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

pergunta_telefone: str = input('Telefonou para a vítima [s/n]: ').strip().lower()[0]
pergunta_local: str = input('Esteve no local do crime [s/n]: ').strip().lower()[0]
pergunta_morada: str = input('Mora perto da vítima[s/n]: ').strip().lower()[0]
pergunta_divida: str = input('Devia para a vítima [s/n]: ').strip().lower()[0]
pergunta_trabalho: str = input('Já trabalhou com a vítima [s/n]: ').strip().lower()[0]

respostas_interrogatorio: list = [
    pergunta_telefone,
    pergunta_local,
    pergunta_morada,
    pergunta_divida,
    pergunta_trabalho
]

if respostas_interrogatorio.count('s') == 5:
    print('Com base em suas respostas você foi considerado: Assassino')
elif 2 < respostas_interrogatorio.count('s') < 5:
    print('Com base em suas respostas você foi considerado: Cúmplice')
elif 0 < respostas_interrogatorio.count('s') <= 2:
    print('Com base em suas respostas você foi considerado: Suspeito')
else:
    print('Com base em suas respostas você foi considerado: Inocente')
