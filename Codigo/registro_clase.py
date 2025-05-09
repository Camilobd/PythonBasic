documento=""
nombre=""
oper=0

while oper!=3:
    print("1. registro de clase")
    print("2. Mostrar asistentes a clase")
    print("3. salir")
    oper=(int)(input("Seleccione la opcion: "))

    if oper==1:
        print("--------- REGISTRO ESTUDIANTES ----------")
        
        documento=input("Digite el documento para el registro")
        nombre=input("Digite el nombre para el registro: ")

    if oper==2:
        print("--------- MOSTRAR ESTUDIANTES ----------")
        print ("Estudiante - Nro Documento:", documento," Nombre: ", nombre)

    if oper >3:
        print("ESTA OPCION NO ESTA DISPONIBLE")


print("fin de la ejecucion")