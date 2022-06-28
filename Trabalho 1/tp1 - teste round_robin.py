class Deque:
    def __init__(self):
        self.items = []
   
    def __repr__(self):
        return str(self.items)
    
    def __getitem__(self, index):
        return self.items[index]

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
#################################################################################################### 
def crypto(v):
    j = 0
    crp = []
    cont_neg = 0
    cont_pos = 0
    
    for i in range(len(v) + 1):
        j = j + 1
        crp.append(j)
    
    for i in range(len(v)):
        if v[i] == '-':
            cont_neg = cont_neg + 1
        elif v[i] == '+':
            cont_pos = cont_pos + 1
    

    if cont_neg == len(v):
        crp.reverse()
        for i in range(len(crp)):
            print(crp[i], end = '')
        print()
    elif cont_pos == len(v):
        for i in range(len(crp)):
            print(crp[i], end = '')
        print()
    else:        
        for i in range(len(crp) - 1):
            if v[i] == '+':
                print(crp[i], end = '')
            elif v[i] == '-':
                if i != len(v) - 1:
                    if v[i+1] == '-':
                        i += 1
                        temp = crp[i]
                        crp[i] = crp[i+1]
                        crp[i+1] = temp
                        print(crp[i], end = '')
                        i -= 1
                        temp = crp[i]
                        crp[i] = crp[i+1]
                        crp[i+1] = temp
                    else:
                        temp = crp[i]
                        crp[i] = crp[i+1]
                        crp[i+1] = temp
                        print(crp[i], end = '')
        if v[len(v) - 1] == '-':
            print(crp[len(crp) - 1], end = '')
            print(crp[len(crp) - 2])
        else:
            print(crp[len(crp) - 1])
    
####################################################################################################         
def deYodafy(s):
    s = s.split(' ')
    s.reverse()
    
    for i in s[0]:
        if i == '!' or i == '?' or i == '.':
            s.append(i)
            
    pontuação = ['!', '?', '.']
    
    for i in pontuação:
        s[0] = s[0].replace(i,'')
 
    for i in range(len(s) - 2):
        print(s[i], end = " ")
    print(s[len(s) - 2], end = "")
    print(s[len(s) - 1])
#################################################################################################### 
def merge(vetor):
    vint = []
    new_vetor = []
    mg = []

    for i in vetor:
        vetor = vetor.replace("[", '')
        vetor = vetor.replace("]", '')
        vetor = vetor.replace(",", '')
    vetor = vetor.split(' ')
    
    for i in range(len(vetor) - 1):
        if i%2 == 0:
            new_vetor.append([int(vetor[i]), int(vetor[i+1])])
    new_vetor.sort()       
    
    if len(new_vetor)%2 == 0:
        for i in range(len(new_vetor)):
            if i%2 == 0:
                if new_vetor[i][1] == new_vetor[i+1][1] or new_vetor[i][1] > new_vetor[i+1][0]:
                    mg.append([new_vetor[i][0], new_vetor[i+1][1]])
                else:
                    mg.append([new_vetor[i][0], new_vetor[i+1][1]])
    else:
        for i in range(len(new_vetor) - 1):
            if new_vetor[i][1] < new_vetor[i+1][1] or new_vetor[i][1] > new_vetor[i+1][1] :
                mg.append([new_vetor[i][0], new_vetor[i][1]])
                     
                
    if mg[0][1] != mg[1][0]:
         for i in range(len(mg) - 1):
             print(mg[i], end = ' ')
         print(mg[len(mg) - 1])
    else:
         print('[%d, %d]' %(mg[0][0], mg[1][1]))
         
####################################################################################################      
processo = Deque()
comando = Deque()
loop = True
vetor_comandos = []
h = 0

while loop:
    cmd = input().split(' ')
    
    if cmd[0] == 'add':
        n = int(cmd[1])
        for i in range(n):
            comando.addRear(input())
            
        while comando.isEmpty() == False:
            vetor_comandos.append(comando.removeFront())          
        processo.addRear(vetor_comandos)
        vetor_comandos = []
    elif cmd[0] == 'process':
        if processo.size() > 0:
            funcao = processo.removeFront()
            if len(funcao) > 1:
                pcmd = funcao[0].split(' ', 1)
                funcao.pop(0)
                processo.addRear(funcao)
            else:
                pcmd = funcao[0].split(' ', 1)           
            
            if pcmd[0] == 'crypto':
                crypto(pcmd[1])
            elif pcmd[0] == 'deYodafy':
                deYodafy(pcmd[1])
            elif pcmd[0] == 'merge':
                merge(pcmd[1])
    elif cmd[0] == 'halt':
        print('%d processo(s) e' %(processo.size()), end = '')
        loop1 = True
        while processo.isEmpty() == False:
            cont = processo.removeFront()
            h += len(cont)
        print(' %d comando(s) órfão(s).' %(h))
        loop = False

        
        
