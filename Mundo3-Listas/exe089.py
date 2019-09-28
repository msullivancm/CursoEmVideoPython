aluno = list()
alunos = list()
while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    alunos.append([nome, [nota1, nota2], media])
    cont = input('Quer continuar?').lower()
    if cont in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-'*30)
for cont, a in enumerate(alunos):
    print(f'{cont:<4}{a[0]:10}{a[2]:>8.1f}')
print('-'*30)
num = 0
while num != 999:
    num = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if num != 999:
        print(f'Notas de {alunos[num][0]} são {alunos[num][1]}')
print(f'Finalizado...')
print(f'{"VOLTE SEMPRE":=^30}')