n = int(input())
tempo = 0
roupa = []
cor = []


for i in range(n):
    tipo = input().split(" ")
    for j in range(1):
        roupa.append(tipo[j])
        cor.append(tipo[j+1])
        tempo = tempo + int(tipo[j+2])
        
roupa.reverse()
cor.reverse()

for i in range(n):
    print("Tipo: %s, Cor: %s" %(roupa[i], cor[i]))
    
print("Total de roupas: %d" %(n))
print("Total de tempo: %d" %(tempo))
    