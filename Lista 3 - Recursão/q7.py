def soma(n):
    if len(n) == 1:
        print("%d" %(n[0]))
        return n[0]
    else:
        print("%d + soma(" %(n[0]), end = "")
        print(n[1:], end = "")
        print(")")
        return n[0] + soma(n[1:])

n = int(input())
vetor = []
impar = 1

for i in range(n):
    vetor.append(impar)
    impar = impar + 2
    
soma(vetor)
print("---------------")
print("%d ** 2 == %d" %(n, n*n))