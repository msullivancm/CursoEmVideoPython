from datetime import datetime
anoatual=int(datetime.now().year)
funcionario = dict()
funcionario['nome'] = input('Nome: ')
ano = int(input('Ano de Nascimento: '))
funcionario['idade'] = anoatual - ano
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps != 0:
    funcionario['ctps'] = ctps
    funcionario['contratacao'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salário: R$ '))
    funcionario['aposentadoria'] = funcionario['idade'] + (funcionario['contratacao'] + 35) - datetime.now().year
print('=-'*30)
print(funcionario)
for k, v in funcionario.items():
    print(f'    -{k} tem valor {v}')
