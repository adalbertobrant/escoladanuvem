import csv

def escrever_dados(nome_arquivo):

    if not nome_arquivo.endswith('.csv'):
        nome_arquivo += '.csv'

    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escrever = csv.writer(arquivo_csv)
        escrever.writerow(['nome', 'idade', 'cidade'])
        
        while True:
            print("\n--- Novo Registro ---")
            nome = input('Entre o nome -> ')
            idade = input('Entre a idade -> ')
            cidade = input('Entre a cidade -> ')
 
            escrever.writerow([nome, idade, cidade])
            print(f"✓ {nome}, {idade}, {cidade} salvos com sucesso.")
            
            entrada = input('Deseja inserir mais dados? (s/n) -> ').lower()
            if entrada != 's':
                break

if __name__ == '__main__':
    nome_arquivo = input("Entre o nome do arquivo csv  -> ")
    escrever_dados(nome_arquivo)
    print(f"Arquivo {nome_arquivo} fechado.")