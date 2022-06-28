class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        tmp = self.head
        lstr = ''
        i = 0
        soma = 0
        n = 0
        while tmp != None:            
            L = tmp.data.split()
            F = float(L[i+1])
            soma = soma + F
            lstr += str(L[i]) + ': R$ %.02f \n' %(F)             
            tmp = tmp.getNext()
            n = n + 1
           
        lstr += '----------------------\n'
        lstr += '%d item(ns): R$ %.02f' %(n, soma)
        
        return lstr

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
Lproduto = UnorderedList()
Lvalor = UnorderedList()
i = 0

lista_compras = []

while i < 1:
    compra = input()
    
    if len(compra) < 20:
        if(compra == 'fim'):
            i = i + 1
        else:
            produto = compra.split()
            c1 = compra.split()   
            lista_compras.append(c1[0])
            lista_compras.append(c1[1])
            if produto[0] != '-':        
                Lproduto.add(compra)         
            else:         
                for k in range(len(produto)):
                    if k%2 == 0:
                        for j in range(len(lista_compras) - 1):
                            if produto[1] == lista_compras[j]:                    
                                l = str(lista_compras[j]) + ' ' + str(lista_compras[j+1])
                                Lproduto.remove(l)
                    
            
print(f'{Lproduto}')


    
