#documento="" esto es una variable
from random import randint

nombre_bd=["Camilo", "Juan", "Pedro", "Luis", "Andres", "Alejandra","Marcela","Michael","Yulieth","Felipe"]
documento=[]# Arreglo de datos 
nombre=[]

oper=0

while oper!=5:
    print("1. registro de clase")
    print("2. Mostrar asistentes a clase")
    print("3. Borrar registro")
    print("4. BUscar registro")
    print("5. salir")
    
    oper=(int)(input("Seleccione la opcion: "))


    if oper==1:
        print("--------- REGISTRO ESTUDIANTES ----------")
        
        #documento_registro=input("Digite el documento para el registro: ")
        
        #nombre_registro=input("Digite el nombre para el registro: ")

        for i in range(0,1000):
            documento_registro=randint(1000000,1200000)
            nombre_registro=nombre_bd[randint(0,(len(nombre_bd)-1))]

            documento.append(documento_registro)
            nombre.append(nombre_registro)
       


    if oper==2:
        print("--------- MOSTRAR ESTUDIANTES ----------")

        for i in range(len(documento)):
            print ("Estudiante Nro: ", i, " - Nro Documento:", 
                   documento[i]," Nombre: ", nombre[i])

    if oper==3:
        print ("-----------BORRAR REGISTRO ESTUDIANTES -----------")
        
        for i in range(len(documento)):
            print ("Estudiante Nro: ", i, " - Nro Documento:", 
                   documento[i]," Nombre: ", nombre[i])
        
        pos=(int)(input("Digite el Nro de Estudiante a borrar:"))
        documento.pop(pos)
        nombre.pop(pos)

    if oper==4:
        print ("---------------- BUSCAR REGISTROS-------------")
        docu=(int)(input("Digite el documento a buscar: "))
        estado=False
        for i in range(len(documento)):
            if docu==documento[i]:
                print("el nombre del estudiante que esta buscando es:",nombre[i])
                estado=True
            #else:
                #print("el estudiante no se encuentra en la lista")
        if estado==False:
            print("el estudiante no se encuentra en la lista")

    if oper >5:
        print("ESTA OPCION NO ESTA DISPONIBLE")


print("fin de la ejecucion")