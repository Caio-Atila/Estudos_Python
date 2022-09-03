'''Faça um programa que calcule o mostre a média aritmética de N notas.'''

soma_notas: float = 0.0
media: float = 0.0
quantidade_notas: int = 0

while True:
    soma_notas += float(input('Digite a nota do aluno: '))
    quantidade_notas += 1
    
    continuar_programa: str = input('Continuar [s/n]: ').strip().lower()[0]
    if continuar_programa == 'n':
        media = soma_notas / quantidade_notas
        break

print('-' * 27)
print(f'Média aritmética das notas: {media:.1f}')
