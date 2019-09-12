frase = 'Curso em Video Python'
print(frase)
print(frase[9])
print(frase[9:13])
print(frase[9:14])
print(frase[9:21])
print(frase[9:21:2]) #saltando de 2 em 2
print(frase[:5]) #quando o início é omitido, começa do 0. Sempre ultimo menos 1. pois o ultimo não entra.
print(frase[15:]) #quando omite o ultimo, vai até o final
print(frase[9::3]) #vai até o final pulando de 3 em 3
print(frase[::2]) #não informa nem inicio nem final e pula de 2 em dois
print(len(frase)) #mostra o comprimento da frase
print(frase.count('o')) #o python conta quantos 'o' tem na frase
print(frase.count('o', 0, 13)) #conta somente do trexo fatiado. lembrando que o ultimo valor -1
print(frase.upper().count('O')) #primeiro maiusculo e depois conta os Os maiusculos
print(frase.find('deo')) #procura a sequencia de caracter na variavel. Retorna o id de inicio onde achou a string.
print(frase.lower().find('curso'))
print(frase.find(("android"))) #Se não encontrar retorna -1.
print('Curso' in frase) #A palavra está contida em frase. Deveria retornar true ou false
print(frase.replace('Python','Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip()) #igual ao AllTrim
print(frase.rstrip()) #tipo o RTrim
print(frase.lstrip()) #tipo o LTrim
print(frase.split()) #por padrão ele considera os espaços para criar a divisão, retornando uma lista.
print(frase.split('o')) #dessa forma usamos o "o" como separador ao invés do espaço padrão
print('-'.join(frase)) #utiliza o "-" para unir cada um caracter da variável frase
print("""Criar um texto muito grande
com quebra de linha
que vai aparecer como formatado por causa
das 3 aspas""")
dividido = frase.split()
print(dividido[0])
print(dividido[2][3]) #pega o segundo elemento da lista na posição 3
