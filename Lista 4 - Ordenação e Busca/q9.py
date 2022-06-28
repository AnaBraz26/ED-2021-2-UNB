def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i][1] < alist[i+1][1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp



n,k = input().split(' ')
n = int(n)
k = int(k)
mnum = []
org = []

for i in range(n):
    num = int(input())
    if num > 0:
        m = num % k
        mnum.append([num, m])
    else:
        m = num % (-k)
        mnum.append([num, m])
    
bubbleSort(mnum)
print(mnum)

for j in range(len(mnum) - 1):
    num = mnum[j][1]
    num2 = mnum[j+1][1]
    if num != num2:
        for i in range(len(mnum)):
            if mnum[i][1] == num:
                org.append(mnum[i])
        
        for i in range(len(org) - 1):
            if org[i][0] % 2 == 0:               
                temp = org[i]
                org[i] = org[i+1]
                org[i+1] = temp
        print(org)
                
   # for l in range(len(org) - 1):
     #   print(org[l][0], end = ' ')
    org = []
    
 
        

