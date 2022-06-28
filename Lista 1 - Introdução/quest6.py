def primos_gemeos(x):
    qtd_pares = x * 2
    primo = 1
    p = n = 0
    np = [] #todos os numeros primos
    ns = [] #numeros primos gemeos sem tupla
    lt = [] #lista das tuplas dos gemeos

    while (primo < 3000): #lista todos o sprimos até 3000
        for i in range(1,primo):
            if(primo % i == 0):
                p = p + 1
        
        if(p == 1):
            np.append(primo)
        
        p = 0    
        primo = primo + 1

    for i in range(0,len(np)): #identifica e coloca na tupla
        if np[i+1] == (np[i] + 2):
            ns.append(np[i])
            ns.append(np[i+1])            
            qtd_pares = qtd_pares - 2
            if qtd_pares == 0:
                for j in range(0,len(ns)):
                    if(j % 2 == 0):
                        nt = (ns[j], ns[j+1])
                        lt.append(nt)
                        n = n + 2                    
                        if(n == len(ns)):
                            print(lt)
                            exit()   
                      
        

