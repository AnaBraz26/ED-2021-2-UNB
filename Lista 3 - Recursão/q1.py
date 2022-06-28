from itertools import combinations

def soma(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + soma(n[1:])
    
premios = input().split(" ")
p = []

for j in range(len(premios)):
    p.append(int(premios[j]))

sorteado = int(input())

comb = combinations(p, 0)

for i in range(len(p)):
    comb = combinations(p, i+1)
    for j in list(comb):
        if soma(j) == sorteado:
            print("E possivel ganhar.")
            exit()

print('Impossivel ganhar.')
