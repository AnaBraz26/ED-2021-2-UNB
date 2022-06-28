import math
byte = int(input())
print("Transmitindo %d bytes..." %(byte))

total = t_total = t_rest = ver = cont =  cont1 = 0 
                              
while(total != byte):
    dados = int(input())
    total = total + dados   #vai somando até dar o bytes completos
    t_total = t_total + 1   #tempo total da transmissão
    ver = ver + dados       #contador de byte trans. por 5 seg
    boff = byte - total
    cont = cont + 1
    if cont == 5:
        if ver == 0:
            print("Tempo restante: pendente...")
            cont = 0
        elif (total == byte):
            print("Tempo total: %d segundos." %(t_total))
        else:
            if cont1 == 0:
                t_rest = math.ceil(((byte * 5)/ver) - 5) 
                print("Tempo restante: %d segundos." %(t_rest))
                ver = 0
                cont = 0
                cont1 = cont1 + 1
            else:
                t_rest = math.ceil(((boff * 5)/ver)) 
                print("Tempo restante: %d segundos." %(t_rest))
                ver = 0
                cont = 0
    elif(total == byte):
            print("Tempo total: %d segundos." %(t_total))