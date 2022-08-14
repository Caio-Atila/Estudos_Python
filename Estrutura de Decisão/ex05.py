'''Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

nota1 = float(input('Informe a 1º nota: '))
nota2 = float(input('Informe a 2º nota: '))
media = (nota1 + nota2) / 2

print(f'Média: {media:.2f}')
if media == 10:
    print('Situação: APROVADO COM DISTINÇÃO')
elif 10 > media >= 7:
    print('Situação: APROVADO')
else:
    print('Situação: REPROVADO')
