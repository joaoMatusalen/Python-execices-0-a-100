paredeAltura = float(input('Qual é a altura da sua parede? '))
paredeLargura = float(input('Qual é a largura da sua parede? '))
paredeCompleta = paredeAltura * paredeLargura
lataDeTinta = 2.000

print(f'Sua área de parede é {paredeAltura}x{paredeLargura} = {paredeCompleta:.3f}metros quadrados.')
print(f'Você vai precisar de {paredeCompleta / 2.000:.4f}L de tinta para pintar sua parede.')