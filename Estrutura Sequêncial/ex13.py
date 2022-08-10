#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('Informe altura: '))
homem_peso = (72.7 * altura) - 58
mulher_peso = (62.1 * altura) - 44.7

print(f'O peso ideal para homens é: {homem_peso:.1f}')
print(f'O peso ideal para mulheres é: {mulher_peso:.1f}')
