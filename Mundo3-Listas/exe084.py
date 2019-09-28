pessoas = list()
pessoa = list()
while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()

    continuar = ''
    while continuar not in ('s','n'):
        continuar = input('Quer continuar? [S/N]').lower()
    if continuar == 'n':
        break

totmaior = totmenor = 0.0
for i in pessoas:
    if totmaior == 0 or i[1] > totmaior:
        totmaior = i[1]
    if totmenor == 0 or i[1] < totmenor:
        totmenor = i[1]

print('=-'*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {totmaior:.2f}. Peso de ', end=' ')
for p in pessoas:
    if p[1] == totmaior:
        print(f'[{p[0]}]', end=' ')
print(f'\nO menor peso foi de {totmenor:.2f}. Peso de ', end=' ')
for p in pessoas:
    if p[1] == totmenor:
        print(f'[{p[0]}]', end=' ')
