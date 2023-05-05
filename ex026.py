frase = str(input('Digite uma frase: ').lower().strip())


print(f'A letra A aparece {frase.count("a")}')
print(f'A primeira letra A aparece na posição: {frase.find("a") + 1}')
print(f'A ultima letra A aparece na posição: {frase.rfind("a") + 1}')