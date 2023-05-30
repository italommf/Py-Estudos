cpf = input('Insira o CPF aqui: ')
cpf_iterado = ''
for numero in cpf:
    if numero == '.' or numero == '-':
        continue
    else:
        cpf_iterado += numero   

# calcula digito 1
i = 10
soma_mult = 0

for numero in cpf_iterado:
    numero = int(numero)
    numero *= i
    i-=1
    soma_mult += numero
    if i == 1:
        break

soma_mult *= 10 
rest_soma_mult = soma_mult
rest_soma_mult %= 11

digito_1 = 0 if rest_soma_mult > 9 else rest_soma_mult

# calcula digito 2
i = 11
soma_mult = 0

for numero in cpf_iterado:
    numero = int(numero)
    numero *= i
    i-=1
    soma_mult += numero
    if i == 1:
        break

soma_mult *= 10 
rest_soma_mult = soma_mult
rest_soma_mult %= 11

digito_2 = 0 if rest_soma_mult > 9 else rest_soma_mult

print(digito_1)
print(digito_2)