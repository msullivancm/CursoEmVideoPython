continua = 's'
while True:
    teste = input('Teste ou a vera? [T/V]').lower()
    if teste in 'tv':
        break
    print('Digite apenas T ou V.')
if teste == 't':
    pessoas=[{'nome': 'Monica', 'sexo': 'F', 'idade': 40}, {'nome': 'Pedro', 'sexo': 'M', 'idade': 22}, {'nome': 'Maria', 'sexo': 'F', 'idade': 33}, {'nome': 'Paula', 'sexo': 'F', 'idade': 12}]
else:
    pessoa = dict()
    pessoas = list()
    while continua != 'N':
        pessoa['nome'] = input('Nome: ')
        while True:
            pessoa['sexo'] = input('Sexo: [M/F]').upper()
            if pessoa['sexo'] in 'MF':
                break
            print('Erro! Digite apenas M ou F.')
        pessoa['idade'] = int(input('Idade: '))
        pessoas.append(pessoa.copy())
        while True:
            continua = input('Quer continuar? [S/N]').upper()
            if continua in 'SN':
                break
            print('Erro! Digite apenas S ou N.')
print('=-'*20)
print(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
totidade = 0
for p in pessoas:
    totidade += p['idade']
mediaidade = totidade/len(pessoas)
print(f'- A média de idade é de {mediaidade:5.2f} anos.')
mulheres = ''
for p in pessoas:
    if p['sexo'] == 'F':
        mulheres += p['nome'] + ' '
print(f'- As mulhers cadastradas foram: {mulheres}')
print(f'- Lista de pessoas que estão acima da média: ')
for p in pessoas:
    if p['idade'] > mediaidade:
        for k, v in p.items():
            print(f'{k} = {v}', end='; ')
        print()
print('<<ENCERRADO>>')
