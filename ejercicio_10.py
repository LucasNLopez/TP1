import random 
print ("""
Intente adivinar el numero del 1 al 10 !!
Contara con 5 intentos!
         !!MUCHA SUERTE!!
""")
aleatorio = random.randint (1,10)
vida=0
while vida <= 5:
    vida += 1
    if vida <=5:
        usuario = int(input("Ingrese un número: \n"))
        if usuario < aleatorio:
            print ("Estas muy cerca")
        elif usuario > aleatorio:
            print ("Estas muy cerca")
        else:
            print(F"FELICIDADES EL NUMERO ELEGIDO {usuario} ES EL CORRECTO!!!")
        input ("Enter para seguir intentando...")
print(input("\nHas perdido!!!!\n Presione enter para salir..."))