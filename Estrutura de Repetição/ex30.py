'''O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
    Preço do pão: R$ 0.18
    Panificadora Pão de Ontem - Tabela de preços
    1 - R$ 0.18
    2 - R$ 0.36
    ...
    50 - R$ 9.00'''

print('Panificadora Pão de Ontem - Tabela de preços')

preço = float(input('Informe o preço do pão R$: '))
valor_unidade_pão = preço

for unidade in range(1, 51):
    valor_unidade_pão *= unidade
    print(f'{unidade:<2} - R${valor_unidade_pão:<6.2f}|', end='')
    valor_unidade_pão = preço

    if unidade % 5 == 0:
        print()
