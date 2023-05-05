kmViagem = float(input('Qual é a distância da viagem? '))

if kmViagem < 200:
    passagem = kmViagem * 0.50
    print(f'A viagem com a distância de {kmViagem}Km irá custar R${passagem:.2f}, Boa viagem!!!')
else:
    passagem = kmViagem * 0.45
    print(f'A viagem com a distância de {kmViagem}Km está com um preço promocional e irá custar R${passagem:.2f}, Boa viagem!!!')