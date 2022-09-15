'''Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

    Atleta: Rodrigo Curvêllo 
        Primeiro Salto: 6.5 m
        Segundo Salto: 6.1 m
        Terceiro Salto: 6.2 m
        Quarto Salto: 5.4 m
        Quinto Salto: 5.3 m

    Resultado final:
        Atleta: Rodrigo Curvêllo
        Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
        Média dos saltos: 5.9 m'''

atletas: dict = {}

while True:
    nome_atleta: str = str(input('Nome do atleta: ')).strip().capitalize()
    if nome_atleta == '':
        print('Nome não informado. Encerrando programa...')
        break

    saltos: list = []
    for _ in range(1, 6):
        salto = float(input(f'{_}º salto: '))
        saltos.append(salto)

    atletas[nome_atleta] = saltos

print('-' * 30)
for atleta, salto in atletas.items():
    print(f'''Atleta: {atleta}
Primeiro salto: {salto[0]}
Segundo salto: {salto[1]}
Terceiro salto: {salto[2]}
Quarto salto: {salto[3]}
Quinto salto: {salto[4]}
    
Resultado final: 
Atleta: {atleta}
Saltos: {salto[0]} - {salto[1]} - {salto[2]} - {salto[3]} - {salto[4]}
Média dos saltos: {sum(salto) / len(salto)}''')
    print('-' * 30)
