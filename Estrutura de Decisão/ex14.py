'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

nota1 = float(input('Informe a 1º nota: '))
nota2 = float(input('Informe a 2º nota: '))
media = (nota1 + nota2) / 2
conceito = ''
situação = ''

if media < 4:
    conceito = 'E'
    situação = 'Reprovado'
elif 6 > media >= 4:
    conceito = 'D'
    situação = 'Reprovado'
elif 7.5 > media >= 6:
    conceito = 'C'
    situação = 'Aprovado'
elif 9 > media >= 7.5:
    conceito = 'B'
    situação = 'Aprovado'
else:
    conceito = 'A'
    situação = 'Aprovado'

print(f'''Notas de Unidade: {nota1} | {nota2} 
Média de aproveitamento: {media:.1f}
Nota conceito: {conceito}
Situação: {situação}''')