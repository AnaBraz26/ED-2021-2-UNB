inicio = input().split(' ')
fim = input().split(' ')
i_i = [] #vetor de inteiros para calculo de h,min,seg
f_i = [] #vetor de inteiros para calculo de h,min,seg

f = int(fim[0])
i = int(inicio[0])

if(i > f or ((inicio[0] == fim[0]) and (inicio[1] > fim[1]))):
    print("Data inválida!")
elif((inicio[0] < fim[0]) and (inicio[1] == fim[1])):
    f = int(fim[0])
    i = int(inicio[0])
    dia = f - i
    print("%d dia(s)\n0 hora(s)\n0 minuto(s)\n0 segundo(s)" %(dia))
else:
    i = inicio[1].split(":",3)
    f = fim[1].split(":",3)
    
    for cast in i:
        i_i.append(int(cast))
    for cast1 in f:
        f_i.append(int(cast1))
        
    if(i_i[2] < f_i[2]):
        seg = f_i[2] - i_i[2]
    elif(i_i[2] > f_i[2]):
        seg = (60 - i_i[2]) + f_i[2]
    else:
        seg = 0
        
    if(i_i[1] < f_i[1]):
        mnt = f_i[1] - i_i[1]
    elif(i_i[1] > f_i[1]):
        mnt = (59 - i_i[1]) + f_i[1]
    else:
        mnt = 0
        
    if(i_i[0] < f_i[0]):
        hr = f_i[0] - i_i[0]
    elif(i_i[0] > f_i[0]):
        if(i_i[1] > f_i[1]):
            hr = (23 - i_i[0]) + f_i[0]
        else:
            hr = (24 - i_i[0]) + f_i[0] 
    else:
        hr = 0
        
    if(inicio[0] != fim[0]):
        f = int(fim[0])
        i = int(inicio[0])
        dia = f - i - 1
    else:
        dia = 0
    
    print("%d dia(s)\n%d hora(s)\n%d minuto(s)\n%d segundo(s)" %(dia,hr,mnt,seg))