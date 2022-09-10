from Jogo.constantes import *


def transformar_linha(linha):
    if str(linha).isnumeric():
        return int(linha)
    if linha == 'A':
        return 0

    elif linha == 'B':
        return 1

    elif linha == 'C':
        return 2

    elif linha == 'D':
        return 3

    elif linha == 'E':
        return 4

    elif linha == 'F':
        return 5

    elif linha == 'G':
        return 6

    elif linha == 'H':
        return 7

    elif linha == 'I':
        return 8

    elif linha == 'J':
        return 9


def checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
    if tipo == REBOCADOR:
        if jogo[linha][coluna] == 'O':
            return True
        else:
            return False

    elif tipo == CONTRA_TORPEDEIRO:
        if direcao == HORIZONTAL:
            for c in range(2):
                if jogo[linha][coluna+c] == 'O':
                    return True
            return False

        else:
            for c in range(2):
                if jogo[linha+c][coluna] == 'O':
                    return True
            return False

    elif tipo == CRUZADOR:
        if direcao == HORIZONTAL:
            for c in range(3):
                if jogo[linha][coluna+c] == 'O':
                    return True
            return False

        else:
            for c in range(3):
                if jogo[linha+c][coluna] == 'O':
                    return True
            return False

    elif tipo == PORTA_AVIOES:
        if direcao == HORIZONTAL:
            for c in range(4):
                if jogo[linha][coluna + c] == 'O':
                    return True
            return False

        else:
            for c in range(4):
                if jogo[linha + c][coluna] == 'O':
                    return True
            return False


def tabuleiro():
    matriz = [[], [], [], [], [], [], [], [], [], []]

    for x in range (0, 10):
        for c in range (0, 10): #  cria uma matriz vazia bonita
            matriz[x].insert(c,'X')

    return matriz


def adicionar_navio(tipo, linha, coluna, direcao, jogo):
    if tipo == REBOCADOR:
        if checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
            return False

        else:
            jogo[linha][coluna] = 'O'
            return True

    elif tipo == CONTRA_TORPEDEIRO:
        if direcao == HORIZONTAL:
            if checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
                return False

            else:
                for c in range(2):
                    jogo[linha][coluna+c] = 'O'
                return True

        if direcao == VERTICAL:
            if checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
                return False

            else:
                for c in range(2):
                    jogo[linha+c][coluna] = 'O'
                return True

    elif tipo == CRUZADOR:
        if direcao == HORIZONTAL:
            if checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
                return False

            else:
                for c in range(3):
                    jogo[linha][coluna+c] = 'O'
                return True

        else:
            if checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
                return False

            else:
                for c in range(3):
                    jogo[linha+c][coluna] = 'O'
                return True

    elif tipo == PORTA_AVIOES:
        if direcao == HORIZONTAL:
            if checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
                return False

            else:
                for c in range(4):
                    jogo[linha+c][coluna] = 'O'
                return True

        else:
            if checa_espaco_vazio(tipo, linha, coluna, direcao, jogo):
                return False

            else:
                for c in range(4):
                    jogo[linha+c][coluna] = 'O'
                return True
