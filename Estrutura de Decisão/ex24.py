'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.'''

num = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

resultado = 0
opção_operação = int(input('''Informe qual operação deseja realizar: 
[1] Soma
[2] Subtração
[3] Multiplicação
[4] Divisão
digite aqui sua opção: '''))

#menu
if opção_operação == 1:
    resultado = num + num2
    print(f'{num} + {num2} = {resultado}')
elif opção_operação == 2:
    resultado = num - num2
    print(f'{num} - {num2} = {resultado}')
elif opção_operação == 3:
    resultado = num * num2
    print(f'{num} x {num2} = {resultado:.1f}')
elif opção_operação == 4:
    resultado = num / num2
    print(f'{num} / {num2} = {resultado}')
else:
    print('Operação inválida')
    exit()

#Visualização de resultados
print('=' * 25)
print(f'{resultado} é PAR' if resultado % 2 == 0 else f'{resultado} é IMPAR')

print(f'{resultado} é DECIMAL' if round(resultado) - resultado != 0 \
else f'{resultado} é INTEIRO')

if resultado > 0:
    print(f'{resultado} é POSITIVO')
elif resultado < 0:
    print(f'{resultado} é NEGATIVO')
else:
    print(f'{resultado} é igual a ZERO')
