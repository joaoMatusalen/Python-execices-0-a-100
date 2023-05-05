from datetime import date

ano = int(input('Escreva um número para analisar (0 para o ano atual): '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} bixesto')
else:
    print(f'Ano {ano} não bixesto')