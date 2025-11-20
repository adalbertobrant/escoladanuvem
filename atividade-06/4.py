# Cotação de Moedas

import requests

def consultar_cotacao():
    print("--- Consulta de Cotação (vs BRL) ---")
    print("Exemplos de códigos: USD (Dólar), EUR (Euro), GBP (Libra), BTC (Bitcoin)")
    
    moeda = input("Digite o código da moeda desejada: ").upper().strip()
    
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            dados = response.json()
            
            chave_moeda = f"{moeda}BRL"
            
            if chave_moeda in dados:
                info = dados[chave_moeda]
                
                nome = info['name']
                atual = float(info['bid'])
                maximo = float(info['high'])
                minimo = float(info['low'])
                data_hora = info['create_date']
                
                # Exibição
                print("\n" + "="*40)
                print(f"Moeda: {nome}")
                print(f"Cotação Atual: R$ {atual:.4f}")
                print(f"Mínimo do dia: R$ {minimo:.4f}")
                print(f"Máximo do dia: R$ {maximo:.4f}")
                print(f"Atualizado em: {data_hora}")
                print("="*40 + "\n")
            else:
                print("\nErro: Formato de resposta inesperado.")
        
        elif response.status_code == 404:
            print("\nErro: Moeda não encontrada. Verifique o código digitado (ex: USD, EUR).")
        else:
            print(f"\nErro na conexão: Código {response.status_code}")

    except Exception as e:
        print(f"\nOcorreu um erro crítico: {e}")

if __name__ == "__main__":
    consultar_cotacao()