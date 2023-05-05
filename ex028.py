import random 

from time import sleep

print('Estou pensando em um número entre 0 a 5. tente adivinhar✨')

playerNumber = int(input('Digite: '))

pcNumber = int(random.uniform(0, 6))
# SOLUÇÃO DO CURSO FOI 
# pcNumber = int(random.randint(0,5))
print('PROCESSANDO....')
sleep(3)


if playerNumber == pcNumber:
    print('Parabéns você acertou!!!')
else:
    print(f'Você errou tente novamente, estava pensando no número {pcNumber}')


