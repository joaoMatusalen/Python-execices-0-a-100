from random import choice

aluno1 = input('Escreva o nome do primerio aluno: ')

aluno2 = input('Escreva o nome do segundo aluno: ')

aluno3 = input('Escreva o nome do treceiro aluno: ')

aluno4 = input('Escreva o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido foi: {choice(alunos)}')

