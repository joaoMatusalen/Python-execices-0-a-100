import math

angulo = float(input('Digite um ângulo qualquer: '))

seno = math.sin(math.radians(angulo))

cosseno = math.cos(math.radians(angulo))

tangente = math.tan(math.radians(angulo))

print(f'{seno:.2f}')
print(f'{cosseno:.2f}')
print(f'{tangente:.2f}')

