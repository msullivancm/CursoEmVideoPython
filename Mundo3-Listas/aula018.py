teste = []
teste.append('Gustavo')
teste.append(40)
print(teste)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
# quando a atribuição é da forma acima, o python identifica que estão compartilhando o mesmo espaço de memória. Logo são so mesmos valores.
# Por isso devemos utilizar a atribuição por [:]

galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria',45]]
print(galera[0])
print(galera[2][1]) #posição 2 de galera, posição 1 da lista dentro da posição 2
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')

galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(input('Nome: '))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menores de idade.')