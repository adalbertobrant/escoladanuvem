# Exercício 4

import json
import os

def escrever_json(nome_arquivo):
    """Solicita dados e salva em uma lista no formato JSON."""

    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'

    lista_pessoas = []

    while True:
        print("\n--- Novo Cadastro ---")
        nome = input('Entre o nome -> ')
        idade = input('Entre a idade -> ')
        cidade = input('Entre a cidade -> ')

        pessoa = {
            "nome": nome,
            "idade": idade,
            "cidade": cidade
        }

        lista_pessoas.append(pessoa)

        continuar = input('Deseja inserir mais dados? (s/n) -> ').lower()
        if continuar != 's':
            break

    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista_pessoas, arquivo, indent=4, ensure_ascii=False)

    print(f"\nDados salvos com sucesso em '{nome_arquivo}'.")

def ler_json(nome_arquivo):
    """Lê o arquivo JSON e exibe os dados formatados."""

    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'

    if not os.path.exists(nome_arquivo):
        print(f"Erro: O arquivo '{nome_arquivo}' não existe.")
        return

    print(f"\n--- Lendo arquivo {nome_arquivo} ---")

    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        dados_lidos = json.load(arquivo)

    for i, pessoa in enumerate(dados_lidos, 1):
        print(f"Pessoa {i}:")
        print(f"  Nome:   {pessoa['nome']}")
        print(f"  Idade:  {pessoa['idade']}")
        print(f"  Cidade: {pessoa['cidade']}")
        print("-" * 20)

if __name__ == '__main__':
    arquivo_nome = input("Defina o nome do arquivo JSON (ex: pessoas) -> ")

    escrever_json(arquivo_nome)

    ler_json(arquivo_nome)
