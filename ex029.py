velCarro = float(input('Qual é a velocida do carro agora? '))


if velCarro <= 80:
    print(f'Continue dirigindo com segurança. {velCarro:.0f}Km do limite de 80Km')
else:
    multa = (velCarro - 80) * 7
    print( f'Você está muito rápido na via!!! DIMUNUA A VELOCIDADE!!! \nVocê está há{velCarro:.0f}Km e levou uma multa de R${multa}')