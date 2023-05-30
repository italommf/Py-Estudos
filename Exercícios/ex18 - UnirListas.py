# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

'''
def zipper(lista1, lista2):

    return [(lista1[i], lista2[i]) for i in range(min(len(cidades), len(estados)))]

print(zipper(cidades, estados))
'''

from itertools import zip_longest # usado para o zip_longest

print(list(zip(cidades, estados))) # "zip" usa a lista menor
print(list(zip_longest(cidades, estados))) # faz o mesmo só que usando a lista maior
print(list(zip_longest(cidades, estados, fillvalue = 'Não há cidade'))) # fillvalue é usado para preencher um valor vazio
