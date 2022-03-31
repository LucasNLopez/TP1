print ("A continuacion deberá ingresar los nombres de sus amigos.\nPara dejar de ingresarlos, debera escribir la palabra 'Exit'.\n")
nombres=[]
vida = 0
nombres.append (input("Ingrese el Primer Nombre:\n"))
while vida >=0:
    vida += 1
    respuesta=input("¿Desea ingresar otro nombre?: \n")
    if respuesta == "si":
        nombres.append (input("Ingrese un Nombre:\n"))
    elif respuesta == "Exit":
        print(*nombres, sep="-")
        break
    else:
        print("   ERROR   !\n Para salir del programa debe ingresar la palabra !! Exit !!\n")
    