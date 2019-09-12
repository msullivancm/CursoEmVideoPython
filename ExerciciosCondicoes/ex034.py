salario = float(input('Digite o salário R$: '))
if salario > 1250.00:
    print('Novo salário é de R${}'.format(salario+salario*0.10))
else:
    print('Novo salário é de R${}'.format(salario+salario*0.15))