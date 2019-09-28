lista = list()
maior = 0
menor = 0
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        c = 0
        while c <= len(lista):
            if valor <= lista[c]:
                lista.insert(c, valor)
                print(f'Adicionado na posição {c}')
                break
            c += 1

print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')