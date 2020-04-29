import time
import os
lis_asig = []
cont = 0

while 1:
    os.system ("cls")
    print("***Asignaturas Primer Curso***")
    print(" ")
    
    print("1 - Agregar Asignatura")
    print("2 - Remover Asignatura")
    print("3 - Listar Asignatura ")
    op = int(input("Que operacion desea realizar: "))

    if op == 1:
        print(" ")
        agree = input("Escriba la asignatura que desea agregar: ")
        lis_asig.append(agree)
        print(" ")
        print("Se a agregado exitosamente!")
        time.sleep(4)
    elif op == 2:
        print(" ")
        dele = input("Escriba la asignatura que desea eliminar: ")    
        lis_asig.remove(dele)
        print(" ")
        print("Se a eliminado exitosamente!")
        time.sleep(4)
    elif op == 3:
        print(" ")
        cont = len(lis_asig)
        for i in range(0,cont): 
            print("Asignatura: ",end="");print(lis_asig[i])
        print(" ")
        print("En 10 segundo vuelve al menu!")    
        time.sleep(10)     