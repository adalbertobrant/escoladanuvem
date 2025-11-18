# Gorjeta para o Garçom do restaurante

def calc_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * porcentagem_gorjeta / 100.00

def main():
    print("--- Calculadora de Gorjetas ---")
    nome_garcom = input("Entre o nome do Garçom que vai ganhar a gorjeta -> ")
    
    try:
        valor_conta = float(input("Entre o valor total da conta R$ -> "))
        porcentagem_gorjeta = float(input("Entre o valor da porcentagem a ser dada (ex: 10) -> "))
        
        valor_da_gorjeta = calc_gorjeta(valor_conta, porcentagem_gorjeta)
        total_com_gorjeta = valor_conta + valor_da_gorjeta
        
        print("\n**********************************\n")
        print(f"Calculadora da Gorjeta para o Garçom -> {nome_garcom}")
        print(f"Valor da conta: R$ {valor_conta:.2f}")
        print(f"O valor a ser recebido de gorjeta é: R$ {valor_da_gorjeta:.2f}")
        print(f"Total a pagar (Conta + Gorjeta): R$ {total_com_gorjeta:.2f}")
        print("\n************************************\n")
        
    except ValueError:
        print("\n[Erro] Por favor, digite apenas números para o valor da conta e a porcentagem (use ponto para decimais).")

# A CORREÇÃO PRINCIPAL ESTÁ AQUI ABAIXO:
if __name__ == "__main__":
    main()
