import sys
from random import randint
from random import uniform
from math import exp


# O tabuleiro será representado por uma lista de tamanho = "número de rainhas". Cada elemento da lista poderá ir de zero há "número de rainhas"
def criaTabuleiro(numeroDeRainhas):
        tabuleiro = []
        for i in range(0, numeroDeRainhas):
            tabuleiro.append(randint(1, numeroDeRainhas))
        print("O tabuleiro criado foi:")
        print(tabuleiro)
        return tabuleiro

# Busca todos os vizinhos do tabuleiro em qustão
def recuperaVizinhosDeTabulero(tabuleiro):
    vizinhosDeTabuleiro = [] 
    
    for identificadorDaRainha in range (0, len(tabuleiro)):
        for posicaoDaRainha in range (1, len(tabuleiro)+1):
            
            if posicaoDaRainha == tabuleiro[identificadorDaRainha] : 
                continue
    
            vizinho = tabuleiro.copy()
            vizinho[identificadorDaRainha] = posicaoDaRainha
            vizinhosDeTabuleiro.append(vizinho)

    print("Nesta iteração, o tabuleiro possui os seguintes vizinhos")
    print(vizinhosDeTabuleiro)

    return vizinhosDeTabuleiro

#Retorna um vizinho alearório dado um tabuleiro
def buscaVizinhoAleatorio(tabuleiro):
    vizinhos = recuperaVizinhosDeTabulero(tabuleiro)
    vizinhoAleatorio = vizinhos[randint(0,len(tabuleiro))]
    print("O vizinho aleatório retornado será:")
    print(vizinhoAleatorio)
    return vizinhoAleatorio



# Como a heurística é baseada em números de ataques. Esta função retorna quantos ataques são possíveis no tabuleiro
def buscarNumeroDeAtaquesNoTabuleiro(tabuleiro):
    numeroDeAtaques = buscarNumeroDeAtaquesNaHorizontal(tabuleiro) + buscarNumeroDeAtaquesNoNordeste(tabuleiro) + buscarNumeroDeAtaquesNoSudeste(tabuleiro) 
    print(numeroDeAtaques)
    return numeroDeAtaques


# Para cada rainha no tabuleiro, busca quantos ataques são possíveis na horizontal
def buscarNumeroDeAtaquesNaHorizontal(tabuleiro):
    return buscarNumeroDeAtaquesNaDireita(tabuleiro) 

# Para cada rainha no tabuleiro, busca quantos ataques são possíveis
def buscarNumeroDeAtaquesNaDireita(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range (0,len(tabuleiro)):
        for possivelAtaqueNaDireita in range (posicaoRainha,len(tabuleiro)):
            if possivelAtaqueNaDireita == posicaoRainha:
                continue 

            elif tabuleiro[posicaoRainha] == tabuleiro[possivelAtaqueNaDireita]:
                numeroDeAtaques += 1 
                break           
    return numeroDeAtaques

# Analisa o tabuleiro no sentido sudeste de cada rainha, contando o número de ataques possíveis
def buscarNumeroDeAtaquesNoNordeste(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range (0,len(tabuleiro)):
        mapeiaDiagonal = tabuleiro[posicaoRainha]
        for posicaoHorizontal in range (posicaoRainha + 1, len(tabuleiro)):
            mapeiaDiagonal -= 1

            if tabuleiro[posicaoHorizontal] == mapeiaDiagonal:
                numeroDeAtaques += 1
                break
    return numeroDeAtaques

# Analisa o tabuleiro no sentido sudeste de cada rainha, contando o número de ataques possíveis
def buscarNumeroDeAtaquesNoSudeste(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range (0,len(tabuleiro)):
        mapeiaDiagonal = tabuleiro[posicaoRainha]
        for posicaoHorizontal in range (posicaoRainha + 1, len(tabuleiro)):
            mapeiaDiagonal += 1

            if tabuleiro[posicaoHorizontal] == mapeiaDiagonal:
                numeroDeAtaques += 1
                break
    return numeroDeAtaques

#Entre um conjunto de tabuleiro, retorna o tabuleiro com a melhor heurística
def buscarMelhorVizinho( vizinhos ):
    melhorVizinho = []
    melhorHeuristica = sys.maxsize
    
    for vizinho in vizinhos :
        heuristicaVizinho = buscarNumeroDeAtaquesNoTabuleiro(vizinho)
        if heuristicaVizinho < melhorHeuristica:
            melhorHeuristica = heuristicaVizinho
            melhorVizinho = vizinho

    print("O melhor vizinho encontrado foi:")
    print(melhorVizinho)
    print("Com a heurística de valor: ")
    print(melhorHeuristica)
    return [melhorVizinho, melhorHeuristica]


#Simula o problema de N_Rainhas usando Hill-climbing
def simuladorProblemaN_RainhasComHillClimbing(numeroDeRainhas):
    tabuleiro = criaTabuleiro(numeroDeRainhas)
    
    tabuleiroAtual = tabuleiro
    solucao = []
    heuristicaAtual = sys.maxsize
    contadorDeHeuristicaRepetida = 0
    while(True):

        melhorVizinhoComHeuristica = buscarMelhorVizinho(recuperaVizinhosDeTabulero(tabuleiroAtual))
        if heuristicaAtual == melhorVizinhoComHeuristica[1]:
            contadorDeHeuristicaRepetida += 1 

        if heuristicaAtual > melhorVizinhoComHeuristica[1]:
            contadorDeHeuristicaRepetida = 0
            tabuleiroAtual = melhorVizinhoComHeuristica[0]
            heuristicaAtual = melhorVizinhoComHeuristica[1]

        if contadorDeHeuristicaRepetida > 10:
            print("foi encontrado um ombro, terminando a execução...")
            break
        
        if heuristicaAtual == 0 :
            print("SOLUÇÃO ENCONTRADA")
            print("A solução do problema será:")
            print(tabuleiroAtual)
            break

    return tabuleiroAtual

#Simula o problema de N_Rainhas usando SimulatedAnnealing
def simuladorProblemaN_RainhasSimulatedAnnealing(numeroDeRainhas, maximoDeIteracoes,temperaturaInicial, alpha):
    tabuleiro = criaTabuleiro(numeroDeRainhas)
     
    temperaturaFinal = 0.1
    tabuleiroAtual = tabuleiro
    solucao = tabuleiroAtual

    temperaturaAtual = temperaturaInicial
    
    for i in range(1,maximoDeIteracoes):
        if(temperaturaAtual<temperaturaFinal):
            break

        vizinhoAleatorio = buscaVizinhoAleatorio(solucao)
        
        diferrencaDeCusto = buscarNumeroDeAtaquesNoTabuleiro(tabuleiroAtual) - buscarNumeroDeAtaquesNoTabuleiro(vizinhoAleatorio)

        if(diferrencaDeCusto < 0):
            tabuleiroAtual = vizinhoAleatorio
            if(buscarNumeroDeAtaquesNoTabuleiro(vizinhoAleatorio) <= buscarNumeroDeAtaquesNoTabuleiro(solucao)):
                solucao = vizinhoAleatorio
        else:
            if(uniform(0,1) < exp(-(diferrencaDeCusto / temperaturaAtual))):
                tabuleiroAtual = vizinhoAleatorio
                temperaturaAtual = temperaturaAtual * alpha
    
    print("A solução encontrad foi:")
    print(solucao)
    print("Com a heurística: ")
    print(buscarNumeroDeAtaquesNoTabuleiro(solucao))
    return solucao
                
simuladorProblemaN_RainhasSimulatedAnnealing(4,5000,900,0.01)

#simuladorProblemaN_Rainhas(8)

#buscarNumeroDeAtaquesNoTabuleiro([1,1,3,3,4,3,1,1])

#buscaVizinhoAleatorio([1,1,3,3,4,3,1,1])

