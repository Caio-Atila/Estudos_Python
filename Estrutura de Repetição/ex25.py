'''Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.'''

soma_idades: int = 0
quantidade_idades: int = 0
media_idades: float = 0.0

while True:
    soma_idades += int(input('Digite a idade da pessoa: '))
    quantidade_idades += 1 

    continuar_programa: str = input('Continuar [s/n]: ').strip().lower()[0]
    if continuar_programa == 'n':
        media_idades = soma_idades / quantidade_idades
        break

print('-' * 25)
if media_idades <= 25:
    print(f'Média de idades: {media_idades:.1f}')
    print('Grupo composto em maioria por: JOVENS')
elif 25 < media_idades <= 60:
    print(f'Média de idades: {media_idades:.1f}')
    print('Grupo composto em maioria por: ADULTOS')
else:
    print(f'Média de idades: {media_idades:.1f}')
    print('Grupo composto em maioria por: IDOSOS')
