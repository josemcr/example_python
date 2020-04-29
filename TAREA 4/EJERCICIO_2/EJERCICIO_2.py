
while 1:
    divisores = []
    num = int(input("Introduzca el numero: "))
    if num < 0:
        print("El numero debe ser mayor a cero !")
    else:
        for n in range(1, num // 2 + 1):
            if num % n == 0:
                divisores.append(n)
        print(f"Los divisores de {num} son ", end=""); print(divisores)

