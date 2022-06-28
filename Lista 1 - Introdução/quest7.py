# Defina o código aqui.
import math

n = int(input())
coelho = input().split(" ")
raposa = input().split(" ")
c = []
r = []
nc = []


for i in coelho:
    c.append(float(i))

for i in raposa:
    r.append(float(i))
    
for i in range(n):
    caso = input().split(" ")
    
    for i in caso:
        nc.append(float(i))
        
    dist_coelho = math.sqrt(((nc[0] - c[0]) ** 2) + ((nc[1] - c[1]) ** 2))
    dist_raposa = math.sqrt(((nc[0] - r[0]) ** 2) + ((nc[1] - r[1]) ** 2))
    dist_raposa = dist_raposa/2
   
    if (dist_coelho < dist_raposa):
        print("O coelho pode escapar pelo buraco (%.3f, %.3f)."%(nc[0], nc[1]))
        exit()
    nc =[]
    
print("O coelho nao pode escapar.")




        