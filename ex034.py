salario = float(input('Qual é o salario do funcionario? '))

if salario <= 1250.00:
    aumento = (salario / 100) * 15 + salario
else:
    aumento = (salario / 100) * 10 + salario
print(f'O aumento de salario foi de R${salario} para R${aumento:.2f}')
