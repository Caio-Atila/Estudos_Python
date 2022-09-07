'''Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.'''

total_alunos = 0

quantidade_turmas = int(input('Informe a quantidade de turmas no colégio: '))
for turma in range(1, quantidade_turmas + 1):
    alunos_por_turma = int(input(f'Informe a quantidade de alunos na {turma}º turma: '))

    while alunos_por_turma > 40:
        print('Não é permitido mais de 40 alunos por turma.')
        alunos_por_turma = int(input(f'Informe a quantidade de alunos na {turma}º turma: '))

    total_alunos += alunos_por_turma

media_alunos_por_turma = total_alunos / quantidade_turmas
print(f'A média de alunos por turma é: {media_alunos_por_turma:.1f}')
