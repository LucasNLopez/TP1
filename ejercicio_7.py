#Ejercicio 7 - Lucas Lopez
nombre= input("Ingrese su Nombre: \n")
apellido=input("Ingrese su Apellido \n")
edad= float (input ("Ingrese su Edad: \n"))
dinero= float(input("¿Cuanto dinero lleva en su billetera?: \n"))
hambre= float(input("Del 0 al 10, ¿cuanto hambre tiene en este momento?: \n"))
#si es menor a 35
#si es mayor a 34 y tiene $500 y su hambre es mayor a 5
#si su hambre es de 7 o mas, o tiene menos de $100 y su edad es menor a 18años
if edad>34 and dinero==500 and hambre>5:
    print (f"Hola {nombre} {apellido}, ¿Hoy hay asado?")
elif (hambre >=7 and dinero < 100 and edad < 18) or (dinero < 100 and edad <18):
    print (f"Hola {nombre} {apellido}, ¿ Vas a comer a lo de tus padres?")
elif edad<35:
    print (f"Hola {nombre}.\n Eres una persona joven ya que tu edad es {edad}")
else:
    print ("Error")