# Verificador de Ano Bissexto

"""
4- Verificador de Ano Bissexto
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.

"""

print("\n======= Ano Bissexto ======\n")

ano = int(input(f"Entre um ano para saber se é bissexto ou não -> "))

if ano % 400 == 0:
  print(f"O ano de {ano} é bissexto")

elif ano % 100 == 0:
  print(f"O ano de {ano} não é bissexto")

elif ano % 4 == 0:
  print(f"O ano de {ano} é bissexto")

else:
  print(f"O ano de {ano} não é bissexto")


