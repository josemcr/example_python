while 1:
    print("***FACTORIAL***")
    print("")
    num = int(input("Introduzca el numero : "))
    def factorial(num):
        fact = 1
        for n in range(1, num + 1):
            fact = fact * n
        print(f"El factorial de {num} es: ", end=""); print(fact)

    if num < 0:
        print("El numero no puede ser negativo!")
    elif num == 0:
        print(f"El factorial de {num} es: ", end=""); print(0)
    elif num > 0:
        factorial(num)
    print("")        
    