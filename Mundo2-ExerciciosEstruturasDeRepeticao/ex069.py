maiores = homens = mulheres20 = 0
while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]').upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres20 += 1
    continua = input('Deseja continuar? [S/N]').upper()
    if continua == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores}\nAo todo temos {homens} homens cadastrados.\nE temos {mulheres20} mulheres com menos de 20 anos')