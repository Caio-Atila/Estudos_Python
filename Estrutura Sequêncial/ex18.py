'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).'''

tamanho_arquivo = float(input('Informe o tamanho do arquivo (MB): '))
velocidade_internet = float(input('Informe sua velocidade de internet (Mbps): '))

conversao_dados = velocidade_internet / 8
download_segundo = tamanho_arquivo / conversao_dados
download_minuto = download_segundo / 60

print('=' * 26)
print(f'{conversao_dados} megabytes por segundo')
print(f'Tempo de download: {download_minuto:.1f}min')
