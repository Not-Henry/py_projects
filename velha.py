import time
import random

def imprimir_tabuleiro(tabuleiro):
    for i, linha in enumerate(tabuleiro):
        print(" | ".join(linha))
        if i < len(tabuleiro) - 1:
            print("-" * 9)

def computador(tabuleiro):
    while True:
        horizontal = random.randint(0, 2)
        vertical = random.randint(0, 2)
        if tabuleiro[horizontal][vertical] == " ":
            return (horizontal, vertical)

def jogador():
    while True:
        try:
            vertical = int(input('Digite o valor da vertical (1 a 3): ')) - 1
            horizontal = int(input('Digite o valor da horizontal (1 a 3): ')) - 1
            if 0 <= vertical <= 2 and 0 <= horizontal <= 2:
                return (vertical, horizontal)
            else:
                print("Posição inválida! Escolha valores entre 1 e 3.")
        except ValueError:
            print("Entrada inválida! Digite números entre 1 e 3.")

def verificar_vitoria(tabuleiro, simbolo):
    for linha in tabuleiro:
        if all(celula == simbolo for celula in linha):
            return True
    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == simbolo for linha in range(3)):
            return True
    if all(tabuleiro[i][i] == simbolo for i in range(3)) or \
       all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

def jogo_da_velha(modo):
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    imprimir_tabuleiro(tabuleiro)
    turno = random.randint(0, 1)

    for rodada in range(9):
        if modo == 1 and turno == 0:
            print("Vez do computador!")
            time.sleep(1)
            jogada = computador(tabuleiro)
        else:
            print("Sua vez!" if turno == 1 else "Jogador 2, sua vez!")
            jogada = jogador()

        if tabuleiro[jogada[0]][jogada[1]] == " ":
            simbolo = "X" if turno == 1 else "O"
            tabuleiro[jogada[0]][jogada[1]] = simbolo
            imprimir_tabuleiro(tabuleiro)

            if verificar_vitoria(tabuleiro, simbolo):
                print(f"Jogador {'1' if turno == 1 else 'Computador' if modo == 1 else '2'} venceu!")
                return

            turno = 1 - turno
        else:
            print("Essa posição já está ocupada! Tente novamente.")
    
    print("Empate! Fim de jogo.")

def main():
    print('***** Bem-vindo ao jogo da velha *****')
    while True:
        print('Escolha a opção: ')
        print('1. Humano VS Computador\n2. Humano VS Humano')
        modo = input("Escolha o modo (1 ou 2): ")
        if modo in {"1", "2"}:
            jogo_da_velha(int(modo))
        else:
            print("Opção inválida! Escolha 1 ou 2.")

        repetir = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if repetir != "s":
            print("Obrigado por jogar!")
            break

if __name__ == "__main__":
    main()