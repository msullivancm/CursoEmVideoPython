frase = input('Digite uma frase longa: ').strip() #para eliminar os espaços a esquerda ou a direita
contaLetra = frase.lower().count('a')
primeiraPosicao = frase.lower().find('a')
ultimaPosicao = frase.lower().rfind('a')
print('Sua fraze tem {} vezes a letra A, que aparece na primeira vez na posição {} e na última vez na posição {}'.format(contaLetra, primeiraPosicao, ultimaPosicao))