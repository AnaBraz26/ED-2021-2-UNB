class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
###########################################################    

frase = input().split(" ")
prioridade = int(input())
tam = len(frase)/2
print("Tamanho da fila: %d" %(tam - prioridade))

atividade = Queue()
priority = Queue()

pp = [] #primeiras palavras
ps = [] #palavras que vem dps
numeros = []
comp = '0'

for i in range(len(frase)):
    if i%2 != 0:
        if comp <= frase[i]:
            comp = frase[i]
            ps.append(frase[i-1])
        else:
            pp.append(frase[i-1])

pp.reverse()

for i in range(len(frase)):
    if i%2 != 0:
        numeros.append(frase[i])

numeros.sort()

for i in range(len(numeros)):   
    priority.enqueue(numeros[i])

for i in range(len(pp)):
    atividade.enqueue(pp[i])

for i in range(len(ps)):
    atividade.enqueue(ps[i])

for i in range(prioridade):
    priority.dequeue()
    atividade.dequeue()

for i in range(atividade.size()):
        print("Atividade: %s, Prioridade: #%s"
              %(atividade.dequeue(), priority.dequeue()))
    
    
    
