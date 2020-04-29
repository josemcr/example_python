import FUNCIONES
import time
import os
while 1: 
    os.system ("cls") 
    print(" ")  
    print(" ****CALCULADORA****")
    print(" ")
    print("QUE OPERACION DESEA REALIZAR ?")
    print(" ")
    print("1 - Sumar dos numeros")
    print(" ")
    print("2 - Restar dos numeros")
    print(" ")
    print("3 - Multiplicar dos numeros")
    print(" ")
    print("4 - Dividir dos numeros")
    print(" ")
    print("5 - Salir")
    print(" ")
    op =  int(input("Ingrese el numero de la operacion: "))
    print(" ")

    if op == 1:
        num1 = int(input("Ingrese el primer digito: "))
        num2 = int(input("Ingrese el segundo digito: "))
        FUNCIONES.suma(num1, num2)
        print("")
        print("Volviendo al menu en 7 segundos !")
        time.sleep(7)
    elif op == 2:
        num1 = int(input("Ingrese el primer digito: "))
        num2 = int(input("Ingrese el segundo digito: "))
        FUNCIONES.resta(num1, num2)
        print("")
        print("Volviendo al menu en 7 segundos !")
        time.sleep(7)
    elif op == 3:
        num1 = int(input("Ingrese el primer digito: "))
        num2 = int(input("Ingrese el segundo digito: "))
        FUNCIONES.mult(num1, num2)
        print("")
        print("Volviendo al menu en 7 segundos !")
        time.sleep(7)
    elif op == 4:
        num1 = int(input("Ingrese el primer digito: "))
        num2 = int(input("Ingrese el segundo digito: "))
        FUNCIONES.divi(num1, num2) 
        print("")
        print("Volviendo al menu en 7 segundos !")
        time.sleep(7)       
    elif op == 5:
        break;    