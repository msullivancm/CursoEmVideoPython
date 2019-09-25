palavras = ('cagar', 'peidar', 'programar', 'fecundar', 'praticar')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    vog = ""
    for i in p:
        if i in vogais:
            vog += f'{i} '
    print(f'Na palavra {p} temos {vog}')
