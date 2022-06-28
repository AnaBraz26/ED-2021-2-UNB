def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
def bubbleSortDec(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] < alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
########################################################
n = ''

while n != 0:
    n = int(input())
    valores = []
    val2 = []
    cte = []
    org = []
    org2 = []
    
    if n != 0:
        for i in range(n):
            cte.append(input().split(" = "))
            valores.append(float(cte[i][1]))
            
        bubbleSortDec(valores)

        for i in range(len(valores)):
            val2.append(round(valores[i] % 1, 2))
                                 
        bubbleSort(val2)
        
        for i in range(len(val2)):
            for j in range(len(valores)):
                if round(valores[j] % 1, 2) == val2[i]:
                    if valores[j] not in org2:
                        org2.append(valores[j])
                       
        for j in range(len(org2)):
           for i in range(len(cte)):
               if float(cte[i][1]) == org2[j]:
                   org.append(cte[i][0])
                    
        for i in range(len(org) - 1):
            print(org[i] +' < ', end = '')
        print(org[len(org) - 1])
            
    