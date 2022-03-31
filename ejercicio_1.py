#Ejercicio 1 - Lucas Lopez
print("Ingrese las materias cursadas durante el año escolar\n")
materias = [] 
materias.append (input("Primer materia cursada: \n"))
materias.append(input("Segunda materia cursada: \n"))
materias.append(input("Tercer materia cursada: \n"))
materias.append(input("Cuarta materia cursada: \n"))
materias.append(input("Quinta materia cursada: \n"))
materias.append(input("Sexta materia cursada: \n"))
vida = 6
while vida != 0:

    vida -= 1
    print (materias)
    datos = input ("¿Los datos son correctos?: ")
    if datos == "no":
        materias.remove(input("Ingrese el nombre de la materia que desea remover: \n"))
        materias.insert(5,input("Ingrese el nombre de la materia que desea agregar: \n"))
    else:
        print ("Gracias, a continuacion debe ingresar las notas de los 3 parciales correspondientes a dichas materias \n")
        break
materia1=materias[0]
materia2=materias[1]
materia3=materias[2]
materia4=materias[3]
materia5=materias[4]
materia6=materias[5]
print(f"\n Coloque las notas de cada parcial de {materia1} \n")
nota1_materia1=float(input("Nota del primer parcial: \n"))
nota2_materia1=float(input("Nota del segundo parcial: \n"))
nota3_materia1=float(input("Nota del tercer parcial: \n"))
suma_materia1=nota1_materia1+nota2_materia1+nota3_materia1
promedio_materia1=suma_materia1/3
print (f"Su promedio de {materia1} es de {promedio_materia1} \n")
if promedio_materia1>=8:
    print ("Felicitaciones, materia PROMOCIONADA!!!")
elif nota1_materia1>=6 and nota1_materia1<8:
    print(f"Materia Aprobada, debe rendir final de {materia1}")
elif nota2_materia1>=6 and nota2_materia1<8:
    print(f"Materia Aprobada, debe rendir final de {materia1}")
elif nota3_materia1>=6 and nota3_materia1<8:
    print(f"Materia Aprobada, debe rendir final de {materia1}")
else:
    print(f"Materia de {materia1} Desaprobada!!")
print(f"\n Coloque las notas de cada parcial de {materia2} \n")
nota1_materia2=float(input("Nota del primer parcial: \n"))
nota2_materia2=float(input("Nota del segundo parcial: \n"))
nota3_materia2=float(input("Nota del tercer parcial: \n"))
suma_materia2=nota1_materia2+nota2_materia2+nota3_materia2
promedio_materia2=suma_materia2/3
print (f"Su promedio de {materia2} es de {promedio_materia2}\n")
if promedio_materia2>=8:
    print ("Felicitaciones, materia PROMOCIONADA!!!")
elif nota1_materia2>=6 and nota1_materia2<8:
    print(f"Materia Aprobada, debe rendir final de {materia2}")
elif nota2_materia2>=6 and nota2_materia2<8:
    print(f"Materia Aprobada, debe rendir final de {materia2}")
elif nota3_materia2>=6 and nota3_materia2<8:
    print(f"Materia Aprobada, debe rendir final de {materia2}")
else:
    print(f"Materia de {materia2} Desaprobada!!")
print(f"\n Coloque las notas de cada parcial de {materia3} \n")
nota1_materia3=float(input("Nota del primer parcial: \n"))
nota2_materia3=float(input("Nota del segundo parcial: \n"))
nota3_materia3=float(input("Nota del tercer parcial: \n"))
suma_materia3=nota1_materia3+nota2_materia3+nota3_materia3
promedio_materia3=suma_materia3/3
print (f"Su promedio de {materia3} es de {promedio_materia3}\n")
if promedio_materia3>=8:
    print ("Felicitaciones, materia PROMOCIONADA!!!")
elif nota1_materia3>=6 and nota1_materia3<8:
    print(f"Materia Aprobada, debe rendir final de {materia3}")
elif nota2_materia3>=6 and nota2_materia3<8:
    print(f"Materia Aprobada, debe rendir final de {materia3}")
elif nota3_materia3>=6 and nota3_materia3<8:
    print(f"Materia Aprobada, debe rendir final de {materia3}")
else:
    print(f"Materia de {materia3} Desaprobada!!")
print(f"\n Coloque las notas de cada parcial de {materia4} \n")
nota1_materia4=float(input("Nota del primer parcial: \n"))
nota2_materia4=float(input("Nota del segundo parcial: \n"))
nota3_materia4=float(input("Nota del tercer parcial: \n"))
suma_materia4=nota1_materia4+nota2_materia4+nota3_materia4
promedio_materia4=suma_materia4/3
print (f"Su promedio de {materia4} es de {promedio_materia4}\n")
if promedio_materia4>=8:
    print ("Felicitaciones, materia PROMOCIONADA!!!")
elif nota1_materia4>=6 and nota1_materia4<8:
    print(f"Materia Aprobada, debe rendir final de {materia4}")
elif nota2_materia4>=6 and nota2_materia4<8:
    print(f"Materia Aprobada, debe rendir final de {materia4}")
elif nota3_materia4>=6 and nota3_materia4<8:
    print(f"Materia Aprobada, debe rendir final de {materia4}")
else:
    print(f"Materia de {materia4} Desaprobada!!")
print(f"\n Coloque las notas de cada parcial de {materia5} \n")
nota1_materia5=float(input("Nota del primer parcial: \n"))
nota2_materia5=float(input("Nota del segundo parcial: \n"))
nota3_materia5=float(input("Nota del tercer parcial: \n"))
suma_materia5=nota1_materia5+nota2_materia5+nota3_materia5
promedio_materia5=suma_materia5/3
print (f"Su promedio de {materia5} es de {promedio_materia5}\n")
if promedio_materia5>=8:
    print ("Felicitaciones, materia PROMOCIONADA!!!")
elif nota1_materia5>=6 and nota1_materia5<8:
    print(f"Materia Aprobada, debe rendir final de {materia5}")
elif nota2_materia5>=6 and nota2_materia5<8:
    print(f"Materia Aprobada, debe rendir final de {materia5}")
elif nota3_materia5>=6 and nota3_materia5<8:
    print(f"Materia Aprobada, debe rendir final de {materia5}")
else:
    print(f"Materia de {materia2} Desaprobada!!")
print(f"\n Coloque las notas de cada parcial de {materia6} \n")
nota1_materia6=float(input("Nota del primer parcial: \n"))
nota2_materia6=float(input("Nota del segundo parcial: \n"))
nota3_materia6=float(input("Nota del tercer parcial: \n"))
suma_materia6=nota1_materia6+nota2_materia6+nota3_materia6
promedio_materia6=suma_materia6/3
print (f"Su promedio de {materia6} es de {promedio_materia6}\n")
if promedio_materia6>=8:
    print ("Felicitaciones, materia PROMOCIONADA!!!")
elif nota1_materia6>=6 and nota1_materia6<8:
    print(f"Materia Aprobada, debe rendir final de {materia6}")
elif nota2_materia6>=6 and nota2_materia6<8:
    print(f"Materia Aprobada, debe rendir final de {materia6}")
elif nota3_materia6>=6 and nota3_materia6<8:
    print(f"Materia Aprobada, debe rendir final de {materia6}")
else:
    print(f"Materia de {materia6} Desaprobada!!")
print ("FIN")