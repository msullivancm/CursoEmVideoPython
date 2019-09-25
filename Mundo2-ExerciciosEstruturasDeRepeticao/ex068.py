from random import randrange
print('=-'*20)
print('Vamos jogar Par ou Impar')
print('=-'*20)
while True:
    n = int(input('Digite um valor: '))
    pi = input('Par ou ímpar? [P/I]')
    comp = randrange(0,10,1)
    total = (n + comp)
    if total % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {comp}. Total de {total} Deu PAR')
        if pi == 'P':
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
    else:
        print(f'Você jogou {n} e o computador jogou {comp}. Total de {total} Deu IMPAR')
        if pi == 'I':
            print('Você venceu!')
        else:
            print('Você perdeu!')
            break
