class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
    
frase = input()
deque = Deque()
deque.isEmpty()
for i in range(0, len(frase)):
    if 'a' <= frase[i] <= 'z' or frase[i] == ' '  or frase[i] == '>' or 'A' <= frase[i] <= 'Z':
        deque.addFront(frase[i])
    elif '0' <= frase[i] <= '9' or  frase[i] == ',' or frase[i] == '.' :        deque.addRear(frase[i])
    elif frase[i] == '*':
        print(deque.removeFront(), end = "")
    elif frase[i] == '+':
        print(deque.removeRear(), end = "")