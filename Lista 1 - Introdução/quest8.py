casos = int(input())

for i in range(casos):
    string = input()
       

    for j in range(len(string)):
         if 'A' <= string[j] <= 'Z':
            if '1' <= string[j+1] <= '9':
                if len(string) != j+2:
                    if '0' <= string[j+2] <= '9':
                        n = int(string[j+1])
                        m = int(string[j+2])
                        total = n*10 + m
                        for i in range(total):
                            print(string[j], end = "")                        
                    else:
                        n = int(string[j+1])
                        for i in range(n):
                            print(string[j], end = "")                       
                else:
                    n = int(string[j+1])
                    for i in range(n):
                        print(string[j], end = "")
                    
    print()
  