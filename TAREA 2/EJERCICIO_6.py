cont1 = 0
cont2 = 0

for i in range(1,7):
    nota_user = int(input("INGRESE NOTA " + str(i) + ": "))
    if nota_user > 1:
        cont1 += 1    
    elif nota_user == 1:
        cont2 += 1

print("CANTIDAD DE ALUMNOS APROBADOS: ", end=str(cont1))
print(" ")
print("CANTIDAD DE ALUMNOS REPROBADOS: ", end=str(cont2))   