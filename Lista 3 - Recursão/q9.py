def soma(n):
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + soma(n[1:])            
         
n = int(input())
v = input().split(" ")
valor = []

for i in range(len(v)):
    valor.append(int(v[i]))


valor.sort()
met = int(n/2)

print(valor)

for i in range(len(valor) - met):
    print(valor.pop(0))

print(valor)
print(soma(valor))


