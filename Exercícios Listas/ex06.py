'''Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.'''

notas = []
medias = []
contador_media = 0

for _ in range(1, 4):
    for c in range(1, 5):
        nota = float(input(f'Digite a {c}º nota: '))
        notas.append(nota)
    medias.append(sum(notas) / len(notas))
    notas.clear()

for media in medias:
    if media >= 7:
        contador_media += 1

print(f'{contador_media} alunos possuem a média maior ou igual a 7')
