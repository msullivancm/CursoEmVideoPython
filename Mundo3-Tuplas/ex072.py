contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
num = 0
num = int(input('Informe um número de 0 a 10: '))
while num not in range(0, 11):
    num = int(input('Tente novamente. Informe um número de 0 a 10: '))
print(f'Seu número é: {contagem[num]}')