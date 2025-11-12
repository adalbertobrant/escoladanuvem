# Calculadora de Consumo

"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""

print("Calculadora de Consumo de Combustível")

distancia = float(input("Entre a distância percorrida -> "))
combustivel = float(input(f"Entre a quantidade de combustível gasta para percorrer {distancia:.2f} -> "))

gasto = distancia / combustivel

print(f"\nO veículo percorreu {distancia:.2f} km com {combustivel:.2f} l e teve um consumo médio de {gasto:.2f} km/l")

