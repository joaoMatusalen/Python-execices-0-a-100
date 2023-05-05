nome = str(input('Qual é o seu nome completo? ')).strip()

nomeSeparado = nome.split()

print(f'Seu primeiro nome é: {nomeSeparado[0]}')

print(f'Seu ultimo nome é: {nomeSeparado[len(nomeSeparado) - 1]}')

