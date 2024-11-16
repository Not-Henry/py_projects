import math

while True:
    print('Vamos calcular uma equação quadrática?')
    print('Para referência, aqui estão os valores:')
    print('ax^2 + bx + c = 0\n')
    
    a = float(input('Digite o coeficiente do termo x^2 (a): '))
    if a == 0:
        print('O valor "a" não pode ser igual a zero\n')
        continue
    b = float(input('Digite o coeficiente do termo x (b): '))
    c = float(input('Digite o termo constante (c): '))
    break

# Cálculo do discriminante
delta = b**2 - 4 * a * c

# Verificação se o discriminante é negativo
if delta < 0:
    print('\nNão resulta em raízes reais.')
    print(f'Δ: {delta}')
else:
    positivo = ((b * -1) + math.sqrt(delta)) / (2 * a)
    negativo = ((b * -1) - math.sqrt(delta)) / (2 * a)
    print(f'\nAs raízes são {positivo:.2f} e {negativo:.2f}')

# input('')