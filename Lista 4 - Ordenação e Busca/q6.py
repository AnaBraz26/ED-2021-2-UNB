def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
def bubbleSortDuplo(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1] < alist[i+1][1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                
n = int(input())
inf = []

for i in range(n):
    inf.append(input().split(' '))
    
frase = input().split(' ')
frase1 = input()
num = ''

for i in range(len(frase)):
    if frase[i].isdigit():
        num = frase[i]
        
num = int(num)
ocorrencias = []
oc_num = []
on = []
cont = 0
cont1 = False
cont2 = 0
cont3 = 0

for i in range(num):
    cidadao = input()
    cont = 0
    cont1 = 0
    cont3 = 0
    ocorrencias = []
    oc_num = []
    on = []
    
    for j in range(len(inf)):
        if inf[j][0] == cidadao:
            cont1 = True
            ocorrencias.append(inf[j][1])            
        else:
            cont = cont + 1    
      
    bubbleSort(ocorrencias)    
    
    if len(ocorrencias) > 1:
        for k in range(len(ocorrencias)):
            if k != len(ocorrencias) - 1:
                if ocorrencias[k] == ocorrencias[k+1]:
                    cont2 = cont2 + 1
                else:
                    oc_num.append([ocorrencias[k], cont2 + 1])
                    cont2 = 0  
            else:
                oc_num.append([ocorrencias[k], cont2 + 1])
                cont2 = 0
                
    if cont1:
        print('Teje, preso %s!' %(cidadao))        
    if cont == len(inf):
        print('Grato, cidadao %s.' %(cidadao))
    
    if len(ocorrencias) == 1:
         print('- Art. %s: 1 ocorrencia(s).' %(ocorrencias[0]))
    elif len(ocorrencias) > 1:         
         bubbleSortDuplo(oc_num)
        
         for i in range(len(oc_num)):
             if oc_num[i][1] == 1:
                 on.append(int(oc_num[i][0]))
                                  
             bubbleSort(on)
             
         for i in range(len(oc_num)):
             if oc_num[i][1] != 1:
                print('- Art. %s: %d ocorrencia(s).' %(oc_num[i][0], oc_num[i][1]))
         
         for i in range(len(on)):
                print('- Art. %s: 1 ocorrencia(s).' %(on[i]))
     
   
   
    
    
       
    

