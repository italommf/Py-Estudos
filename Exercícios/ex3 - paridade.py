num = input('Digite um numero inteiro: ')

2
if num.isdigit():

    num = int(num)
    
    if num % 2 == 0:
        print(f'o numero {num} É par')
    else:
        print(f'o numero {num} NÃO é par')
  
else:

    print(f'O numero {num} não é um numero inteiro')
