salario = float(input("Qual é o salario do funcionario? R$"))

aumento = 15

salarioAumento = salario * aumento / 100

print(f'O salarico com {aumento}% de aumento vai de R${salario} para R${salario + salarioAumento:.2f}')

