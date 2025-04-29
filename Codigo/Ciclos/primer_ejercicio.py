from random import randint


print("INICIO DE LA EJECUCION")
numero=1
cont=0

while numero<10000000:
    aleatorio= randint(10,1000)
    cont= cont+1
    numero=numero+aleatorio
    
    if (cont%3000==0):
        print ("en la ejecucion",cont,
                "El nuermo que se ha generado va en ",numero )

    ##numero_veces=randint(1,1000000)
    

print (numero,". ME ESTOY EJECUTANDO")
print ("se hicieron",cont, " numero de ejecuciones" )
print("FIN DE LA EJECUCION")