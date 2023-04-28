from math import hypot

catetoOposto = float(input("Informe o cateto oposto: "))
catetoAdja = float(input("Informe o cateto adjacente: "))

hipotenusa = hypot(catetoOposto, catetoAdja)

print(f'{hipotenusa:.2f}')