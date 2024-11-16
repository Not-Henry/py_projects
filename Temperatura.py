import time

temperatura = str(input('Insira o tipo de temperatura: ')).upper()[0]

try:
    valor = float(input('Insira o valor da temperatura: '))
except ValueError:
    # Caso o valor não seja um float ou int
    print('Valor inválido, tente novamente.')
    time.sleep(3)
    exit()

if temperatura == 'C':
    Celsius = valor * 1.8 + 32
    print(f'Em Fahrenheit, isso seria: {Celsius:.2f}º')
    time.sleep(3)
elif temperatura == 'F':
    Fahrenheit = (valor - 32) / 1.8
    print(f'Em Celsius, isso seria: {Fahrenheit:.2f}º')
    time.sleep(3)
else:
    print(f'Valores inválidos, o programa agora irá fechar.')
    time.sleep(3)
    exit()
