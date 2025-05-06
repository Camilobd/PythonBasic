from random import randint

tam=5
cont=0
cont_total=0

for i in range(0,tam):
    for j in range (0,tam):             
        dato=randint(0,9)
        if dato>=2 and dato<=7:
            print(dato,end=" ")
            cont_total=cont_total+1
            if dato==1:
                cont=cont+1
        else:
            print("N",end=" ")

            

    print("") 

print("dentro de la matriz  hay ",cont," unos, de",cont_total,
      " elementos", 
      (cont/cont_total*100))
