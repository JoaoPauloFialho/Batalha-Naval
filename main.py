from Jogo.cadastro_jogador import *
from time import sleep
from Base_de_Dados.dados import Dashboard
from Jogo.jogo_acoes import *

while True:
    print(f'[1] Iniciar\n'
          '[2] Regras\n'
          '[3] Pontuação\n'
          '[4] Sair\n')
    try:
        escolha = int(input('-> '))
    except:
        print('\033[1;31m\033[1;107mESCOLHA 1-4\033[m')
        continue

    if escolha == 1:
        jogador1 = input('Digite seu nome jogador 1 -> ')
        jogador2 = input('Digite seu nome jogador 2 -> ')
        jogo = tabuleiro()
        cadastro(jogo)
        jogo2 = tabuleiro()
        cadastro(jogo2)
        print()
        print()
        print()
        jogo_jogador1_ver = tabuleiro()
        jogo_jogador2_ver = tabuleiro()

        while True:
            print('VEZ DO JOGADOR 1, ESCOLHA A POSIÇÃO DO DISPARO')
            mostrar_jogo(jogo_jogador1_ver)
            for c in range(3):
                if jogo_vitoria(jogo):
                    break
                linha = input()
                linha = transformar_linha(linha)
                coluna = int(input())
                print('Navio atingido') if atirar(linha, coluna, jogo2, jogo_jogador1_ver) else print('Errou o alvo')

            if jogo_vitoria(jogo):
                print('Jogador numero 1 venceu')
                vencedor = Dashboard(jogador1, vitoria=True)
                vencedor.adicionar()
                perdedor = Dashboard(jogador2, vitoria=False)
                perdedor.adicionar()
                break

            print('VEZ DO JOGADOR 2, ESCOLHA A POSIÇÃO DO DISPARO')
            mostrar_jogo(jogo_jogador2_ver)
            for c in range(3):
                if jogo_vitoria(jogo):
                    break
                linha = input()
                linha = transformar_linha(linha)
                coluna = int(input())
                print('Navio atingido') if atirar(linha, coluna, jogo, jogo_jogador2_ver) else print('Errou o alvo')

            if jogo_vitoria(jogo):
                print('Jogador numero 2 venceu')
                vencedor = Dashboard(jogador2, vitoria=True)
                vencedor.adicionar()
                perdedor = Dashboard(jogador1, vitoria=False)
                perdedor.adicionar()
                break

            if jogo_vitoria(jogo2):
                print('Jogador numero 1 venceu')
                break

    elif escolha == 4:
        print('Encerrando...')
        sleep(0.9)
        break

    elif escolha == 2:
        print('=' * 31)
        print('         BATALHA NAVAL')
        print('=' * 31)
        print('''O JOGO CONSISTE EM 2 JOGADORES TENTANDO AFUNDAR OS NAVIOS INIMIGOS QUE ESTÃO ESCONDIDOSNO COMEÇO CADA JOGADOR
        VAI SELECIONAR ONDE VAI FICAR OS SEUS NAVIOS DE GUERRA. 
        NÃO ÉPOSSÍVEL SOBREPOR NAVIOS
        As COLUNAS VÃO DE 1-10 E AS LINHAS A-J.
        ''')

    elif escolha == 3:
        pass

    else:
        print('\033[1;31m\033[1;107mESCOLHA 1-4\033[m')
