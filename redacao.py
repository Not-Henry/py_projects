import pyautogui
import time

def type_text(text):
    # Espera um momento antes de começar a digitar
    time.sleep(5)  # Tempo para você abrir o aplicativo e focar no campo de texto
    words = text.split()
    for word in words:
        pyautogui.write(word)  # Escreve a palavra
        pyautogui.write(' ')     # Adiciona um espaço
        time.sleep(6)           # Espera aproximadamente 6 segundos (10 WPM)

if __name__ == "__main__":
    # Cole seu texto aqui
    text_to_type = input("Cole o texto que deseja digitar: ")
    type_text(text_to_type)
