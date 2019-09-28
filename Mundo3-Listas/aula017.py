num = [2,5,9,1] #lista
print(num)
num[2]=3 #muda o valor da posição 2 com o conteúdo 3
num.append(7) #inclui, no ultimo o conteúdo 7
print(num)
num.sort(reverse=True) #ordena decrescente
print(num)
num.insert(2,0) #insere na posição 2 o conteúdo 0
print(num)
num.pop(5) #remove o conteúdo 5
print(num)
num.pop(2) #remove conteúdo do indice 2
print(num)
num.pop() #remove ultimo
print(num)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 5')
print(num)

for c, v in enumerate(num):
    print(f'na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

for cont in range(0,len(num)):
    num.append(int(input('Digite um valor: ')))
print(num)

a = [2, 3, 4, 7]
b = a #No pyton, quando uma lista é igualada a outra, elas apontam para o mesmo espaço de memória. Logo se alterar uma, a outra também é alterada.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

a = [2, 3, 4, 7]
b = a[:] #Nesse caso, os valores de a são incluídos em b. Não estão mais compartilhando memória.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')