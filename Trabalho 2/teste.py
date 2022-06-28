def dfs(v, numb, parente, j):
    numb[v] = '1'
    for i in lista[v]:
        if numb[i] == '2':
            ciclo = dfs(i, numb, parente, j+1)
        elif numb[i] == '1':
            return j

    numb[v] = '2'

    return 0
    
n = int(input())
lista = {}

for i in range(n):
    seq= input().split()
    v_id = seq[0]
    lista[v_id] = []

    for j in seq[2:]:
        v_adj = j
        lista[v_id].append(v_adj)

numb = {}
parente = {}
ciclo = False

for i in lista.keys():
    numb[i] = '2'
    parente[i] = None

j = -1
cont = 0
for i in lista.keys():
        j += 1
        if numb[i] == '2':
            ciclo = dfs(i, numb, parente, j)
            print(ciclo)
            cont += 1

if cont == 1:
    print(0)
else:
    if ciclo == 0:
        print('Forevis alonis...')
    else:
        print(ciclo - 1)