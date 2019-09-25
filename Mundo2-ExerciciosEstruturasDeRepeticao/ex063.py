n = int(input('Informe o número da sequencia fibonacci a ser exibido: '))
fibo=''
a = 0
b = 1
fibo=str(a)
while (b < n):
    c = a
    a = b
    b = c + b
    fibo = fibo + '->' + str(a)
print(fibo)
