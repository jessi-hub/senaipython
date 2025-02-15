tabuada =  2
contador =  1
resultado = 0

while tabuada <= 10:
    resultado = tabuada * contador
    print(tabuada," x ",contador," = ",resultado)
    contador += 1
    if contador == 11:
       tabuada+=1
       contador=1
    
while contador <= 11:
   resultado = tabuada * contador 
   print(f"(tabuada) * (contador) = (resultado)")
   contador += 1