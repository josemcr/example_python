cont1 = 0
cont2 = 0
cont3 = 0
positive = 0
negative = 0

for i in range(1,11):
    numero = int(input("INGRESE EL NUMERO " + str(i) + " DE 10: "))
    if numero > 0:
        positive = positive + numero
        cont1 += 1    
    elif numero < 0:
        negative = negative + numero
        cont2 += 1
    else:
        cont3 += 1

prom_positive = positive / cont1
prom_negative = negative / cont2
cant_cero = cont3
print(" ")
print("PROMEDIO DE NUMEROS POSITIVOS: ");print(prom_positive)
print("PROMEDIO DE NUMEROS NEGATIVOS: ");print(prom_negative)
print("CANTIDAD DE CEROS: ");print(cant_cero)