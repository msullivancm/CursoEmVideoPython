velo = float(input('Informe a velocidade: Km'))
multa = (velo - 80.0)*7.0
if velo >= 80.0:
    print('Você voi multado. Sua velocidade está {:.2f}Km acima do limite de velocidade. \nSua multa custa R${:.2f}'.format(velo-80.0, multa))
else:
    print('Parabéns, sua velocidade foi {:.2f}Km você está dentro do limite de velocidade.'.format(velo))
