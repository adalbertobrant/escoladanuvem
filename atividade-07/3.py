# Exercício 3

import csv


def ler_csv(nome_arquivo):
    with open(nome_arquivo, 'r', newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)


if __name__ == '__main__':

    entrada = input("Entre o nome do arquivo csv -> ")
    ler_csv(entrada)
    print("Arquivo fechado")


