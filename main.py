import random
import numpy

cargas = [5, 10, 15, 3, 10, 5, 2, 16, 9, 7]
tam_dados = 10
tam_tarefas = len(cargas)

def main():

    populacao = numpy.zeros((tam_tarefas, tam_dados + 1))
    populacaoIntermediaria = numpy.zeros((tam_tarefas, tam_dados))

    for i in range(tam_tarefas):
        for j in range(tam_dados - 1):
            populacao[i][j] = random.choice([0, 1])

    for i in range(tam_tarefas):
        aptidao(populacao[i], cargas)

    printa(populacao)


def aptidao(linha, cargas):
    acum1 = 0
    acum2 = 0

    for i in range(tam_dados):
        if(linha[i] == 0):
            acum1 += cargas[i]
        else:
            acum2 += cargas[i]
    
    linha[tam_dados] = abs(acum1 - acum2)


def elitismo(populacao):
    aux = []
    linha = 0
    menor_valor = populacao[0][tam_dados]

    for i in range(tam_tarefas):
        if(populacao[i][tam_dados] < menor_valor):
            menor_valor = populacao[i][tam_dados]
            linha = i

    for j in range(tam_dados):
        aux[j] = populacao[linha][j]

    return aux


def printa(coisa):
    for i in range(tam_tarefas):
        str_linha = ""

        for j in range(tam_dados):
            str_linha += str(int(coisa[i][j])) + " "

        print(str(i) + " - " + str_linha)

def crossover(populacao, populacaoIntermediaria):
    for i=

def torneio(populacao):
    linha1 = random.choice(range(tam_tarefas))
    linha2 = random.choice(range(tam_tarefas))

    return linha2 if populacao[linha1][tam_dados] > populacao[linha2][tam_dados] else linha1

main()
