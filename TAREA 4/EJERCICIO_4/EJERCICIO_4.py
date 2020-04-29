
while 1:
    print("***CALCULAR JORNAR DIARIO***")
    print("")

    turno = input("Introduzca turno trabajo el empleado: ")
    dia = input("Introduzca dia de la semana trabajado por el empleado: ")
    horas = int(input("Introduzca Horas Trabajadas: "))

    def diurno_semana(horas):
        jornal_dia = 0
        jornal_dia = 5 * horas
        print("El jornal diario Diurno/Semana es: ", end=""), print(jornal_dia)

    def diurno_domingo(horas):
        jornal_dia_sun = 0
        jornal_dia_sun = (5 + 2) * horas
        print("El jornal diario Diurno/Domingo es: ", end=""), print(jornal_dia_sun)

    def nocturno_semana(horas):
        jornal_noct = 0
        jornal_noct = 8 * horas
        print("El jornal diario Nocturno/Semana es: ", end=""), print(jornal_noct)

    def nocturno_domingo(horas):
        jornal_noct_sun = 0
        jornal_noct_sun = (8 + 3) * horas
        print("El jornal diario Nocturno/Domingo es: ", end=""), print(jornal_noct_sun)


    if (turno.lower() == "diurno" and dia.lower() != "domingo"):
        diurno_semana(horas)
    elif (turno.lower() == "diurno" and dia.lower() == "domingo"):
        diurno_domingo(horas)
    elif (turno.lower() == "nocturno" and dia.lower() != "domingo"):
        nocturno_semana(horas)
       
    elif (turno.lower() == "nocturno" and dia.lower() == "domingo"):
        nocturno_domingo(horas)
        
    print(" ")