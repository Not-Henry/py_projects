import re

def le_assinatura():
    '''A função lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A função recebe um texto e devolve uma lista das sentenças dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A função recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A função recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''Essa função recebe duas assinaturas de texto e devolve o grau de similaridade nas assinaturas.'''
    somatorio = sum(abs(as_a[i] - as_b[i]) for i in range(6))
    return somatorio / 6

def calcula_assinatura(texto):
    '''Essa função recebe um texto e devolve a assinatura do texto.'''
    # Dividir o texto em sentenças
    sentencas = separa_sentencas(texto)
    
    # Características para cálculo dos traços linguísticos
    total_palavras = []
    total_frases = []
    soma_sentencas = sum(len(sentenca) for sentenca in sentencas)
    
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        total_frases.extend(frases)
        
        for frase in frases:
            palavras = separa_palavras(frase)
            total_palavras.extend(palavras)
    
    soma_palavras = sum(len(palavra) for palavra in total_palavras)
    n_palavras = len(total_palavras)
    n_palavras_dif = n_palavras_diferentes(total_palavras)
    n_palavras_uniq = n_palavras_unicas(total_palavras)
    
    # Traços linguísticos
    wal = soma_palavras / n_palavras
    ttr = n_palavras_dif / n_palavras
    hlr = n_palavras_uniq / n_palavras
    sal = soma_sentencas / len(sentencas)
    sac = len(total_frases) / len(sentencas)
    pal = sum(len(frase) for frase in total_frases) / len(total_frases)
    
    return [wal, ttr, hlr, sal, sac, pal]

def avalia_textos(textos, ass_cp):
    '''Essa função recebe uma lista de textos e uma assinatura ass_cp e devolve o número (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    menor_similaridade = float('inf')
    texto_infectado = 0
    
    for i, texto in enumerate(textos):
        assinatura_texto = calcula_assinatura(texto)
        similaridade = compara_assinatura(assinatura_texto, ass_cp)
        
        if similaridade < menor_similaridade:
            menor_similaridade = similaridade
            texto_infectado = i + 1  # Contagem dos textos começa em 1
    
    return texto_infectado

# Execução do programa
assinatura_infectada = le_assinatura()
textos = le_textos()
infectado = avalia_textos(textos, assinatura_infectada)
print(f"O autor do texto {infectado} está infectado com COH-PIAH")