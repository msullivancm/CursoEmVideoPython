aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Média é igual a {aluno["media"]}')
if aluno['media']>=5.0:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')