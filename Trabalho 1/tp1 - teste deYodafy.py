def deYodafy(s):
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
    

comando = input().split(" ")

if comando[0] == 'deYodafy':
    valores = []
    for i in range(1,len(comando)):
        valores.append(comando[i])
    print(valores)
    deYodafy(valores)