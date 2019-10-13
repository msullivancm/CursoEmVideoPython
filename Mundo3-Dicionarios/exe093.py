jogador=dict()
jogador['nome']= input('Nome do Jogador: ')
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = list()
tot = 0
for j in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {j}? ')))
    tot += jogador['gols'][j]
jogador['total'] = tot
#jogador['total'] = sum(jogador['gols']) #o sum soma todos os valores do vetor
print('=-'*20)
print(jogador)
print('=-'*20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-'*20)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, g in enumerate(jogador['gols']):
    print(f'    => Na partida {i}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')