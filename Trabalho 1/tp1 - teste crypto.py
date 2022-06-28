def crypto(v):
    j = 0
    crp = []
    cont_neg = 0
    cont_pos = 0
    
    for i in range(len(v) + 1):
        j = j + 1
        crp.append(j)
    
    for i in range(len(v)):
        if v[i] == '-':
            cont_neg = cont_neg + 1
        elif v[i] == '+':
            cont_pos = cont_pos + 1
    

    if cont_neg == len(v):
        crp.reverse()
        for i in range(len(crp)):
            print(crp[i], end = '')
        print()
    elif cont_pos == len(v):
        for i in range(len(crp)):
            print(crp[i], end = '')
        print()
    else:        
        for i in range(len(crp) - 1):
            if v[i] == '+':
                print(crp[i], end = '')
            elif v[i] == '-':
                if i != len(v) - 1:
                    if v[i+1] == '-':
                        i += 1
                        temp = crp[i]
                        crp[i] = crp[i+1]
                        crp[i+1] = temp
                        print(crp[i], end = '')
                        i -= 1
                        temp = crp[i]
                        crp[i] = crp[i+1]
                        crp[i+1] = temp
                    else:
                        temp = crp[i]
                        crp[i] = crp[i+1]
                        crp[i+1] = temp
                        print(crp[i], end = '')
        if v[len(v) - 1] == '-':
            print(crp[len(crp) - 1], end = '')
            print(crp[len(crp) - 2])
        else:
            print(crp[len(crp) - 1])
    
    
comando = input().split(" ")

if comando[0] == 'crypto':
    valores = []
    for i in comando[1]:
        valores.append(i)
    crypto(valores)

