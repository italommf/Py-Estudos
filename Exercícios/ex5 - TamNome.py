nome = input('Digite seu nome aqui: ')
tam_nome = len(nome)

if tam_nome <= 4:
    print('Seu nome é PEQUENO')
if tam_nome > 4 and tam_nome < 7:
    print('Seu nome é NORMAL')
if tam_nome > 6:
    print('Seu nome é MUITO GRANDE')