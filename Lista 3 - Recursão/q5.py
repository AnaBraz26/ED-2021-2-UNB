def fibonacci(n):
    if n == 0:        
        return 0
    elif n == 1:       
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def fibonacci1(n, v, i, tam):
   v.append(i)
   if n == 0:
       if tam == 0:
           return 0, 1
       else:
           return 0, i
   elif n == 1:
       if tam == 1:
           return 0, 1
       else:
           return 1, i
   else:
       return fibonacci1(n-1,v, i, tam) + fibonacci1(n-2,v,i, tam), v
    
n = int(input())
i = 0
v = []

tam = n

seq, i = fibonacci1(n,v,i, tam)

if tam == 0 or tam == 1:
    print("Fib(%d) = %d (%d chamadas)" %(n, fibonacci(n), i))
else:
    print("Fib(%d) = %d (%d chamadas)" %(n, fibonacci(n), len(i)))
    