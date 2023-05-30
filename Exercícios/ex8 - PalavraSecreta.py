palavra_secreta = 'abcd'
letras_acertadas = ''
tam_palavra = len(palavra_secreta)
venceu = False
tentativa = 0

while venceu == False:

    letra_dig = input('Digite uma letra: ')
    tentativa += 1

    if letra_dig in palavra_secreta:
        letras_acertadas += letra_dig

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
            
        else:
            palavra_formada += '*'
           
    print(f'Palavra: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        venceu = True

print('====================================')
print('Parabens, voce venceu!!!')
print(f'Numero de tentativas: {tentativa}')
print(f'A palavra secreta era: {palavra_secreta}')
print('====================================')