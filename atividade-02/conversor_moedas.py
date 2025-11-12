# Conversor de moedas
""""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

"""

print("Conversor de Moedas")

entrada = float(input("Entre o valor em Reais R$ a ser convertido-> "))

tx_dolar = float(input("Entre o valor da dólar -> "))
tx_euro = float(input("Entre o valor do euro -> "))

valor_dolar = entrada / tx_dolar
valor_euro = entrada / tx_euro

print(f"O valor de R$ {entrada:.2f} em dólar é U$ {valor_dolar:.2f}")
print(f"O valor de R$ {entrada:.2f} em euro é EU$ {valor_euro:.2f}")



