from itertools import combinations

def soma(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + soma(n[1:])            
         
n = int(input())
v = input().split(" ")
valor = []
suma = []

for i in range(len(v)):
    valor.append(int(v[i]))

met = int(n/2)

comb = combinations(valor, 0)

for i in range(len(valor) - met):
    comb = combinations(valor, i+1)
    for j in list(comb):
        print(j)
        suma.append(soma(j))

print(max(suma))
#print(soma(valor))
