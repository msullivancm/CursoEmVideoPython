#jogadores = [{'nome': 'Joelson', 'gols': [3, 2], 'total': 5}, {'nome': 'Pedrão', 'gols': [2, 0, 4], 'total': 6}, {'nome': 'Wesley', 'gols': [0, 0, 0, 0], 'total': 0}]
jogador=dict()
jogadores=list()
continua = 's'
while continua != 'n':
    jogador['nome']= input('Nome do Jogador: ')
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = list()
    tot = 0
    for j in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {j}? ')))
        tot += jogador['gols'][j]
    jogador['total'] = tot
    jogadores.append(jogador.copy())
    continua = input('Quer continuar? [S/N]').lower()
print('=-'*20)
print(jogadores)
print('{:>3} {:<10} {:<20} {:<20}'.format('Cod', 'Nome', 'Gols', 'Total'))
print('-'*42)
for i, j in enumerate(jogadores):
    print('{:>3} {:<10} {:<20} {:<20}'.format(i, j['nome'], str(j['gols']), str(j['total'])))
mostrar = 's'
while mostrar != 'n':
    jog= int(input(f'Mostrar dados de qual jogador? (999 para finalizar)'))
    if jog == 999:
        break
    else:
        if jog >= len(jogadores):
            print(f'Erro! Não existe jogador com código {jog}! Tente novamente')
        else:
            print(f'-- Levantamento do jogador {jogadores[jog]["nome"]}:')
            for i, j in enumerate(jogadores[jog]['gols']):
                print(f'    No jogo {i} fez {j} gols.')
print('<<< Volte Sempre >>>')
