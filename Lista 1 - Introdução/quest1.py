class Um(object):
    def __init__(self,velocidade):
        self.vel = velocidade
        
    def __gt__(self, other):
        return self.vel > other.vel
    
    def __str__(self):
        return str(self.vel)
    
class Dois(object):
    def __init__(self,velocidade1):
        self.vel = velocidade1
        
    def __gt__(self, other):
        return self.vel > other.vel
    
    def __str__(self):
        return str(self.vel)
    
class Tres(object):
    def __init__(self, velocidade2):
        self.vel = velocidade2
        
    def __gt__(self, other):
        return self.vel > other.vel
    
    def __str__(self):
        return str(self.vel)
    
qtd_lesma = int(input())
lista_lenta= []
lista_media = []
lista_rapida = []

for i in range(qtd_lesma):
    vel = int(input())
    if(vel < 10):
       lenta = Um(vel)
       lista_lenta.append(lenta)
    elif((vel >= 10) and (vel < 20)):
       media = Dois(vel)
       lista_media.append(media)
    else:
       rapida = Tres(vel)
       lista_rapida.append(rapida)
       
if (len(lista_lenta) != 0): 
    print(max(lista_lenta), end = " ")
else:
    print(0, end = " ")

if (len(lista_media) != 0): 
    print(max(lista_media), end = " ")
else:
    print(0, end = " ")

if (len(lista_rapida) != 0): 
    print(max(lista_rapida))
else:
    print(0)