'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.'''

wage = float(input('Informe seu salário R$: '))
increase = 0
increase_wage = 0
if 0 < wage <= 280:
    increase = 20
    increase_wage = wage * 0.20
elif 700 >= wage > 280:
    increase = 15
    increase_wage = wage * 0.15
elif 1500 >= wage > 700:
    increase = 10
    increase_wage = wage * 0.10
elif wage > 1500:
    increase = 5
    increase_wage = wage * 0.05

print('=' * 87)
print(f'Com base em seu salário atual você receberá um aumento de {increase}%. Correspondete a R${increase_wage:.2f}')
print(f'Salário atual: R${wage:.2f}')
print(f'Novo salário: R${wage + increase_wage:.2f}')
