"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. 
* Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3

* O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""
nome_do_produto = "Cadeira Infantil"
preco_unitario = 12.40
quantidade = 3
total = quantidade * preco_unitario

print(f"Preço total do produto -> {nome_do_produto}")
print(f"Nome do produto => {nome_do_produto}")
print(f"Preço Unitário => {preco_unitario:.2f}")
print(f"Quantidade => {quantidade}")
print(f"Total => R$ {total:.2f}")

