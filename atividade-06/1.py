# Gerador aleatório usando random 

import random
import string

def gerar_senha(quantidade_caracteres):
  if quantidade_caracteres <= 0:
    while(True):
      try:
        quantidade_caracteres = int(input(f"{quantidade_caracteres} não é permitida\nEntre uma quantidade maior que zero -> "))
      except ValueError:
        print(f"Dado ainda está errado insira um dado correto")
      break
  
  letras = string.ascii_letters
  numeros = string.digits
  caracteres ="!@#$%*()_-'`^~<>,.:;?/|°"

  palavra = letras + caracteres + numeros

  resultado = ''.join(random.choice(palavra) for _ in range(quantidade_caracteres))

  return resultado

def main():
  print(" GERADOR DE SENHAS FORTES ")
  x = 0
  while(x == 0):
    try:
      tam = int(input(f"Entre a quantidade de caracteres para gerar a senha forte -> "))
      senha_forte = gerar_senha(tam)
      print(f"A senha forte gerada é {senha_forte}")
      x = int(input('Digite 0 para gerar nova senha ou qualquer número para sair -> '))
    except ValueError:
      print("Erro de entrada ")

if __name__ == '__main__':
  main()