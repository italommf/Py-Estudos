#============================================================
print("=======================")

'''
para criar uma função

def Somar():
    print('Resultado da soma')

por padrão, funções em python retornam "none"

'''

# passando argumentos não nomeados
'''
numeros = []
numeros.append(int(input('Digite numeros que deseja somar aqui: ')))
numeros = numeros.split()
numeros = tuple(numeros)
'''
#numeros = input('Digite os numeros que deseja somar, separados por espacos: ')
numeros = '1 2 3 4'
numeros = numeros.split()  # divide a string em uma lista de strings
numeros = [int(n) for n in numeros]  # converte cada string em um numero inteiro

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total
    
print(f'O resultado da soma é: {soma(*numeros)}')

#============================================================
print("=======================")

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(5))
print(triplicar(2))
print(quadruplicar(1))

'''
ao definir a variável, eu estou atribuindo a ela, o retorno de 
"duplicar = criar_multiplicador(2)" que é outra função, multiplicar(numero).
ou seja, estou atribuindo a função interna a variável. Dessa forma, eu "transformo minha
variável em função.

No "print(duplicar(5))" eu passo o parâmetro 5 para a função interna de criar_multiplicador(2)
ele executa a função interna com base no parâmetro externo, me retornando 10.

Eu basicamente crio funções internas e atribuo elas à variáveis, desta forma podendo
passar outros parâmetros para que as funções internas sejam executadas.

'''
#============================================================
print("=======================")

#dicionario, dict

pessoa = {
    'nome': 'Italo Mageste',
    'sobrenome': 'Martins França',
    'idade': 24,
    'endereco': [{'rua': 'lyra'},
                 {'numero': 656}]
}

print(f'A idade do {pessoa["nome"]} é {pessoa["idade"]} anos')
print(f'O endereço de {pessoa["nome"]} é rua {pessoa["endereco"][0]}')


for chave in pessoa: # imprime a chave
    print(chave)

print("")

for valor in pessoa.values(): # imprime o valor
    print(valor)

print("")

for valor in pessoa.items(): # imprime a chave e o valor
    print(valor)

print("")

'''
a chave pode ser criada fora do dicionario
'''

pessoa['peso'] = 72
print(pessoa['peso'])

del pessoa['sobrenome'] # apaguei a chave "sobrenome"
print(pessoa)

if pessoa.get('sobrenome') is None: # .get procura a chave passado como parâmetro e retorna se existe ou não.
    print('Não existe a chave sobrenome')
else:
    print('Existe a chave sobrenome')

'''
p1 = {
    'nome': 'italo',
    'idade': '24',
}

* .get pega um item de uma chave: print(p1.get('nome', 'valor padrão'))
* .pop apaga um item especificado:  teste = p1.pop('nome')
* .popitem() apaga a ultima chave do dicionario, não pode passar a chave como parâmetro (da erro)

* .update({
    'nome': 'novo valor' # atualiza um valor ja existente
    'peso': 70 # também pode ser usado para criar novas chaves
})

    * .update(nome = 'novo valor', peso = 70) # também pode ser atualizada desta forma
    # também pode receber listas

    lista = [('nome', 'novo valor'), ('peso', 70)]
    * .uptade(lista)

'''
#============================================================
print("=======================")

#conjuntos (o mesmo conjunto numerico da matematica)

s1 = set() # set vazio
s1 = {'Luiz', 1, 2, 3} # com dados

# os sets são eficientes para remover valores duplicados

s2 = set()
s2 = {1, 2, 3, 3, 3, 3, 3, 4, 5, 5} # elimina naturalemnte os valores repetidos
print(s2) # printa {1, 2, 3, 4, 5}

'''
posso converter listas e tuplas para um set, fazendo isso os valores
duplicados são eliminados, após isso eu posso converter novamente para
listas

set não garante a ordem dos elementos e não aceitam valores mutaveis
ex.: listas e dicionários

set não tem índice, por isso não garantem a ordem dos elementos
É POSSÍVEL ITERAR em sets usando "for" e outras coisas

métodos úteis em sets:

s1 = set()
*s1.add('italo') # adiciona o valor 'italo' da forma que coloquei
*s1.uptade('italo') # adiciona de forma iterada, letra por letra
                     'i', 't', 'a', 'l', 'o'
                    para mandar pelo update um iteravel sem separar
                    é só mandar no formato de iteraveis, exemplo, a tupla
                    s1.uptade(('italo', 1, 2, 3))     
*s1.clear() # limpa o set todo
*s1.discard('italo') # apaga o valor informado como parâmetro

'''
# operadores úteis

'''
s1 = set()
s2 = set()

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2 # une os dois sets e vira {1, 2, 3, 4}
s3 = s1 & s2 # intersecção dos dois sets {2, 3}
s3 = s1 - s2 # diferença dos dois sets {1}
s3 = s1 ^ s2 # diferença simetrica dos dois sets ao msm tempo {1, 4}
                        (o que não está nos dois sets)
'''

lista = [1, 32, 43, 12, 4, 3 ,2 ,5, 21]
lista.sort() # ordena a lista
print(lista)
lista.sort(reverse=True) # ordena a lista de trás para frente
print(lista)

#============================================================
print("=======================")

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

'''
def ordena(item):
    return item['nome']
    
lista.sort(key=ordena)
'''
lista.sort(key=lambda item: item['nome']) # ESTUDAR MAIS SOBRE FUNÇÕES LAMBDA

for item in lista:
    print(item)

#============================================================
print("=======================")

pessoa = {
    'nome': 'Italo',
    'sobrenome': 'Mageste',
}

dados_pessoa = {
    'idade': 24,
    'altura': 1.72,

}

a, b = pessoa # imprime as chaves de "pessoa"
print(a, b) # printa "nome sobrenome"

a, b = pessoa.values() # imprime os valores das chaves de "pessoa"
print(a, b) # printa "Italo Mageste"

a, b = pessoa.items() # imprime uma tupla com chave e valor
print(a, b) # printa "('nome': 'Italo') ('sobrenome': 'Mageste')"

pessoa_completa = {**pessoa, **dados_pessoa}    # com dois asteriscos eu extraio os valores do 
                                # dicionario passado para o novo dicionario
print(pessoa_completa) # dicionário com a junção dos outros dois passados como parâmetro

'''
*args para argumentos não nomeados
    função_qualquer('italo')

**kwargs para argumentos nomeados (para kwargs se usa 2 asteríscos)
     função_qualquer(nome = 'italo')
'''

def mostro_argumentos_nomeados(*args, **kwargs):
    print('Não Nomeados: ', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

print()
mostro_argumentos_nomeados(*pessoa_completa) # *args
print()
mostro_argumentos_nomeados(**pessoa_completa) # **kwargs

#============================================================
print("=======================")
print()

#print(list(range(10)))

lista = []
lista = [1 for numero in range(10)] # para cada numero no range 10, insira o valor 1
print(lista) # printa uma lista com 10 "1"

lista = []
lista = [numero for numero in range(10)] # para cada numero no range 10, insira o valor de numero
print(lista) # printa uma lista indo de 0 a 9

lista = []
lista = [numero * 2 for numero in range(10)] 
print(lista) # printa uma lista de 0 a 9 multiplicada por 2

print()

lista_pessoas = [

    {
        'nome': 'Jobisclei',
        'sobrenome': 'Aroldo',
        'idade': 202
    },

    {
        'nome': 'Abineldes',
        'sobrenome': 'Marconei',
        'idade': 212
    }
    
]

'''
É possível usar lógica em list comprehencion.

Para cada "dados" em "dados na lista_pessoas muda idade 
(o nome da variavel, se mudar aqui, muda na lista também)
para idade - 200.
'''

lista_pessoas_2 = [{**dados, 'idade': dados['idade'] - 200 } for dados in lista_pessoas]
print(*lista_pessoas_2, sep = '\n')

print()

#============================================================
print("=======================")
print()


lista = [n for n in range(10) if n < 5] # inclui o numero se for verdadeiro
                                        # se for falso o numero não é incluído
print (lista)

lista_pessoas_2 = []

#altera a idade e filtra. caso tenha alguma idade nova < 10 ela é adicionada na lista, caso não, não é adicionada na lista
lista_pessoas_2 = [{**dados, 'idade': dados['idade'] - 200} for dados in lista_pessoas if dados['idade'] - 200 < 10]
print(*lista_pessoas_2, sep = '\n') 

#============================================================
print("=======================")
print()

lista = [
    'a', 
    1, 1.1, 
    True, 
    [0, 1, 2], 
    (1, 2), 
    {1, 2}, 
    {'nome': 'Italo'}
]

for item in lista:
    if isinstance(item, set): # verifica se o tipo do item é "set"
        item.add(99999)
        print(item, isinstance(item, set))

#============================================================
print("=======================")
print()


generator = (n for n in range(100000))  # é uma função que sabe pausar, não salva
                                        # o numero na lista até eu mandar um .next
                                        # após isso ele salva somente o próximo.

def meu_gerador():
    yield 1 # yield diz para o gerador onde interromper a execução e retornar um valor
    yield 2 # quando a função for chamada novamente ela continuará a execução de onde parou
    yield 2
    yield 3

for valor in meu_gerador():
    print(valor)

print("=======================")
print()

a = 18
b = 0

try: # tenta executar o codigo, caso não de, pula direto para o except
    c = a / b
except ZeroDivisionError: # Exception é a classe que contém todos os erros do python. NÃO E BOA PRÁTICA
    print('NÃO HA DIVISAO POR 0')

'''
também posso tratar mais de um erro por linha
except (TypeError, ZeroDivisionError):
'''

try:
    c = a / b

except ZeroDivisionError as error:
    print('ZeroDivisionError')
    print(f'Mensagem de erro: {error}') # printa o erro
    print(f'Classe do erro: {error.__class__.__name__}')  # me da a calsse 

try: # tenta executar o trexo de código
    print('ABRIR ARQUIVO') 
    8/0

except ZeroDivisionError as e: # caso o try de erro de divisão por zero, 
    print(e.__class__.__name__)  # imprime o nome da classe do erro
    print(e)                     # imprime o erro em sí
    print('DIVIDIU ZERO')

except IndexError as error:     # caso dê erro de index, executa o print 
    print('IndexError')

except (NameError, ImportError): # mesma coisa para os erros passados
    print('NameError, ImportError')

else:   # caso o try passe sem nenhum erro, executa o else
    print('Não deu erro')

finally: # aqui sempre executa, independente de ter dado erro ou não nos trys
    print('FECHAR ARQUIVO')

'''
HIERARQUIA DAS EXCESSÕES: https://docs.python.org/pt-br/3/library/exceptions.html#exception-hierarchy

O try não pode ser executado sozinho

try except
try except finaly
try finaly
'''
print("=======================")
print()

#raise ValueError('Deu erro') # cria uma mensagem de erro personalizada

'''
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True

def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(8, '0'))    

'''

print("=======================")
print()

'''
de "sys" importe "exit"
    from sys import exit

para dar apelido para o comando ou módulo.
    import sys as s     # sys passa a se chamar "s"

para recarregar um módulo
    import importlib

    importlib.reload(nome do módulo)

'''

print("=======================")
print()

#variáveis livres e nonlocal

def fora(x):
    a = x   
    def dentro():
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(20)
dentro3 = fora(645)

print(dentro1())
print(dentro2())
print(dentro3())

'''
"a" é uma variável livre pois não está definida dentro do escopo da 
função "dentro".

''' 

print("=======================")
print()

# cout() está no namespace itertols

from itertools import count

c1 = count() # diferentemente do range(), o count é um contador infinito

for i in c1: 
    if i > 5:
        break
    print(i, end = ", ")

print("=======================")
print()

#combinações, perutações e produtos

from itertools import combinations, permutations, product


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2)) # a ordem NÃO importa
print_iter(permutations(pessoas, 2)) # a ordem IMPORTA
print_iter(product(*camisetas)) # faz todas as combinações possíveis

print("=======================")
print()

# groupby - agrupar por

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)


print("=======================")
print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]


def filtrar_preco(produto):
    return produto['preco'] > 100


# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]

novos_produtos = filter(
    lambda produto: produto['preco'] > 100, 
    produtos
)



lista = ['show' for i in range(5)]

for i in range(len(lista)):
    print(lista[i])
