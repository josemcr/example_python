
while 1:
    num_user = int(input("INGRESE EL NUMERO: "))
    if num_user < 0:
        print("SU NUMERO ES NEGATIVO")
        break 
    else:
        cuadrado = num_user**2
        print("EL CUADRADO DE SU NUMERO ES: "); print(cuadrado)    