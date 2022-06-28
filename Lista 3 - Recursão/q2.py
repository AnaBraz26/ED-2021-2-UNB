def fatorial(n):
    if n == 1:
        return 1
    else:
        if n > 6:
            return (n * fatorial(n-1)) % 2357
        else:
            return n * fatorial(n-1)
            
print(fatorial(7))