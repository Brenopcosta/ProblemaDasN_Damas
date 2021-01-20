import sys
from random import randint

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

# Como a heurística é baseada em números de ataques. Esta função retorna quantos ataques são possíveis no tabuleiro
def buscarNumeroDeAtaquesNoTabuleiro(tabuleiro):
    numeroDeAtaques = buscarNumeroDeAtaquesNaHorizontal(tabuleiro) + buscarNumeroDeAtaquesNoNordeste(tabuleiro) + buscarNumeroDeAtaquesNoSudeste(tabuleiro) 
    print(numeroDeAtaques)
    return numeroDeAtaques


# Para cada rainha no tabuleiro, busca quantos ataques são possíveis na horizontal
def buscarNumeroDeAtaquesNaHorizontal(tabuleiro):
    return buscarNumeroDeAtaquesNaDireita(tabuleiro) 
    
'''+ buscarNumeroDeAtaquesNaEsquerda(tabuleiro)'''

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
'''
def buscarNumeroDeAtaquesNaEsquerda(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range (0,len(tabuleiro)):
        for possivelAtaqueNaEsquerda in range (len(tabuleiro) - 1, posicaoRainha, -1):
            if possivelAtaqueNaEsquerda == posicaoRainha:
                continue 

            elif tabuleiro[posicaoRainha] == tabuleiro[possivelAtaqueNaEsquerda]:
                numeroDeAtaques += 1 
                break
    return numeroDeAtaques
'''
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
'''
def buscarNumeroDeAtaquesNoNoroeste(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range ( 0, len(tabuleiro)):
        mapeiaDiagonal = tabuleiro[posicaoRainha]
        for posicaoHorizontal in range (posicaoRainha - 1, -1, -1):
            mapeiaDiagonal -= 1

            if tabuleiro[posicaoHorizontal] == mapeiaDiagonal:
                numeroDeAtaques += 1
                break
    return numeroDeAtaques

def buscarNumeroDeAtaquesNoSudoeste(tabuleiro):
    numeroDeAtaques = 0

    for posicaoRainha in range ( 0, len(tabuleiro)):
        mapeiaDiagonal = tabuleiro[posicaoRainha]
        for posicaoHorizontal in range (posicaoRainha - 1, -1, -1):
            mapeiaDiagonal += 1

            if tabuleiro[posicaoHorizontal] == mapeiaDiagonal:
                numeroDeAtaques += 1
                break
    return numeroDeAtaques
'''

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



def simuladorProblemaN_Rainhas(numeroDeRainhas):
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

#simuladorProblemaN_Rainhas(8)

buscarNumeroDeAtaquesNoTabuleiro([1,1,3,3,4,3,1,1])

