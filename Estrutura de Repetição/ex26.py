'''Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.'''

quantidade_eleitores = int(input('Informe a quantidade de eleitores: '))
votos_candidato_a = 0
votos_candidato_b = 0
votos_candidato_c = 0

for eleitor in range(1, quantidade_eleitores + 1):
    opção_voto_eleitor = int(input(f'''Eleitor nº{eleitor} escolha sua opção de voto: 
- [1] Candidato A
- [2] Candidato B
- [3] Candidato C
Digite aqui: '''))
    print('-' * 39)

    while opção_voto_eleitor < 1 or opção_voto_eleitor > 3:
        print('Opção de voto inválida. Tente novamente')
        opção_voto_eleitor = int(input(f'''Eleitor nº{eleitor} escolha sua opção de voto: 
- [1] Candidato A
- [2] Candidato B
- [3] Candidato C
Digite aqui: '''))
        print('-' * 39)
    
    if opção_voto_eleitor == 1:
        votos_candidato_a += 1
    elif opção_voto_eleitor == 2:
        votos_candidato_b += 1
    else:
        votos_candidato_c += 1

print(f'''Contagem de votos: 
Candidato A: {votos_candidato_a} voto(s)
Candidato B: {votos_candidato_b} voto(s)
Candidato C: {votos_candidato_c} vato(s)''')
