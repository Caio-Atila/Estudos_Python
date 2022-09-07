'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.'''

valores_1: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_2: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_3: list = []

lista_guia = list(zip(valores_1, valores_2))
for dupla in lista_guia:
    num1, num2 = dupla
    valores_3.append(num1)
    valores_3.append(num2)

print(valores_3)
