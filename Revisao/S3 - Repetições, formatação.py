print("teste atenção")
print(12, 34)
print(12, 34, sep="-") #adiiona - como separador 
print("teste de \"aspas\" qualquer coisa") # \ é um caracter de escape, ao colocar, o interpretador não le ele como comando
print('"aspas" simples tambem reconhece aspas')

print(type(2.41)) #a funçã type me retorna o tipo de 2.41 sendo como float
print(type(True)) #bool
print(type(10==10)) #bool
print(type(int('1'))) #converte a string 1 para inteiro e me retorna o tipo int

print(2**3) #2^3, me retorna 8

print('1' + '2' + '3') #contatena as letras a, b e c
print(1 + 2 + 3) #soma

print(4 * 'italo') #repete italo 4 vezes

nome = "italo"
altura = 1.72354
peso = 72
idade = 24
print(f'{nome} tem {altura:.2f} de altura e {peso}kg de peso.')
#f-strings é um tipo de formatação
#para informar o numero de casas decimais "vaiavel:.numerof"

print('o {} tem {:.2f} de altura e {}kg de peso'.format(nome, altura, peso))
# .format(a,b,c,d) é outra forma de formatação

print('{1:.2f} {0} {2}'.format(nome, altura, peso))
#também posso passar o índice do parametro que quero exibir com sua respectiva formatação

'''
input("digite um numero: ")

o que eu digitar vai ser armazenado como string e não como inteiro
para colocar como inteiro a entrada ficaria assim:

int(input("digite um numero: "))

fazer dessa forma é possivel, mas não checa o que o usuario digitou
antes da conversão. o melhor seria:

numero = input("digite um numero: ")
int_num = int(numero)

'''
if nome == "jobisclei":
    print("o nome esta errado")
elif nome == "italo":
    print("o nome esta CORRETISSIMO")
else:
    print("c digitou os nome tudo errado")

if nome == "italo" and idade == 24: # o if executa se AS DUAS forem verdadeiras
    print('printa qualquer coisa aqui')

if nome == "italo" or idade == 24: # o if executa se UMA DAS DUAS forem verdadeiras
    print('printa qualquer coisa aqui')

'''

if(True and True and True) executa todos as três condições e retorna o valor da função
if(True and False and True) para a ececução e retorna no False

if(0 or False or 0 or 'abc' or True) ele para a execução no primeiro "verdadeiro" que encontrar 
                                     e retorna o abc (que é considerado verdadeiro)
                                     
'''
print(nome[2]) # me retorna "a" ja que é a letra de íncice 2 no nome Italo
print('ita' in nome) # retorna True, ja que ita esta em italo
print('aaa' not in nome) # retorna True, ja que aaa não está em italo

print(50 * '-')

variavel = '%s, sua altura é %.2f' % (nome, altura) # %s para string, %f para float
print(variavel)

print('O hexadecimal de %d é: %x' % (idade, idade)) # %x minusculo gera um hexadecimal minusculo
                                                    # %X maiusculo gera um hexadecimal maiusculo 

variavel = 'italo'
print(variavel)
print(f'{variavel: >50}') #preenche na esquerda com espaços que somados a string dão 50 caracteres

'''
formatação f-string
preenche com os caracteres:
> esquerda
< direita
^ centro

'''

'''
fatiamento de strings

string[inicio:fim:passo]

'''

variavel = 'ola mundo'
print(variavel[4:]) # ao omitir, ele me retorna da 4 em diante
print(variavel[:3]) # aqui me retorna até o "a", lembrando que não me mostra o ultimo. Então o correto é pedir até o caractere desejado +1 
print(len(variavel)) # a função me retorna a quantidade (começando a contagem do 1), NÃO ME RETORNA ÍNDICES, por isso não começa do 0
print(variavel[::2]) # aqui exibe as letras de duas em duas, exibe uma e pula a proxima.
print(variavel[::-1]) # começa a exibir contando de trás para frente, inverte a string

# comentado para parar de dar imput toda hora para dobrar o numero
''' 
# tratamento de erro
try:
    numero = input('Vou dobrar o numero que voce digitar aqui: ')
    print(f'String digitada: {numero}')
    numero = int(numero)
    dobro_num = numero*2
    print(f'O dobro do numero {numero} é {dobro_num}')
except:
    print('Ocorreu algum erro') # se eu digitar um caractere que não seja um numero o programa passa para a excessão e me retorna o print
'''

# variaveis constantes a gente escreve com letra maiuscula (por convenção)
velocidade_atual = 60
local_carro = 90
VELOCIDADE_RADAR_1 = 60
LOCAL_RADAR_1 = 100
ALCANCE_RADAR = 1

print(id(nome)) # id aponta para onde nome esta armazenado na memoria

nome.isdigit() # acusa se a STRING digitada é um numero INTEIRO, não funciona com valores, somente com STRINGS

'''
tipo imutaveis: str, int, float, bool

'''

while nome == 'italo':
    print('laço feito com sucesso')
    break # para o laço

contador = 0
while contador <= 20:
    
    contador += 1
    
    if contador >= 5 and contador <= 10:
        continue    # volta para o laço, sem executar daqui para baixo.
                    # nesse caso, quando o contador estiver entre 5 e 10
                    # o continue é chamado e volta para o laço, somando mais um até ficar maior que 10.
    print(f'O contador está atualmente em {contador}')

'''
for letra in texto:

a sintaxe do for aqui funciona de forma diferente

'''

# range(inicio, fim, de tanto em tanto)
numeros = range(1, 20, 2) # cria um intervalo inciando em 1, terminando em 20 e contando de 2 em 2.
for numero_teste in numeros:  
    print(numero_teste)
# para numeros negativos é necessário informar o passo a passo como num negativo
# exemplo: range(0, -10, -1) de 0 à -10 contando de -1 em -1.
# continue, break e else também funcionam no "for"

'''
listas em python são o equivalente aos arrays
são do tipo list
* 'del' apaga um índice específico e move todos os outros
* '.pop()' remove o ultimo elemento da lista e retorna uma string
* '.append()' insere um elemento no final da lista
* '.clear()' limpa a lista
* '.insert(indice, valor)' insere um valor no indice especificado e move todos os outros
* '+' concatena listas: lista_a[] + lista_b[]
* .extend() concatena lista, não precisa atribuir a uma variável
    - Exemplo: lista_a.extend(lista_b)
'''

lista = [123, 'texto qualquer', 'Italo', 1.2, 4, False]
print(lista)
del lista[2] # apaga o índice especificado e move todos os outros.
print(lista)
lista.append(89) # inseriu o 89 ao fim da lista
print(lista)
ultimo_elemento = lista.pop() # removeu o último elemento da lista, não preciso atribuir a uma variável.
print(lista)
print(ultimo_elemento)

var1, var2, var3, var4, var5 = lista # desempacotamento, atribuindo os valores da lista às variáveis
print(var3) # vai printar "Italo"

var1, *resto = lista
print(var1, resto)

# listas sem os colchetes são chamadas de tuplas e são imutáveis
nomes = '123', 'texto qualquer', 'Italo', 1.2, 4, False


lista = tuple(lista) # é possível converter listas para tuple
lista = list(lista) # o inverso também é possível, de tuple para lista
print(f'a lista desempacotada com *lista aqui: ', end=' ')
print(*lista) # desempacota a lista
print(*lista, sep = '\n') # desempacota a lista quebrando a linha entre cada um


#lista enumerada
lista_enumerada = enumerate(lista)
for item in lista_enumerada: 
    print(item)

''' 
para imprimir todos os itens da lista, é usado o for
caso queira imprimir um a um, o processo é diferente, é
preciso criar um iterador toda vez que for imprimir na tela.
É como se o iterador fosse "consumido" ao imprimir
Não é possível dar um print só enumerando a lista

lista_enumerada = enumerate(lista)

É preciso transformar o tipo para lista ou tupla novamente.

lista_enumerada = list(enumerate(lista))

'''
for item in enumerate(lista): # aqui esta sendo criado a cada ciclo do for
    print(item) # estou imprimindo a tupla

for indice, item_lista in enumerate(lista): # aqui esta sendo criado a cada ciclo do for
    print(indice, item_lista) # estou imprimindo os ítens da tupla

'''
# função do sistema, LIMPAR O TERMINAL
import os
os.system('cls')

'''

frase = 'Olha só, que coisa interessane'
lista_palavras = frase.split(',') # me retorna uma lista com todas as palavras usando o separador de escolha passado como parâmetro
'''
* .strip() corta os espaços do inicio e do fim da string
* .rstrip() corta os espaços da direita
* .lstrip() corta os espaços da esquerda
* .join() une novamente as strings
'''

# depurar depois
'''i = 0
lista_frases = []
for i, frase in enumerate(lista_palavras):
    lista_frases.append(lista_frases[i].strip())
print(lista_frases)

frases_unidas = '-'.join(lista_frases)
print(frases_unidas)'''

salas = [['Maria', 'Helena',], 
         ['Elaine'], 
         ['Luiz', 'João', 'Eduarda', (0, 10, 20, 30, 40)]]
print(salas[1][0]) # lista 1, indice 0 - Elaine
print(salas[0][1]) # lista 0, indice 1 - Helena
print(salas[2][3]) # lista 2, indice 2 - Eduarda
print(salas[2][3][3]) # lista 2, indice 3, indice 3 da tupla - 30

for sala in salas:
    print(f'A sala: {sala}')
    for aluno in sala:
        print(f'tem os alunos: {aluno}')

print(*salas) # desempacota a lista de listas
print(*salas, sep = '\n') # desempacota a lista quebrando a linha entre cada lista interna

# operação ternária
condicao = 10 == 100 # True
variavel = 'x' if False else 'y'
print(variavel) # deve imprimir y

digito = 10
novo_digito = 0 if digito > 9 else digito  
print(novo_digito)

import random # importa a biblioteca de random
print(random.randint(0,9)) # gera um inteiro entre 0 e 9

nove_digitos = ''
for i in range (9):
    nove_digitos += str(random.randint(0, 9))  # gera 9 inteiros, converte os 9 para str e adiciona na variável
                                            # é preciso a conversão pois a variável aceita iteraveis, e inteiro não itera
print(nove_digitos)