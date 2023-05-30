# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Ordene os produtos por nome decrescente (do maior para menor) 
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

import copy

print()
print('Produtos originais abaixo !!')
print(*produtos, sep = '\n')
print()

novos_produtos = [{**p, 'preco': round(p['preco'] * 1.1, 2)} for p in copy.deepcopy(produtos)]
print()
print('Aumento de 10/100 !!')
print(*novos_produtos, sep = '\n')
print()

novos_produtos.sort(key = lambda item: item['nome'])
produtos_ordenados_por_nome = [{**p} for p in copy.deepcopy(novos_produtos)]
print()
print('Produtos ordenados por NOME (menor para o maior) !!')
print(*novos_produtos, sep = '\n')
print()

novos_produtos.sort(key = lambda item: item['preco'])
print()
print('Produtos ordenados por PREÇO (menor para o maior) !!')
print(*novos_produtos, sep = '\n')
print()

print()
print('Produtos originais abaixo NOVAMENTE ainda sem alteração!!')
print(*produtos, sep = '\n')
print()








