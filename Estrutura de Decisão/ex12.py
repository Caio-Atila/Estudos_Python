'''Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
    Salário Bruto até 900 (inclusive) - isento
    Salário Bruto até 1500 (inclusive) - desconto de 5%
    Salário Bruto até 2500 (inclusive) - desconto de 10%
    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.'''

valor_hora = float(input('Informe o valor da sua hora R$: '))
horas_trabalhadas = int(input('Informe a quantidade de horas trabalhadas no mês: '))
salario = valor_hora * horas_trabalhadas
fgts = salario * 0.11
inss = salario * 0.10
imposto_renda = 0
n_imposto = 0

if salario <= 900:
    imposto_renda = salario * 0
    n_imposto = 0
elif 1500 >= salario > 900:
    imposto_renda = salario * 0.05
    n_imposto = 5
elif 2500 >= salario > 1500:
    imposto_renda = salario * 0.10
    n_imposto = 10
else:
    imposto_renda = salario * 0.20
    n_imposto = 20

print('=' * 35)
print(f'''Salário Bruto:............R${salario:.2f}
(-) IR ({n_imposto}%):..............R${imposto_renda:.2f}
(-) INSS (10%):...........R${inss:.2f}
FGTS (11%):...............R${fgts:.2f}
Total de descontos:.......R${imposto_renda + inss:.2f}
Salário Líquido:..........R${(salario - imposto_renda) - inss:.2f}''')
