qtd_jogadores = int(input())
habilidade = input().split(" ")
v_hab = []

for i in habilidade:
    v_hab.append(int(i)) #muda o vetor de string para int

v_hab.sort() #coloca ordenado menor-maior
r = qtd_jogadores - 11
r_hab = 0 #nivel de habilidade dos reservas

if r <= 11:
    for i in range(r):
        r_hab = r_hab + v_hab[i]
else:
    for i in range(r):
        r_hab = r_hab + v_hab[i]
    rnc = r - 11  #reservas não convacados
    for i in range(rnc):
        r_hab = r_hab - v_hab[i]

v_hab.reverse()  #inverte o vetor
t_hab = 0 #nivel de habilidade ddos titulares 
for i in range(11):
    t_hab = t_hab + v_hab[i]

dif = t_hab - r_hab #diferença das habilidade
print(dif)
