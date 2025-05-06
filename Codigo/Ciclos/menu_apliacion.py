
import math


print("MI PRIMERA APLICACION")

oper=0
while oper!=3:
    print("-----",oper)
    print("1. Tablas de multiplicar")
    print("2. Area del circulo")
    print("3. Salir")
    oper=(int)(input("Digite la opcion deseada:"))
    
    if oper==1:
        print("Tabla de multiplciar")
        numero_tablas=(int) (input("cuantas tablas desea generar"))

        for i in range (1,numero_tablas+1):
            for j in range (1,11):
                print(i,"x",j, " = ",(i*j))

    if oper==2:
        print("Area del circulo")
        #pi *r 2
        radio=(float) (input("Digite el radio del circulo (m):"))
        area=math.pi * (radio**2)

        print("El area del circulo es: ",area," m2" ) 


    
    


print("Fin de la aplicacion")