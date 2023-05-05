nome = str(input('Qual é o seu nome completo? ').lower().strip())

## Fiz dessa maneira
print(nome.find('silva') != -1)

## Resolução do curso em video
print('silva' in nome)
