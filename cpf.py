cpf = str(input('Digite o CPF completo (11 dígitos): '))
valor = 10
soma = 0
igual = False

# Verificar se o CPF possui números iguais
for i in range(10):
    if cpf[i] != cpf[0]:
        break
    else:
        igual = True
        
# Calcular os valores para o digito um
for i in range(9):
    soma += int(cpf[i]) * valor
    valor -= 1

# Calcular o digito um
resto = soma % 11
    
if resto < 2 or resto == 10:
    digito1 = 0
else:
    digito1 = 11 - resto

# Resetamos o soma, o valor e o coiso
soma = 0
valor = 11

# Calcular o os valores para o digito dois
for i in range(10):
    soma += int(cpf[i]) * valor + soma
    valor -= 1

# Calcular o digito dois
resto = soma % 11

if resto < 2 or resto == 10:
    digito2 = 0
else:
    digito2 = 11 - resto

# Verifiacação do CPF
print('A verificação do seu CPF foi completa!')
if igual == True:
    print(f'O seu CPF ({cpf}) é inválido, pois possui letras iguais!')
elif int(cpf[-1]) == digito2 and int(cpf[-2]) == digito1:
    print(f'O seu CPF ({cpf}) é válido!')
else:
    print(f'O seu CPF ({cpf}) é inválido!')


input('')