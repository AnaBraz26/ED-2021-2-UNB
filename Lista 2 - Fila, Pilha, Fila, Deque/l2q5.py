mn = input().split(' ')
seq = input().split(' ')
mn1 = []
seq1 = []
soma = 0
h = 0

for i in range(len(mn)):
    mn1.append(int(mn[i]))
    
for j in range(len(seq)):
    seq1.append(int(seq[j]))

for k in range(mn1[0] - mn1[1] + 1):    
    for l in range(k,mn1[1]+h):
        soma = soma + seq1[l]
        media = soma/mn1[1]
    
    if media < 0:
        media = media - 1
        print(int(media))
    else:
        print(int(media))
    soma = 0
    media = 0
    h = h + 1 
    


    
