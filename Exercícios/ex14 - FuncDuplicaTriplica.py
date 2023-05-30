
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