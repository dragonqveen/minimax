import random
import numpy

cargas = [5,10,15,3,10,5,2,16,9,7,5,10,15,3,10,5,2,16,9,7]

def main():

    populacao = numpy.zeros((11, 21))
    populacao_intermediaria = numpy.zeros((11, 21))

    for i in range(11):
        for j in range(20):
            populacao[i][j] = random.choice([0, 1])

    for i in range(5):
        print("Geração: " , i)
        for j in range(11):
            aptidao(populacao[j], cargas)

        print("População atual")
        for j in range(11):
            for k in range(20):
                print(int(populacao[j][k]), end=' ')
            print("- função: ", populacao[j][20])

        print()

        populacao_intermediaria[0] = elitismo(populacao)
        crossover(populacao, populacao_intermediaria)
        populacao = populacao_intermediaria

    #printa(populacao)


def aptidao(linha, cargas):
    acum1 = 0
    acum2 = 0

    for i in range(20):
        if(linha[i] == 0):
            acum1 += cargas[i]
        else:
            acum2 += cargas[i]
    
    linha[20] = abs(acum1 - acum2)


def elitismo(populacao):
    aux = numpy.zeros(21)
    linha = 0
    menor_valor = populacao[0][20]

    for i in range(1, 11):
        if(populacao[i][20] < menor_valor):
            menor_valor = populacao[i][20]
            linha = i

    for j in range(20):
        aux[j] = populacao[linha][j]

    return aux


def printa(coisa):
    for i in range(11):
        str_linha = ""

        for j in range(21):
            str_linha += str(int(coisa[i][j])) + " "

        print(str(i) + " - " + str_linha)

def crossover(populacao, populacao_intermediaria):
    i = 1
    while(i < 11):
        individuo1 = torneio(populacao)
        individuo2 = torneio(populacao)

        for j in range(10):
            populacao_intermediaria[i][j] = populacao[individuo1][j]
            populacao_intermediaria[i + 1][j] = populacao[individuo2][j]
        
        for j in range(10, 20):
            populacao_intermediaria[i][j] = populacao[individuo2][j]
            populacao_intermediaria[i+1][j] = populacao[individuo1][j]

        i += 2



def torneio(populacao):
    linha1 = random.choice(range(11))
    linha2 = random.choice(range(11))

    return linha2 if populacao[linha1][20] > populacao[linha2][20] else linha1

def mutacao(populacao):
    linha = random.choice(range(11))
    coluna = random.choice(range(20))

    if(populacao[linha][coluna] == 0):
        populacao[linha][coluna] = 1
    

main()
