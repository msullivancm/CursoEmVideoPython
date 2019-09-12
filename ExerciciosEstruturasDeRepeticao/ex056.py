idademaior = 0
mulheresnovas = 0
idades = 0
for i in range(0, 4):
    nome = input('Informe o nome: ')
    idade = int(input('Informe a idade: '))
    sexo = input('Informe o sexo. M para masculino e F para feminino: ')
    idades += idade
    if sexo.upper() == 'M' and idade > idademaior:
        maisvelho = nome
    if sexo.upper() == 'F' and idade < 20:
        mulheresnovas += 1
print('A média de idade do grupo é {}, o homem mais velho é {} e {} mulheres abaixo de 20 anos'.format(idades/4, maisvelho, mulheresnovas))
