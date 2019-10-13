def titulo(tit):
    print('-' * 30)
    print(f'{tit.upper():^30} ')
    print('-' * 30)


def soma(a, b):
    print(f'A é igual a {a} e B é igual a {b}')
    s = a + b
    print(f'A soma é {s}')


def contador(*num):
    print(f' Os valores {num}, são {len(num)} números.')


def dobra(lst):
    for i, v in enumerate(lst):
        lst[i] = v * 2


titulo('Curso em Vídeo')
titulo('Aprenda Python')
titulo('Gustavo Guanabara')

soma(4, 5)
soma(a=4, b=5)
soma(a=5, b=4)

# Empacotamento de parâmetros
contador(2, 5, 3, 5, 7)
contador(2, 5, 3)
contador(5, 1, 2, 6, 6, 2)

lista = [2, 5, 5, 6, 7, 7]
print(lista)
dobra(lista)
print(lista)
