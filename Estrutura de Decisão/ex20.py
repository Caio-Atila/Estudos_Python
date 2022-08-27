'''Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
    A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
    A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
    A mensagem "Aprovado com Distinção", se a média for igual a 10.'''

nota1 = float(input('Digite a 1º nota: '))
nota2 = float(input('Digite a 2º nota: '))
nota3 = float(input('Digite a 3º nota: '))
media = (nota1 + nota2 + nota3) / 3

print(f'Média: {media:.1f}')
if 9.9 >= media >= 7:
    print('Situação: APROVADO')
elif media < 7:
    print('Situação: REPROVADO')
else:
    print('Situação: APROVADO COM DISTINÇÃO')
