class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()
        
     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     
pilha_palavras = Stack()
pilha_numeros = Stack()

frase = input().split(" ")

pilha_palavras.isEmpty()
pilha_numeros.isEmpty()

for i in range(len(frase)):
    if '0' <= frase[i] <= '9':
        pilha_numeros.push(frase[i])
    else:
        pilha_palavras.push(frase[i])

print("Palavra:")
for i in range(pilha_palavras.size()):
    print(pilha_palavras.peek())
    pilha_palavras.pop()

print()
print("Numeros:")
for i in range(pilha_numeros.size()):
    print(pilha_numeros.peek())
    pilha_numeros.pop()