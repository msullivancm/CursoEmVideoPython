vlrCasa = float(input('Informe o valor da casa R$:'))
vlrSalario = float(input('Informe o valor do salário R$: '))
anos = int(input('Informe em quantos anos vai pagar: '))
tempoEmMeses = anos * 12
mensalidade = vlrCasa / tempoEmMeses
if mensalidade > vlrSalario*0.30:
    print('Emprestimo negado. Sua prestação seria de R${:.2f} em {} meses.'.format(mensalidade, tempoEmMeses))
else:
    print('Sua prestação será de R${:.2f} que deverá ser paga em {} meses'.format(mensalidade, tempoEmMeses))
