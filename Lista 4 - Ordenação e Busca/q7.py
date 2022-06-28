def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1] < alist[i+1][1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
                    
def bubbleSortL(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if int(alist[i][1]) <= int(alist[i+1][1]) and int(alist[i][2]) <= int(alist[i+1][2]):
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
               
                    
def bubbleSortR(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1] <= alist[i+1][1] and alist[i][2] <= alist[i+1][2] and alist[i][3] <= alist[i+1][3] and  alist[i][4] <= alist[i+1][4] and alist[i][5] <= alist[i+1][5]:
                    temp = alist[i]
                    alist[i] = alist[i-1]
                    alist[i-1] = temp
                    
def bubbleSortNome(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1] == alist[i+1][1] and alist[i][2] == alist[i+1][2] and alist[i][3] == alist[i+1][3] and alist[i][4] == alist[i+1][4] and alist[i][5] == alist[i+1][5] and alist[i][0] <= alist[i+1][0]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        

rodada = 20
j = 0
pont = 0
vit = 0
saldo = 0
gols = 0
gols_contra = 0
total = 0
tabela = []

while j < 20:
    time = input().split(' ', 1)
    placar = time[1].split(' ')
    
    for i in range(len(placar)):
        p = placar[i].split('x')        
        if p[0] > p[1]:
            pont += 3
            vit += 1
        elif p[0] == p[1]:
            pont += 1
         
        gols += int(p[0])
        gols_contra += int(p[1])
        
    total+= pont     
    saldo = gols - gols_contra
    tabela.append([time[0], pont, vit, saldo, gols, gols_contra])
    pont = 0
    vit = 0
    saldo = 0
    gols = 0
    gols_contra = 0
    j += 1
    
bubbleSort(tabela)

liberta = []
rebaixamento = []

for i in range(0, 10):
    liberta.append(tabela[i])

bubbleSortL(liberta)
bubbleSortNome(liberta)

print('Media de pontos: %.2f' %(total/20))

print('Liberadores: ', end = ' ')
for i in range(0,3):
    print(liberta[i][0]+', ', end ='')
print(liberta[3][0])


for i in range(10, 20):
    rebaixamento.append(tabela[i])

bubbleSortNome(rebaixamento)
bubbleSortR(rebaixamento)

rebaixamento.reverse()
print(rebaixamento)
print('Rebaixados: ', end = '')
for i in range(0,3):
    print(rebaixamento[i][0]+', ', end ='')
print(rebaixamento[3][0])


        
    
    
    
    
    
    
    
    
    
    
    
 