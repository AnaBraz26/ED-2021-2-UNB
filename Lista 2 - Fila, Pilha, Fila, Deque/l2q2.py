def exibe_candidatos(deque, pos, ordem):
    if(deque.size() > 0 or deque.size() < pos):
        if ordem == 'direta':
            for i in range(0,pos):
                deque.remove_front()
            for j in range(deque.size()):
                print(deque.remove_front())
        else:        
            for i in range(0,(deque.size() - pos - 1)):
                deque.remove_rear()
            for j in range(deque.size()):
                print(deque.remove_rear())
           