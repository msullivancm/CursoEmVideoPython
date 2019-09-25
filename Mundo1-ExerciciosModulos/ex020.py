from random import shuffle
n1 = input('Informe o primeiro nome: ')
n2 = input('segundo nome: ')
n3 = input('terceiro: ')
n4 = input('quarto: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print("A ordem de apresentação é: {}".format(lista))
