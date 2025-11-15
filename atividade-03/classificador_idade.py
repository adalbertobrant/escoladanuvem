# Classificador de Idade

"""
1- Classificador de Idade
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

* Criança (0-12 anos),
* Adolescente (13-17 anos),
* Adulto (18-59 anos) ou
* Idoso (60 anos ou mais).

"""

nome = input(f"Entre o seu nome -> ")
idade = int(input(f"{nome.title()} digite sua idade -> "))
if idade >=0 and idade <= 12:
  print(f"{nome.title()} é uma Criança com {idade} anos.")

if idade >= 13 and idade <= 17:
  print(f"{nome.title()} é um(a) Adolescente com {idade} anos.")

if idade >= 18 and idade <= 59:
  print(f"{nome.title()} é uma pessoa  Adulta com {idade} anos.")

if idade >= 60:
  print(f"{nome.title()} é uma pessoa Idosa com {idade} anos.")
