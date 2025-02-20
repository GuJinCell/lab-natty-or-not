import random

# Tabuleiro inicial
tabuleiro = [" " for _ in range(9)]

# Mostra o tabuleiro
def exibir_tabuleiro():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("---------")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("---------")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

# Verifica vitória
def verificar_vitoria(jogador):
    # Linhas, colunas e diagonais
    vitorias = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
    for a, b, c in vitorias:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == jogador:
            return True
    return False

# Verifica empate
def verificar_empate():
    return " " not in tabuleiro

# Jogada do jogador
def jogada_jogador():
    while True:
        try:
            pos = int(input("Escolha uma posição (1-9): ")) - 1
            if 0 <= pos <= 8 and tabuleiro[pos] == " ":
                tabuleiro[pos] = "X"
                break
            print("Posição inválida, tente novamente!")
        except ValueError:
            print("Entrada inválida")

# Jogada da IA
def jogada_ia():
    livres = [i for i in range(9) if tabuleiro[i] == " "]
    if livres:
        pos = random.choice(livres)
        tabuleiro[pos] = "O"
        print(f"IA jogou na posição {pos + 1}")

# Jogo principal
print("Você é 'X', a IA é 'O'")
print("1 | 2 | 3\n---------\n4 | 5 | 6\n---------\n7 | 8 | 9")
while True:
    exibir_tabuleiro()
    jogada_jogador()
    if verificar_vitoria("X"):
        exibir_tabuleiro()
        print("Você venceu!")
        break
    if verificar_empate():
        exibir_tabuleiro()
        print("Empate!")
        break
    jogada_ia()
    if verificar_vitoria("O"):
        exibir_tabuleiro()
        print("IA venceu!")
        break
    if verificar_empate():
        exibir_tabuleiro()
        print("Empate!")
        break