def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] < alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                

a,t = input().split(' ')
a = int(a)
t = int(t)

ira = []
notas = []
nome_org = []

for i in range(a):
    ira.append(input().split(' ', 1))

for i in range(a):
    notas.append(ira[i][0])

print(len(notas))
print(notas)

bubbleSort(notas)

for j in range(a):
    for i in range(a):
        if ira[i][0] == notas[j]:
            if ira[i][1] not in nome_org:
                nome_org.append(ira[i][1])
            

for i in range(t):
    ti = int(input())
    
    print(nome_org[ti], end = ' ')
    print('(', end = '')
    print(notas[ti], end = '')
    print(')')