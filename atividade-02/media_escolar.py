# Média Escolar

"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

"""
print("Calculadora de média escolar")

nome_aluno = input("Entre o nome do aluno -> ")

nota1 = float(input(f"Entre a 1° nota do aluno {nome_aluno} -> "))
nota2 = float(input(f"Entre a 2° nota do aluno {nome_aluno} -> "))
nota3 = float(input(f"Entre a 3° nota do aluno {nome_aluno} -> "))

media = (nota1 + nota2 + nota3) / 3.0

print(f"\nNotas Finais do aluno {nome_aluno}")
print(f"\nNota da 1° prova {nota1:.2f}")
print(f"Nota da 2° prova {nota2:.2f}")
print(f"Nota da 3° prova {nota3:.2f}")
print(f"\nMédia final obtida {media:.2f}")


