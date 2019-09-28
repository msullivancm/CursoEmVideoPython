matriz = [[],[],[]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))

print('=-'*30)
print(f'[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]')
print(f'[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]')
print(f'[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]')
