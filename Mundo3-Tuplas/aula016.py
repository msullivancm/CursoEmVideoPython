lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Vou comer {comida}')
print('-'*20)
for cont in range(0, len(lanche)):
    print(f'Vou comer {lanche[cont]} na posição {cont}')
print('-'*20)
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {pos}')
print('-' * 20)
print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(c.count(5)) #Conta quantos números existe na tupla
print(c.index(8)) #Exibe a posição da primeira ocorrência do número
del(c) #apaga a tupla interia da memoria