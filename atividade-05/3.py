# Calculadora Preço Final

"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.

"""

def preco_desconto(preco_produto, desconto):
  return preco_produto * desconto / 100.00

def preco_final(preco_inicial, preco_desconto):
  return preco_inicial - preco_desconto

def main():
  print(f"\nCalculadora do Preço Final do Produto com desconto\n")
  while(True):
    try:
      preco = float(input(f"Entre o preço do produto -> "))
      
    except ValueError:
      print("Tente entrar apenas dados numéricos")
    try:
      desconto = float(input("Entre o desconto a ser aplicado em % "))
      
    except ValueError:
      print("Tente entrar apenas dados numéricos")
    break

  desconto_dado = preco_desconto(preco, desconto)
  total = preco_final(preco, desconto_dado)

  print("\n***********************************\n")
  print(f"Preço do produto sem desconto R$ {preco:.2f}")
  print(f"Desconto de {desconto:.2f} % aplicado")
  print(f"Valor do desconto R$ {desconto_dado:.2f} reais")
  print(f"Preço final R$ {total:.2f} reais")

if __name__ == "__main__":
    main()

