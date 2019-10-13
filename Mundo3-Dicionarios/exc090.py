aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media']>=7.0:
    aluno['situcao'] = 'Aprovado'
elif 5.0 <= aluno['media'] < 7.0:
    aluno['situcao'] = 'Recuperação'
else:
    aluno['situcao'] = 'Reprovado'
for k, v in aluno.items():
    print(f'    -{k} é igual a {v}')
