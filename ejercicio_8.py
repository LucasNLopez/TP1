import re
from turtle import clear
def validar_contraseña(contraseña):
    if 8 <= len(contraseña) <= 16:
        if re.search("[a-z]", contraseña) and re.search("[A-Z]", contraseña):
            if re.search("[$@#&]", contraseña):
                if  re.search("[1-9]", contraseña):
                    return True
    return False
    

print("""
Bienvenido, a continuacion debera ingresar sus datos correctamente:

""")
print("""
NOMBRE Y APELLIDO
""")
nombre=input("Ingrese su nombre: \n")
apellido= input ("Ingrese su apellido: \n")
if re.search("[aeiou]",nombre) and re.search("[aeiou]",apellido):
    print (input("Nombre ingresado correctamente\n Pulse enter para continuar..."))
else:
    print ("Nombre erroneo")
print ("""
AÑO DE NACIMIENTO
""")
nacimiento=input("Ingrese su fecha de nacimiento: \n ")
while len (nacimiento) >0:
    if len (nacimiento) !=4:
        print("Formato de año de nacimiento erroneo\n")
        nacimiento=input("Ingrese Nuevamente su año de nacimiento: \n")
    else:
        print(" Año de nacimiento correcto\n")
        input("Pulse enter para continuar...")
    break
print("""
CONTRASEÑA
""")
password=input ("Ingrese la contraseña: \n")
if  validar_contraseña(password) == False:
    print (input("Ingrese nuevamente la contraseña\n Pulsa enter para continuar..."))
else:
    print(f"Hola {nombre} {apellido}, Bienvenido")

    print("Nos Vemos")