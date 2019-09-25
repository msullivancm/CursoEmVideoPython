fim = 0
while fim != 1:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    opcao = int(input('Digite: \n[1]somar \n[2]multiplicar \n[3]maior \n[4]novos números \n[5]sair do programa'))
    if opcao == 1:
        print('A soma de {} e {} é igual a {}'.format(n1,n2,n1+n2))
        fim = 0
    elif opcao == 2:
        print('A multiplicação de {} e {} é igual a {}'.format(n1, n2, n1 * n2))
        fim = 0
    elif opcao == 3:
        maior = 0
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número entre {} e {} é {}'.format(n1, n2, maior))
        fim = 0
    elif opcao == 4:
        fim = 0
    elif opcao == 5:
        fim = 1
        break
print('Programa terminado.')