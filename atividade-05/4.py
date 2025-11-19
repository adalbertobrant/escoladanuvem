# Função para transformar anos de vida em dias


from datetime import datetime

def dias_vida(dia, mes, ano_nascimento, dia_hoje):
  data = f"{dia}/{mes}/{ano_nascimento}"
  vida_inicial = datetime.strptime(data, "%d/%m/%Y")
  return dia_hoje - vida_inicial



def main():
  try:
    dia = int(input("Entre o seu dia de nascimento -> "))
    mes = int(input("Entre o seu mês de nascimento -> "))
    ano = int(input("Entre o seu ano de nascimento -> "))

    today = datetime.now()

    vidas = dias_vida(dia, mes, ano, today)

    if vidas.days < 0:
      print(f"Acho que algum dado seu está errado...\n")
    else:
      print(f"Você já está aqui nesse mundo a {vidas.days} dias")


  except ValueError:
    print("Apenas dados numérios permitidos")


if __name__ == "__main__":
  main()

