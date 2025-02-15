
contador = 0
sair = False # true ou false

while sair == False:
    print("contador.: ", contador)
    contador += 1
    resposta = input ("deseja parar o contador? s/m: ")
    if resposta =="n": 
        sair = False
    else:
        sair = True

        print("final da contagem")