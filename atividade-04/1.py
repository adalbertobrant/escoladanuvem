# Calculadora de dois números com tratamento de erros 

while(True):
  try:

    n1 = input("Entre o primeiro número -> ")
    n1 = float(n1)
    break
  except ValueError:
    print(f"Insira apenas números - ENTRADA INVÁLIDA - ")

while(True):
  try:
    n2 = input("Entre o segundo número -> ")
    n2 = float(n2)
    break
  except ValueError:
    print(f"Insira apenas números - ENTRADA INVÁLIDA - ")

op = ""

while(True):
  print("\nOperações permitidas\n")
  print("Digite + para somar")
  print("Digite - para subtrair")
  print("Digite * para multiplicar")
  print("Digite / para dividir\n")
  print("Digite sair para terminar o programa")
  try:
    op = input(" ")
    if op in ['+','-','/','*']:
      print("\nRealizando operações")
      if op == '+':
        print(f"Soma de {n1} + {n2}")
        print(f"{n1 + n2}")
      if op == '-':
        print(f"Subtração de {n1} - {n2}")
        print(f"{n1 - n2}")
      if op == '*':
        print(f"Multiplicação de {n1} * {n2}")
        print(f"{n1 * n2}")
      
      if op == '/':
        try:
          print(f"Divisão de {n1} /  {n2}")
          print(f"{n1 / n2}")
        except ZeroDivisionError:
          print(f"O segundo número é  {n2} (ZERO)")
          while(True):
            try:
              n2_str = input("\nEntre o novo valor para n2 -> ")
              n2 = float(n2_str)
              if n2 == 0:
                print("\nO novo valor também é ZERO. Tente novamente.")
              else:
                print(f"\nNovo resultado: de {n1} / {n2} =  {n1 / n2}")
                break
            except ValueError:
              print(f"Ops, '{n2_str}' não é um número.")
              
    elif op == 'sair':
      print("Programa FINALIZADO\n")
      break
      
    else:
      raise ValueError("Opção inválida")
      
  except ValueError:
    print("Entre apenas os dígitos permitidos")
    print(f"Você tentou entrar um dígito não permitido -> {op}")

  


