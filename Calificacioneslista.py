cantidad = input("¿Cuantas calificaciones quieres ingresar): ")
lista=[]
elementos = 0
suma=0
nombre = input("Dame tu nombre: ")
lista.append[nombre]
while elementos < cantidad:
    cal = float(input("Dame la calificacion: "))
    lista.append[cal]
    elementos = elementos + 1
    suma = suma + cal

promedio = suma/cantidad

print("EL alumno ", lista[0], " tuvo un promedio de ", promedio)

    