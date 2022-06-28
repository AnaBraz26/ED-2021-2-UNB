def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci1(n, v, tam):
    if n == 0:
        v.append(n)
        return 0, v
    elif n == 1 and tam == 1:
        v.append(0)
        v.append(n)
        return 1, v
    elif n == 1 and tam != 1:
        v.append(n)
        return 1, v
    else:
        v.append(n)
        return fibonacci1(n-1, v,tam) + fibonacci1(n-2,v,tam), v
    
n = int(input())

i = 0
vetor = []

seq, vetor = fibonacci1(n,vetor, n)
print("fibonacci(%d) = %d." %(n, fibonacci(n)))

cont = 0
j = 0
tam = n

while tam >= 0:
    if n == 0:
        print("1 chamada(s) a fibonacci(0).")
        exit()
    elif n == 1:
        print("0 chamada(s) a fibonacci(0).")
        print("1 chamada(s) a fibonacci(1).")
        exit()
    else:
        for i in range(len(vetor)):
            if j == vetor[i]:
                cont = cont + 1         
        print("%d chamada(s) a fibonacci(%d)" %(cont, j))
    j = j + 1
    cont = 0
    tam = tam - 1
    

