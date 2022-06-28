n = int(input())
cont = 0
cont1 = True
j = 0
for tam in range(n):
    exp = input()
    
    for i in range(len(exp)):
        if exp[i] == '(' :
            if exp[i+1] == '(':
                cont = cont + 2
            else:
                cont = cont + 1
        elif exp[i] == ')':
            for j in range(i, len(exp)):
                if exp[j] == '(' and cont1:
                    cont = cont - 2
                    cont1 = False                
    
    for i in range(len(exp)):
        if i == len(exp) - 1:
            if exp[i] == ')':
                cont = cont - 1
        elif exp[i] == ')':
            if exp[i] == ')' :            
                if exp[i+1] == ')':
                    cont = cont + 2
                else:
                    cont = cont - 1             
     
    if cont < 3:
        print("A expressão não possui duplicata.")
        cont = 0
    else:
        print("A expressão possui duplicata.")
        cont = 0
       
        


        


        