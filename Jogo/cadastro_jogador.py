from Jogo.criacao_jogo import *
from Jogo.constantes import *
from Jogo.jogo_acoes import *


def cadastro(jogo):
    num_portas_avioes = 1
    num_cruzadores = 1
    num_contra_torpedeiro = 2
    num_rebocadores = 2
    num_navios = 6

    while num_navios > 0:
        mostrar_jogo(jogo)
        print('\033[1;97mNAVIOS RESTANTES')
        print(f'\033[1;97m1 - Rebocadores ({num_rebocadores}/2)')
        print(f'\033[1;97m2 - Contra-Torpedeiros ({num_contra_torpedeiro}/2)')
        print(f'\033[1;97m3 - Cruzadores ({num_cruzadores}/1)')
        print(f'\033[1;97m4 - Porta-aviões ({num_portas_avioes}/1)\033[m')
        print()
        try:
            tipo = input('\033[1;93mSelecione o tipo do navio navio (1-4)-> \033[m')

            if tipo not in '1234':
                raise f'\033[1;31mDIGITE NÚMEROS ENTRE 1-4\033[m'
            linha = input('\033[1;97mSelecione a linha (1-10) -> \033[m')
            linha = transformar_linha(linha) - 1
            coluna = int(input('\033[1;97mSelecione uma coluna (1-10) -> \033[m'))-1
            direcao = input('\033[1;97mSelecione uma direção (Horizontal/Vertical) -> \033[m')

            if tipo == '1':
                if num_rebocadores == 0:
                    print('Sem navios restantes')
                    continue

                if adicionar_navio(REBOCADOR, linha, coluna, direcao, jogo):
                    print('Navio adicionado')
                    num_rebocadores -= 1
                    num_navios -= 1
                else:
                    print('Já existe navio na posição')

            elif tipo == '2':
                if num_contra_torpedeiro == 0:
                    print('Sem navios restantes')
                    continue

                if adicionar_navio(CONTRA_TORPEDEIRO, linha, coluna, direcao, jogo):
                    print('Navio adicionado')
                    num_contra_torpedeiro -= 1
                    num_navios -= 1
                else:
                    print('Já existe navio na posição')

            elif tipo == '3':
                if num_cruzadores == 0:
                    print('Sem navios restantes')
                    continue

                if adicionar_navio(CRUZADOR, linha, coluna, direcao, jogo):
                    print('Navio adicionado')
                    num_cruzadores -= 1
                    num_navios -= 1
                else:
                    print('Já existe navio na posição')

            else:
                if num_portas_avioes == 0:
                    print('Sem navios restantes')
                    continue

                if adicionar_navio(PORTA_AVIOES, linha, coluna, direcao, jogo):
                    print('Navio adicionado')
                    num_portas_avioes -= 1
                    num_navios -= 1
                else:
                    print('Já existe navio na posição')

        except Exception as error:
            print(error)
