import csv
import math
import os.path
import numpy as np


def formata_equacao(row):
    for i in range(len(row)):
        if math.fabs(int(row[i])) > 1 and i < len(row)-1:
            if int(row[i]) > 1 and i != 0:
                row[i] = row[i] + '+ x'
            else:
                row[i] = row[i] + 'x'
        elif int(row[i]) == 1 and i < len(row)-1:
            if i != 0:
                row[i] = '+x'
            else:
                row[i] = 'x'
        if i+1 == len(row):
            row[i] = '= '+row[i]
    return row


nome_arquivo = os.path.join('..', 'files', 'equacao.csv')


def resolve_equacao(nome_arquivo):
    listaValores = []
    with open(nome_arquivo, 'r') as file:
        reader = csv.reader(file, delimiter=',')

        for linha in reader:
            listaValores.append(linha)

        if len(listaValores) == 2:
            A = np.array([[int(listaValores[0][0]), int(listaValores[0][1])], [int(listaValores[1][0]), int(listaValores[1][1])]])
            B = np.array([int(listaValores[0][2]), int(listaValores[1][2])])
            X2 = np.linalg.solve(A, B)
            print('Resolução')
            print(X2)

        elif len(listaValores) == 3:
            A = np.array([[int(listaValores[0][0]), int(listaValores[0][1]), int(listaValores[0][2])], [int(listaValores[1][0]), int(listaValores[1][1]), int(listaValores[1][2])], [int(listaValores[2][0]), int(listaValores[2][1]), int(listaValores[2][2])]])
            B = np.array([int(listaValores[0][3]), int(listaValores[1][3]), int(listaValores[2][3])])
            X2 = np.linalg.solve(A, B)
            print('Resolução')
            print(X2)

        else:
            print('Entrada incorreta')


def main():
    print('Equação formatada:')

    with open(nome_arquivo, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            formata_equacao(row)
            if len(row) == 3:
                print(row[0], row[1], row[2])
            elif len(row) == 4:
                print(row[0], row[1], row[2], row[3])

    resolve_equacao(nome_arquivo)


if __name__ == "__main__":
    main()