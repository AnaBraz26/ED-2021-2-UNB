import math

def fatorial(n):
    if n == 0:
        return 1
    else:
        if n > 6:
            return math.ceil((n * fatorial(n-1)) % 2357)
        else:
            return n * fatorial(n-1)

linha = int(input())

for i in range(linha):
    numero = int(input())
    
    for i in range(numero + 1):
        print(fatorial(i), end = " ")
    print()