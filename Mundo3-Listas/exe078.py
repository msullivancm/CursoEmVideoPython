lista = list()
maior = 0
menor = 0
for l in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {l}: ')))
    if lista[l] > maior or maior == 0:
        maior = lista[l]
    if lista[l] < menor or menor == 0:
        menor = lista[l]
print('=-'*30)
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {maior} nas posições ', end=' ')
for cont, elemento in enumerate(lista):
    if elemento == maior:
        print(f'{cont}...', end=' ')
print(f'\nO menor valor digitado foi {menor} nas posições ', end=' ')
for cont, elemento in enumerate(lista):
    if elemento == menor:
        print(f'{cont}...', end=' ')