nome = str(input('Qual é o seu nome completo? ').strip())
nomeSeparado = nome.split()
nomeNoSpace = ''.join(nomeSeparado)

print('Analisando seu nome....')

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()} ')

print(f'Seu nome tem ao todo: {len(nomeNoSpace)} letras')
print(f'Seu primeiro nome tem {len(nomeSeparado[0])} letras')