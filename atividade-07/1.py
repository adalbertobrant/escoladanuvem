# Exercício 1

import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao = df['tempo_execucao'].std()
        print(f"Média do tempo de execução: {media_tempo:.2f} segundos")
        print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f} segundos")
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")

if __name__== "__main__":
    
    nome_arquivo = input("Entre o nome do arquivo -> ")
    processar_logs_treinamento(nome_arquivo)


