def fib(n):
    if n == 0:        
        return 0
    elif n == 1:        
        return 1
    else: 
        return fib(n-1) + fib(n-2) 
    
def fibonacci(n):
    vetor = []
    for i in range(n):
        vetor.append(fib(i))
    return vetor
    
    
print(fibonacci(10))