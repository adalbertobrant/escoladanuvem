# Calculadora de Desconto

"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

"""

print("CALCULADORA DESCONTO")

nome_produto = input("Informe nome do produto -> ")
preco_original = float(input(f"Entre o preço do {nome_produto} -> "))

desconto = 20/100

preco_descontado = preco_original * desconto

print(f"{nome_produto}")
print(f"Parabéns você ganhou um desconto de R$ {preco_descontado:.2f}")
print(f"Preço final do {nome_produto} é de R$ {(preco_original - preco_descontado):.2f}")


