nome = input('Digite seu nome completo: ')
if nome.lower().find('silva')>0:
    print("Seu nome tem Silva.")
else:
    print("Seu nome não tem Silva.")
#ou
print('='*20)
print('silva' in nome.lower())