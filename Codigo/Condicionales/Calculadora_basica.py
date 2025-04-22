print ("_________________________________________________________")
print("1. Suma")
print("2. Resta")
print("3. multiplicacion")
print("4. division")

operacion=(int)(input("\neleccion la operacion a realizar:  "))
print ("_________________________________________________________")

if operacion==1:
    print ("_________________________________________________________")
    print("SUMA")
    #definicion de varibles
    num1=(int)(input("digite el primer numero: "))
    num2=(int)(input("digite el segundo numero: "))
    # Operaciones
    resultado=num1+num2
    #salidas
    print(num1," + ",num2," = ",resultado)
    
elif operacion==2:
    print ("_________________________________________________________")
    print("RESTA")
    #definicion de varibles
    num1=(int)(input("digite el primer numero: "))
    num2=(int)(input("digite el segundo numero: "))
    # Operaciones
    resultado=num1-num2
    #salidas
    print(num1," - ",num2," = ",resultado)

elif operacion==3:
    print ("_________________________________________________________")
    print("MULTIPLICACION")

    #definicion de varibles
    num1=(float)(input("digite el primer numero: "))
    num2=(float)(input("digite el segundo numero: "))
    # Operaciones3
    resultado=num1*num2
    #salidas
    print(num1," x ",num2," = ",resultado)

elif operacion==4:
    print ("_________________________________________________________")
    print("DIVISION")
     #definicion de varibles
    dividendo=(float)(input("digite el dividendo: "))
    divisor=(float)(input("digite el divisor: "))

    if divisor!=0:    
        resultado=dividendo/divisor
    #salidas
        print(dividendo," / ",divisor," = ",resultado)
    else:
        print("LA DIVISION EN CERO NO ES POSIBLE")

else:
    print("opcion NO DEFINIDA")

print ("FIN DE LA EJECUCION")