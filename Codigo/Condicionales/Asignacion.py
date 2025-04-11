print("\n___________________________________")

print("1. Opcion nueva")
print("2. opcion vieja")

print("___________________________________")
condicion = (int)(input("selecione una opcion digitando el nuemro:"))

if condicion==1:
    #todo lo que este aca se ejecutara si la opcion es true
    print("opcion nueva")
    print ("lo logre entro al if")
else:    
    if condicion==2:
        print("Ocion vieja")
    else:
        print ("Condicion Incorrecta")


print("termine la ejecucion")