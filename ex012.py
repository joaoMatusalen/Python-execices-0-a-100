produto = float(input("Qual é o valor do produto? R$"))

desconto = 10

produtoDesconto = produto * desconto / 100

print(f'O produto com {desconto}% de desconto vai custar de R${produto} para R${produto - produtoDesconto:.2f}')

