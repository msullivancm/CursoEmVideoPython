from random import choice

nome1 = input('Informe o número 1: ')
nome2 = input('Informe o numero 2: ')
nome3 = input('Informe o numero 3: ')
nome4 = input('Informe o numero 4: ')
lista = [nome1, nome2, nome3, nome4]
sorteio = choice(lista)
print('O aluno escolhido foi: {}'.format(sorteio))

