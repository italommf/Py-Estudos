

lista = []

while True:
    print('============================')
    print('Selecione uma opção!')

    opcao = input('[I]nserir   [A]pagar   [L]istar   [S]air: ')
    oplowcase = opcao.lower()

    if oplowcase == 'a':

        apagar = input('Selecione o indice do qual deseja apagar: ')
        apagar = int(apagar)

        if apagar in range(len(lista)): 
            del lista[apagar]
            print('ítem apagado com sucesso!!!')

        else:
            print('Indice não encontrado')

    elif oplowcase == 'l':

        print('Aqui esta a lista com todos os itens adicionados!')
        for index, item in enumerate(lista):
            print(f'N°{index}, {item.capitalize()}')
       
    elif oplowcase == 'i':
        lista.append(input('Insira o item aqui: '))

    elif oplowcase == 's':
        break
       

