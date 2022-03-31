#Ejercicio 9 - Lucas Lopez
suma = 1
resta = 2
multiplicacion = 3
division = 4
potencia = 5
print (f"""
{suma})SUMA
{resta})RESTA
{multiplicacion})MULTIPLICACION
{division})DIVISION
{potencia})POTENCIA     """)
opcion= int (input("Selecciona una opcion: \n"))
if suma <= opcion <= potencia:
    num1 = float (input("Seleccione el primer numero: \n"))
    num2 = float (input("Seleccione el segundo numero: \n"))
    if opcion == suma:
        print (f"{num1}+{num2} = {num1+num2}")
    elif opcion == resta:
        print(f"{num1} - {num2} = {num1-num2}")
    elif opcion == multiplicacion:
        print (f"{num1}*{num2} = {num1*num2}")
    elif opcion == division:
        print (f"{num1} / {num2} = {num1/num2}")
    else:
        print (f"{num1}**{num2} = {num1**num2}")
    
else:
    print ("Opcion Incorrecta.")
input("Nos Vemos...")