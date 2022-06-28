def buscarArtefato():
    flag = bb8.verificarNorte()
    if flag == True:
          bb8.moverNorte()
          resposta = bb8.verificarChao()