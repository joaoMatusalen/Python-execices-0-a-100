valor = float(input('Escreva um valor em metros: '))

cm = 10**2 * (valor)
ml = 10**3 * (valor)

print('O valor convertido em {:.0f} cm, e milimetros {:.0f} mm'.format(cm, ml))