# Calculadora de notas com média

soma = 0
quantidade = 0
aluno = 1

while(True):
  notas = input(f"Digite a nota do {aluno}° ou fim -> ")
  if notas == 'fim':
    print("\nResultados:\n")
    break
  
  try:
    nota = float(notas)
    if 0 <= nota <= 10:
      soma = soma + nota
      quantidade = quantidade + 1
      print(f"Nota do {aluno}° registrada")
    else:
      print(f"Nota digitada fora do intervalo válido!!!")
  except ValueError:
    print("Entrada inválida dado ignorado")

  aluno += 1
  
if quantidade > 0:
  media_notas = soma / quantidade
  print(f"Total de notas registradas {quantidade}")
  print(f"Média da turma {media_notas:.2f}")

else:
  print("Nenhuma nota foi validada, sem dados para calcular")

