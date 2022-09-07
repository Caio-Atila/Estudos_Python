'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.'''

valores_1: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_2: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_3: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valores_4: list = []

lista_guia = list(zip(valores_1, valores_2, valores_3))
for trio in lista_guia:
    num1, num2, num3 = trio
    valores_4.append(num1)
    valores_4.append(num2)
    valores_4.append(num3)

print(valores_4)