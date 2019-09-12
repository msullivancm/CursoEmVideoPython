frase = input('Informe a frase a ser verificada: ').strip()
fraselimpa = frase.replace(' ', '')
aocontrario = ""
for i in range(len(fraselimpa)-1, -1, -1):
    aocontrario += fraselimpa[i]
if fraselimpa == aocontrario:
    print('Esta frase é um palíndromo!')
else:
    print('Esta frase não é um palíndromo!')

