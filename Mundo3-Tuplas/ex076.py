lista = ('Arroz', 10.50, 'feijão', 3.9, 'Alho', 5.0)
for i in range(0, len(lista), 2):
    print(f'Produto {lista[i]:-<20} Preço R$ {lista[i + 1]:.2f}')
