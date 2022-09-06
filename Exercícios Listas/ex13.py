'''Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).'''

media_temperaturas_por_mes: list = []
meses_por_extenso: list = [
    'janeiro', 'fevereiro', 'março', 
    'abril', 'maio', 'junho', 
    'julho', 'agosto', 'setembro', 
    'outubro', 'novembro', 'dezembro'
]

for mes in range(1, 13):
    temperatura_media = float(input(f'Informe a média de temperatura do {mes}º mês: '))
    media_temperaturas_por_mes.append(temperatura_media)

media_anual_temperatura: float = sum(media_temperaturas_por_mes) / len(media_temperaturas_por_mes)
temperaturas_meses: list = list(zip(media_temperaturas_por_mes, meses_por_extenso))

print(f'Meses com temperatura acima da média anual ({media_anual_temperatura:.1f}ºC):')
for posição, registro in enumerate(temperaturas_meses):
    temp_media, mes = registro
    if temp_media > media_anual_temperatura:
        print(f'{posição}º {mes} - Temperatura média: {temp_media}')
