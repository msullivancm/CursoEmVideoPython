matriz = [[],[],[]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('=-'*30)
print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]')
print('=-'*30)
totpares = 0
for l in range(0,3):
    for c in range(0,3):
        if matriz[l][c] % 2 == 0:
            totpares += matriz[l][c]
print(f'A soma dos valores pares é {totpares}')

tot3col = 0
for l in range(0,3):
    tot3col += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {tot3col}')

maior2lin = 0
for c in range(0,3):
    if matriz[1][c] > maior2lin:
        maior2lin = matriz[1][c]
print(f'O maior valor da segunda linha é {maior2lin}')