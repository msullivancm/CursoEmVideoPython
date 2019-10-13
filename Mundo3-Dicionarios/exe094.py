continua = 's'
#pessoas=[{'nome': 'Monica', 'sexo': 'F', 'idade': 40}, {'nome': 'Pedro', 'sexo': 'M', 'idade': 22}, {'nome': 'Maria', 'sexo': 'F', 'idade': 33}, {'nome': 'Paula', 'sexo': 'F', 'idade': 12}]
pessoa = dict()
pessoas = list()
while continua != 'n':
    pessoa['nome'] = input('Nome: ')
    pessoa['sexo'] = input('Sexo: ').upper()
    pessoa['idade'] = int(input('Idade: '))
    pessoas.append(pessoa.copy())
    continua = input('Quer continuar? [S/N]').lower()
print('=-'*20)
print(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
totidade = 0
for p in pessoas:
    totidade += p['idade']
mediaidade = totidade/len(pessoas)
print(f'- A média de idade é de {mediaidade} anos.')
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
