def mostrar_jogo(jogo):
    print('\033[1;47m\033[1;30m  1 2 3 4 5 6 7 8 9 10\033[m')

    for i, c in enumerate(jogo):
        print(f'\033[1;47m\033[1;30m{i} \033[m', end='')

        for x in c:
            print(f'\033[;1m\033[1;40m{x} \033[m', end='')
        print()


def atirar(linha, coluna, jogo, jogo_jogador_ve):
    if jogo[linha][coluna] == 'O':
        jogo[linha][coluna] = 'Z'
        jogo_jogador_ve[linha][coluna] = 'Z'
        return True
    else:
        jogo[linha][coluna] = 'Z'
        jogo_jogador_ve[linha][coluna] = 'Z'
        return False


def jogo_vitoria(jogo):
    for c in jogo:
        if 'O' in c:
            return False
    return True


def mostrar_jogo(jogo):
    letras = 'ABCDEFGHIJ'
    print('\033[1;47m\033[1;30m  1 2 3 4 5 6 7 8 9 10\033[m')

    for i, c in enumerate(jogo):
        print(f'\033[1;47m\033[1;30m{letras[i]} \033[m', end='')

        for x in c:
            print(f'\033[;1m\033[1;40m{x} \033[m', end='')
        print()


