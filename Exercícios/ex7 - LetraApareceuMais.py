'''
frase de teste

frase = 'O python é uma linguagem de programação multiparadigma. Python foi criado por Guido Van Rossum.'

'''
frase = input('Digite qualquer coisa aqui: ')

tam_frase = len(frase)

i = 0
letra_que_apareceu_mais = '' # armazena a letra que mais apareceu
cont_apareceu_mais = 0 # armazena a quantidade da letra que mais apareceu

while i < tam_frase:
    letra = frase[i]
    num_letra = frase.count(letra)

    if letra == ' ':
        i += 1
        continue

    if cont_apareceu_mais < num_letra:
        letra_que_apareceu_mais = letra
        cont_apareceu_mais = num_letra

    i += 1
    
print(f'A letra "{letra_que_apareceu_mais}" apareceu {cont_apareceu_mais} vezes')