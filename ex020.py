from random import shuffle

lider1 = input('Escreva o nome do represantante do primeiro grupo: ')

lider2 = input('Escreva o nome do represantante do segundo grupo: ')

lider3 = input('Escreva o nome do represantante do terceiro grupo: ')

lider4 = input('Escreva o nome do represantante do quarto grupo: ')

grupos = [lider1, lider2,  lider3, lider4]
shuffle(grupos)


print(f'A sequência de apresentação ficará: \n{grupos}')