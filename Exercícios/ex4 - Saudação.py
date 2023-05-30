hora = input('Digite a hora no formato de 24 horas: ')


try:

    hora = int(hora)

    if hora >= 0 and hora < 12:
        print('Bom dia')
    if hora >= 12 and hora < 18:
        print('Boa tarde')
    if hora >= 18 and hora < 24:
        print('Boa noite')
    else:
        print('Hora inválida')
except:
    print('Hora inválida')