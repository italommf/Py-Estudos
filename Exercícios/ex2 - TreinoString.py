print(50*'-')
print('Digite seu nome: ')
nome = input()
print('Digite sua idade: ')
idade = input()

if nome and idade:

    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome contem espaço')
    else:
        print(f'Seu nome NÃO contem espaço')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

else:
    print('Desculpe, você deixou campos vazios.')
