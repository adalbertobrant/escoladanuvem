# Senha forte

while(True):
    senha = input("\nEntre uma senha forte ou 'sair' para desligar: ")
    
    if senha.lower() == 'sair':
        print("Programa Encerrado")
        break
    
    try:
        if len(senha) < 8:
            raise ValueError("Senha muito curta. Deve ter pelo menos 8 caracteres.")
        
        tem_numero = False
        for caractere in senha:
            if caractere.isdigit():
                tem_numero = True
                break 
        
        if not tem_numero:
            raise ValueError("Senha inválida. Deve conter pelo menos um número.")

        print(f"SUCESSO! A senha '{senha}' é forte.")
        break 

    except ValueError as e:
        print(f"ERRO: {e}") 
    
    finally:
        print(f"(Analisando a tentativa: '{senha}'...)")
