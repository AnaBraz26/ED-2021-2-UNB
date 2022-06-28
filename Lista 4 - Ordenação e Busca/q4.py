def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

n = int(input())
media = []

for i in range(n):
    media.append(input().split(' ', 1))
    
SS = []
MS = []
MM = []
MI = []
II = []
SR = []

for i in range(len(media)):
    if media[i][0] == 'SS':
        SS.append(media[i][1])
    if media[i][0] == 'MS':
        MS.append(media[i][1])
    if media[i][0] == 'MM':
        MM.append(media[i][1])
    if media[i][0] == 'MI':
        MI.append(media[i][1])
    if media[i][0] == 'II':
        II.append(media[i][1])
    if media[i][0] == 'SR':
        SR.append(media[i][1])

bubbleSort(SS)
bubbleSort(MS)
bubbleSort(MM)
bubbleSort(MI)
bubbleSort(II)
bubbleSort(SR)

for i in range(len(SS)):
    print('SS %s' %(SS[i]))
for i in range(len(MS)):
    print('MS %s' %(MS[i]))    
for i in range(len(MM)):
    print('MM %s' %(MM[i]))    
for i in range(len(MI)):
    print('MI %s' %(MI[i]))    
for i in range(len(II)):
    print('II %s' %(II[i]))
for i in range(len(SR)):
    print('SR %s' %(SR[i]))
    
