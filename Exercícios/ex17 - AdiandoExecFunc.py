def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y): 
        return funcao(x, y)
    return interna
'''
a fução interna recebe o segundo parâmetro na chamada nos prints
ela é a responsavel por executar o codigo de "criar_função" (o código de
"criar_função" vai dentro de "interna"). Isso adia a execução de "criar 
função". A função "criar_função" é ""pausada"" e só é concluída quando a 
chamada no final do código é realizada com a passagem do parâmetro "y" 
(10). Nesse meio tempo eu posso executar outras funções enquanto esta 
está em pause.

'''

soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(10))
print(multiplica_por_dez(10))