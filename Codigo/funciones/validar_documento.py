lista_cc=["1051","1052","1053","1054","1055","1056","1057"]
lista_Cervezas=["0","0","0","0","0","0","0"]

def ced_correcta(lista_cc, cedula):
    valido=True
    for i in range(len(lista_cc)):
        print (lista_cc[i]," - ",cedula)
        
        if cedula==lista_cc[i]:
            print("---------------------")
            valido=True
        else:
            valido=False
    return valido


def menu():
    print("1. seguir tomando")
    print("2. ir para la casa")
    opc=(int)(input("Que quieren hacer: "))
    return opc


def retorno_indice(cc,lista):
    for i in range(len(lista)):
        if lista[i]==cc:
            return i


def listado_tomar():
    print ("ud se han tomado")
    for i in range(len(lista_cc)):
        print (lista_cc[i]," - ",lista_Cervezas[i])


opc=0
while opc!=2:
    opc=menu()
    listado_tomar()

    

    
