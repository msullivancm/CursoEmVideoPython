algo = input('Digite algo: ')
print('O tipo de {} é {}'.format(algo, type(algo)))
print('{} é número? {}'.format(algo, algo.isalnum()))
print('{} é alpha? {}'.format(algo, algo.isalpha()))
print('{} é alpha? {}'.format(algo, algo.isalphanum()))
print('{} é ascii? {}'.format(algo, algo.isascii()))
print('{} é decimal? {}'.format(algo, algo.isdecimal()))
print('{} é digito? {}'.format(algo, algo.isdigit()))
print('{} é identificador? {}'.format(algo, algo.isidentifier()))
print('{} é minúsculo? {}'.format(algo, algo.islower()))
print('{} é imprimível? {}'.format(algo, algo.isprintable()))
print('{} é espaço? {}'.format(algo, algo.isspace()))
print('{} é title? {}'.format(algo, algo.istitle()))
