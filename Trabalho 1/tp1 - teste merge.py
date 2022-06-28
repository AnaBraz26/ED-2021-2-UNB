def merge(vetor):
    vint = []
    new_vetor = []
    mg = []

    for i in vetor:
        vetor = vetor.replace("[", '')
        vetor = vetor.replace("]", '')
        vetor = vetor.replace(",", '')
    vetor = vetor.split(' ')
    
    for i in range(len(vetor) - 1):
        if i%2 == 0:
            new_vetor.append([int(vetor[i]), int(vetor[i+1])])
    new_vetor.sort()       
    
    if len(new_vetor)%2 == 0:
        for i in range(len(new_vetor)):
            if i%2 == 0:
                if new_vetor[i][1] == new_vetor[i+1][1] or new_vetor[i][1] > new_vetor[i+1][0]:
                    mg.append([new_vetor[i][0], new_vetor[i+1][1]])
                else:
                    mg.append([new_vetor[i][0], new_vetor[i+1][1]])
    else:
        for i in range(len(new_vetor) - 1):
            print(new_vetor[i][1])
            print(new_vetor[i+1][1])
            if new_vetor[i][1] < new_vetor[i+1][1] or new_vetor[i][1] > new_vetor[i+1][1] :
                mg.append([new_vetor[i][0], new_vetor[i][1]])
                     
                
    if mg[0][1] != mg[1][0]:
         for i in range(len(mg) - 1):
             print(mg[i], end = ' ')
         print(mg[len(mg) - 1])
    else:
         print('[%d, %d]' %(mg[0][0], mg[1][1]))
        

comando = input().split(' ',1)

if comando[0] == 'merge':
    merge(comando[1])