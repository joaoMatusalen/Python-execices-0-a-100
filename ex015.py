carroDia = int(input('Quantos dias você alugou o seu carro? '))
carroKm = float(input('Quantos KM você percorreu? '))

valorPagar = (60 * carroDia) + (0.15 * carroKm)

print(f'Você deve pagar R${valorPagar:.2f} por {carroDia} dia(s) e por {carroKm} KM rodado.')