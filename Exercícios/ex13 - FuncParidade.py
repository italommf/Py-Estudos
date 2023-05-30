numero = int(input('Teste a paridade aqui: '))

def paridade(num):
    paridade = 'Par' if num % 2 == 0 else 'Impar'
    return paridade
    
print(f'A paridade do numero {numero} é: {paridade(numero)}')