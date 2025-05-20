#lista de datos
producto=["1. QUESO","1. LECHE","1. HUEVO","1. YOGURT",
          "2. CARNE","2. POLLO", "2. PESCADO", "2. JAMON",
          "3. MANZANA", "3. NARANJA","3. PERA","3. PLATANO"]

precio_prodcuto=[15000,5500,15000,15000,16000, 13500,7000,23000,2500,400,2200,200]

#Definicion de la funcion
def mostrar_producto(lista_producto,tipo_producto):
    subproductos=[]
    for i in range (len(lista_producto)):
        if tipo_producto in lista_producto[i]:
            if tipo_producto=="1.":
                subproductos.append(lista_producto[i].replace(tipo_producto,"BASICO - "))
            if tipo_producto=="2.":
                subproductos.append(lista_producto[i].replace(tipo_producto,"PROTEINA - "))
            if tipo_producto=="3.":
                subproductos.append(lista_producto[i].replace(tipo_producto,"FRUTAS - "))
    return subproductos    

def descuentos(lista_productos,descuento,orden):
    for i in range (len(lista_productos)):
        precio=precio_prodcuto[i+orden]
        valor_con_descuento=(100-descuento)*precio/100        
        print("Producto: ",lista_productos[i]," Valor: ",precio,
              "valor con descuento: ",valor_con_descuento)

#llamado de la funcion
#print (mostrar_producto(producto,"1."))

def menu():
    print("1. Calcular descuentos")
    print ("2. salir")

def menu_productos():
    print("-------TIPO DE PRODUCTOS-----")
    print("1. BASICO")
    print("2. PROTEINA")
    print("3. FRUTAS")

opc=0
opc_producto=0
porcentaje=0
while opc!=2:
    menu()
    opc= (int)(input("seleccione la opcion:"))
    if opc==1:
        menu_productos()
        opc_producto= (int)(input("seleccione la opcion:"))
        porcentaje= (int)(input("Digite el procentaje del calculo:"))
        if opc_producto==1:
            descuentos(mostrar_producto(producto,"1."),porcentaje,0)
        if opc_producto==2:
            descuentos(mostrar_producto(producto,"2."),porcentaje,4)
        if opc_producto==3:
            descuentos(mostrar_producto(producto,"3."),porcentaje,8)


