def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][2] > alist[i+1][2]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
            elif alist[i][2] ==  alist[i+1][2]:
                if alist[i][3] > alist[i+1][3]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
                    
def bubbleSortNome(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1] > alist[i+1][1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
def bubbleSortNumb(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

n = int(input())
pret = []
alt = []
peso = []
org = []
org1 = []
org2 = []
org3 = []
org4 = []
org5 = []

for i in range(n):
    pret.append(input().split(' ', 3))
    
bubbleSort(pret)

for i in range(len(pret)):
    if pret[i][2] == '180' and pret[i][3] == '75':
        org.append(pret[i])        
bubbleSortNome(org)

for i in range(len(org)):
    print(org[i][1]+', '+org[i][0])

for i in range(len(pret)):
    if pret[i][2] == '180' and pret[i][3] != '75':
        org1.append(pret[i])
bubbleSort(org1)

for i in range(len(org1)):
    print(org1[i][1]+', '+org1[i][0])

for i in range(len(pret)):
    if pret[i] not in org1 and pret[i] not in org:
        org2.append(pret[i])

for i in range(len(org2)):
    org4.append(abs(180 - int(org2[i][2])))
bubbleSortNumb(org4)
bubbleSortNome(org2)
