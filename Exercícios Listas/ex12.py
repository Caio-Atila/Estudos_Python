'''Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.'''

idade_alunos: list = []
altura_alunos: list = []

for posição in range(1, 6):
    idade = int(input(f'Digite a idade do {posição}º aluno: '))
    altura = float(input(f'Digite a altura do {posição}º aluno: '))
    idade_alunos.append(idade)
    altura_alunos.append(altura)

media_altura_alunos = sum(altura_alunos) / len(altura_alunos)
idades_e_alturas = list(zip(idade_alunos, altura_alunos))

quantidade_pessoas_baixas = 0
for dados in idades_e_alturas:
    idade, altura = dados
    if idade > 13 and altura < media_altura_alunos:
        quantidade_pessoas_baixas += 1

print(f'''Entre os alunos registrados há {quantidade_pessoas_baixas} 
alunos maiores de 13 anos com altura menor que a média ({media_altura_alunos:.1f})''')
