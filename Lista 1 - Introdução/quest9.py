palavra = input()
inverso = ''.join(reversed(palavra))
tamanho = len(palavra)
cont = cont1 =0

for i in range(tamanho):
    if(palavra[i] != inverso[i]):
        cont = cont + 1
        if(cont == 3):
            print("IMPOSSÍVEL")
            exit()
    elif(palavra[i] == inverso[i]):
        cont1 = cont1 + 1
        if(cont1 == (tamanho - 1) and (tamanho % 2) == 0 ):
            print("IMPOSSÍVEL")
            exit()
print("POSSÍVEL")

       
