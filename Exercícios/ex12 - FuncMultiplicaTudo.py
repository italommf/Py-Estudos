numeros = input('Digite os numeros a serem multipicados separados por virgula (,): ').split(',')
lista = [int(n) for n in numeros]

def multiplica_tudo(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

print(f'O resultado da multiplicação é: {multiplica_tudo(*lista)}')
