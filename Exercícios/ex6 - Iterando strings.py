nome = input('Escreva seu nome: ')
tam_nome = len(nome)
novo_nome = ''

cont = 0

while cont < tam_nome:

    letra = nome[cont]
    novo_nome += f'*{letra}' #novo_nome = novo_nome + * + letra
    cont+=1
   
print(novo_nome)