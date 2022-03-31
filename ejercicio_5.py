#Ejercicio 5 - Lucas Lopez
mayor = 0
maximo = 3
 
for i in range(maximo):
    num = float(input('Ingrese un numero:'))
    if num >= mayor:
        mayor = num
 
print(f"el numero mayor es: {mayor}")