

while 1:
    numero = int(input("INGRESE UN NUMERO ENTERO: "))

    div = 2

    while numero>div:
        if numero%div == 0:
            print("EL NUMERO NO ES PRIMO")
            break
        elif numero%div != 0:
            div += 1

    if numero == div:
        print("EL NUMERO ES PRIMO")
    elif numero < div:
        print("EL NUMERO NO ES PRIMO")    