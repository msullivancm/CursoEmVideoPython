from random import randrange
menor = maior = 0
tupla = (randrange(100), randrange(100), randrange(100), randrange(100), randrange(100))
print(tupla)
for t in tupla:
    if t < menor or menor == 0:
        menor = t
    if t > maior or maior == 0:
        maior = t
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')