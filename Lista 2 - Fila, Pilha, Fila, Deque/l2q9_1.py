def duplicata(exp):
    for i in range(len(exp)):
        if exp[i] == '(' :
                if exp[i+1] == '(':
                   for j in range(i, len(exp) - 1):
                       if exp[j] == ')':
                           if exp[j+1] == ')':
                              return print("A expressão possui duplicata.")
    return print("A expressão não possui duplicata.")
                               

n = int(input())
cont = 0
for tam in range(n):
    exp = input()
    
    duplicata(exp)
        
             
   
        