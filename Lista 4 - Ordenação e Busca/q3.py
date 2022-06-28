def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
     
n = int(input())
seq = []
seq_nomes = []
org = []

for i in range(n):
    nome = input()
    t1,t2,t3 = input().split(' ')    
    t1 = float(t1)
    t2 = float(t2)
    t3 = float(t3)
        
    ttotal = float(t1+t2+t3)
    
    seq_nomes.append([nome,ttotal])
    seq.append(ttotal)
    insertionSort(seq)
    
   
for j in range(len(seq)):
    for i in range(len(seq_nomes)):
        if seq_nomes[i][1] == seq[j]:
            if seq_nomes[i][0] not in org:
                org.append(seq_nomes[i][0])
                print(seq_nomes)

j = 1
for i in range(len(seq)):
    m = seq[i]/60
    seg = (seq[i])-(60 * int(m))
    
    if seg < 10.0:
        print(f'%d. %s (%d:0{seg:.3f})' %(j,org[i],int(m)))
    else:
        print(f'%d. %s (%d:{seg:.3f})' %(j,org[i],int(m)))
    j = j + 1
