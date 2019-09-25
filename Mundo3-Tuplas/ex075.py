n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
n4 = int(input('Digite o quarto valor: '))
tupla = (n1, n2, n3, n4)
nove = tupla.count(9)
if tupla.count(3) > 0:
    tres = tupla.index(3)
else:
    tres = 0
pares = ''
for i in tupla:
    if i % 2 == 0:
        pares += str(i) + ' '
print(f'O valor 9 apareceu {nove} vezes.')
print(f'O valor 3 foi digitado na posição {tres}')
print(f'Os números pares são: {pares}')