'''Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.'''

while True: 
    pais_a = int(input('Informe o número de habitantes da população A: '))
    pais_b = int(input('Informe o número de habitantes da população B: '))
    porcentagem_crescimentoA = float(input('Informe a taxa de crescimento anual da população A: '))
    porcentagem_crescimentoB = float(input('Informe a taxa de crescimento anual da população B: '))
    anos_necessarios = 0
    
    continuar = 's'
    while continuar == 's':
        for c in range(1, 6):
            print(f'{anos_necessarios}º Ano: País A: {pais_a:.0f} |País B: {pais_b:.0f}')
            taxa_crescimento_paisA = (pais_a * porcentagem_crescimentoA) / 100
            pais_a += taxa_crescimento_paisA
            taxa_crescimento_paisB = (pais_b * porcentagem_crescimentoB) / 100
            pais_b += taxa_crescimento_paisB
            anos_necessarios += 1
        continuar = input('Deseja continuar a simulação [s/n]: ').strip().lower()[0]
        if continuar == 'n':
            break
    
    print(f'Após {anos_necessarios} anos segue a abaixo o número de habitantes estimados')
    print(f'População atual do país A: {pais_a:.0f} habitantes')
    print(f'População atual do país B: {pais_b:.0f} habitantes')
    sair = str(input('Deseja sair do programa [s/n]: ')).strip().lower()[0]
    if sair == 's':
        print('Programa encerrado.')
        exit()
