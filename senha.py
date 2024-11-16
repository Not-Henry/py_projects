import random
import string

def gerar_senha(tamanho, minuscula, maisculas, numeros, especiais):
    # Cria listas de caracteres específicos
    caracteres = []
    
    # Adiciona a quantidade específica de cada tipo de caractere
    if minuscula > 0:
        caracteres.extend(random.choices(string.ascii_lowercase, k=minuscula))
    if maisculas > 0:
        caracteres.extend(random.choices(string.ascii_uppercase, k=maisculas))
    if numeros > 0:
        caracteres.extend(random.choices(string.digits, k=numeros))
    if especiais > 0:
        caracteres.extend(random.choices(string.punctuation, k=especiais))
    
    # Caso a senha ter menos caracteres do que o tamanho
    if len(caracteres) < tamanho:
        print('\n*A senha teve que ser completada por falta de caracteres*')
    # Caso a senha ter mais caracteres do que o tamanho
    elif len(caracteres) > tamanho:
        print('\n*A senha possui mais caracteres desejados do que o tamanho solicitado*')
        
    # Completa o tamanho da senha, se necessário
    while len(caracteres) < tamanho:
        caracteres.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        
    # Embaralha tudo, para ficar ainda mais aleatório
    random.shuffle(caracteres)
    
    # Retorna a senha
    senha = ''.join(caracteres[:tamanho])
    return senha

# Coleta os input dos usuários
tamanho = int(input('Qual o tamanho da senha? '))
minuscula = int(input('Quantas letras serão minúsculas? '))
maisculas = int(input('Quantas serão maisculas? '))
numeros = int(input('Quantos números? '))
especiais = int(input('E caracteres especiais? '))

# Gera e imprime a senha
print(f'\nSua senha é: {gerar_senha(tamanho, minuscula, maisculas, numeros, especiais)}')

input('')