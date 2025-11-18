# Verifica se o texto ou palavra é palíndromo

import unicodedata

def eh_palindromo(texto):
    txt = unicodedata.normalize('NFKD', texto)

    limpa = ''.join(
        ch.lower() for ch in txt
        if ch.isalnum()
    )
    
    invertido = limpa[::-1]
    return limpa == invertido

def main():
    print("\n--- Verificador de Palíndromos  ---")
    print("Reconhece frases, acentos e pontuação.")
    txt = input("Digite o texto: ")

    if eh_palindromo(txt):
        print(f"\nSim! \"{txt}\" é um palíndromo.")
    else:
        print(f"\nNão. \"{txt}\" não é um palíndromo.")

if __name__ == "__main__":
    main()
