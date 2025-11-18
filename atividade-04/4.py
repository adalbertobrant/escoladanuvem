# Números inteiros pares e impares

pares = 0
impares = 0

while True:
    entrada = input("Digite um número (ou 'fim'): ")    
    if entrada.lower() == 'fim':
        print("\nCalculando resultados...")
        break   
    try:
        numero = int(entrada)       
       
        if numero % 2 == 0:
            print(f"-> {numero} é PAR.")
            pares = pares + 1
        else:
            print(f"-> {numero} é ÍMPAR.")
            impares = impares + 1

    except ValueError:        
        print(f"(!) Entrada inválida. '{entrada}' não é um número inteiro. (Ignorando)")
       

print(f"Total  PARES : {pares}")
print(f"Total  ÍMPARES : {impares}")