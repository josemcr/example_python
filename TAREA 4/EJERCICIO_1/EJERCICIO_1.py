while 1:
    anio = int(input("Ingresa el Año: "))

    def anho_bisiesto(anio):
        if anio % 4 == 0:
            if anio % 100 == 0:
                if anio % 400 == 0:
                    print("El Año es bisiesto")
                else:
                    print("El Año no es bisiesto")
            else:
                print("El Año es bisiesto")
        else:
            print("El Año no es bisiesto")

    anho_bisiesto(anio)            
