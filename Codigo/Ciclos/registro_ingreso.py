from datetime import datetime


print("registro ingreso a INCITEMA")

oper=0

while oper!="3":
    print("1.Registrar datos del ingreso")
    print("2. mostrar cuantas personas han ingresado")
    print("3. Salir")

    oper= input("Digite la opcion que desea ejecutar: ")

    if oper=="1":
        
        nombre= input("Digite su nombre: ")
        cedula= input("Digite su cedula: ")
        eps= input("Digite El nombre de la  eps: ")    
        fecha= datetime.now()
               

        print(nombre,"ingreso :", fecha)
        print("1. Lab de Materiales")
        print("2. Lab de fluidos")
        print("3. Area Administrativa")
        lugar= input("Digite el lugar al que desea ingresar: ")
    
        if lugar=="1":
            print("Ingreso a Lab de Materiales")
        elif   lugar=="2":
            print("ingrese a lab de Fluidos")

