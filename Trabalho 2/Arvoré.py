def show(node, level=0):
    print(f'{"---" * level}{node.key}')    
    for f in sorted(node.child, key=lambda x:x.key): 
        show(f, level + 1)
        
class Node:
    def __init__(self, chave):
        self.key = chave
        self.child = []
        
    def add_child(self, no):
        self.child.append(no)
    
    def get_child(self, chave):
        for i in self.child:
            if i.key == chave:
                return i
    
    def __eq__(self,chave):
        return chave == self.key
        
    def __getitem__(self, key):
        for i in self.child:
            if i.key == key:
                return i
            
    def __setitem__(self, key, data):
        for i in self.child:
            if i.key == key:
                self.child.remove(key)
                
        self.child.append(data)


tree = Node('/')
i = int
caminho = '/'
current = str

while True:
    comando = input().split(" ")
    add = []
    cont = 0 #pra saber se o diretório já existe    
    
    if comando[0] == 'mkdir':
         add = comando[1].split('/')
         
         if add[1] == '':
            print('DIRETÓRIO JÁ EXISTE')
         else:
             for i in range(1,len(add)):
                 if i == 1 and (tree.get_child(add[i]) == None):
                     tree[add[i]] = Node(add[i])                                
                 elif i == 2 and (tree[add[1]].get_child(add[i]) == None):
                     tree[add[1]][add[i]] = Node(add[i])
                 elif i == 3 and (tree[add[1]][add[2]].get_child(add[i]) == None):
                     tree[add[1]][add[2]][add[i]] = Node(add[i])
                 elif i == 4 and (tree[add[1]][add[2]][add[3]].get_child(add[i]) == None):
                     tree[add[1]][add[2]][add[3]][add[i]] = Node(add[i])
                 else:                
                     cont += 1
             if cont == (len(add) - 1):
                 print('DIRETÓRIO JÁ EXISTE')
            
           
             
    elif comando[0] == "cd":
        add = comando[1].split('/')
        
        
        if add[0] == '':
            add.pop(0)
            if len(add) != 1:
                if tree.get_child(add[0]) == add[0]:
                    if len(add) > 2:
                        if tree[add[0]][add[1]].get_child(add[2]) == add[2]:
                            if len(add) > 3:
                                if tree[add[0]][add[1]][add[2]].get_child(add[3]) == add[3]:
                                   caminho = comando[1]
                                else:
                                    print('CAMINHO INVÁLIDO')
                            else:
                                caminho = comando[1]
                        else:
                            print('CAMINHO INVÁLIDO')
                    else:
                        caminho = comando[1]
                else:
                    print('CAMINHO INVÁLIDO')
        else:
            if add[0] == '.':
                caminho = caminho
                        
                
    elif comando[0] == 'touch': #Falta os pontos
        add = comando[1].split('/')
        
        arq = add[len(add) - 1].split('.')
     
        if len(arq) == 2:
            if add[0] == '':
                add.pop(0)
                if tree.get_child(add[0]) == add[0]:
                    if len(add) > 2:
                        if tree[add[0]][add[1]].get_child(add[2]) == add[2]:
                            if len(add) > 3:
                                if tree[add[0]][add[1]][add[2]].get_child(add[3]) == add[3]:
                                    if tree[add[0]][add[1]][add[2]].get_child(add[3]) == add[3]:
                                        print('ARQUIVO JÁ EXISTE')
                                    else:
                                        tree[add[0]][add[1]][add[2]][add[3]] = Node(add[3])
                                else:
                                    print('CAMINHO INVÁLIDO')
                            else:
                                if tree[add[0]][add[1]].get_child(add[2]) == add[2]:
                                    print('ARQUIVO JÁ EXISTE')
                                else:
                                    tree[add[0]][add[1]][add[2]] = Node(add[2])
                        else:
                            print('CAMINHO INVÁLIDO')
                    else:
                        if tree[add[0]].get_child(add[1]) == add[1]:
                            print('ARQUIVO JÁ EXISTE')
                        else:
                            tree[add[0]][add[1]] = Node(add[1])
                else:
                    print('CAMINHO INVÁLIDO')                 
            else:
                if tree.get_child(add[0]) == add[0]:
                    print('ARQUIVO JÁ EXISTE')
                else:
                    tree[add[0]] = Node(add[0])
        else:
            print('CAMINHO INVÁLIDO')
            
    
    
    #elif comando[0] == 'find':
    #     print('find')
    
    elif comando[0] == 'pwd':
         print(caminho)
         
    elif comando[0] == 'rm':
         add = comando[1].split('/')
         
         if tree.get_child(add[1]) == None:
             print('ARQUIVO ou DIRETÓRIO não existe')
         else:
             print('tem mais')    
    
    
    elif comando[0] == 'show':
        show(tree)        
    elif comando[0] == 'end':
        exit()
        
    
    
    
    
    
    
    
    
    
    
    
    ## Nota: 4,17
    
    
    
    
    
    
    
    
    
    