from random import randint
import random

numero_notas= (int) (input("cuantas notas desea sacar"))
cont=1
porcentaje_total=0
prom_est_1=0;
nota_total_est_1=0

while cont<=numero_notas:       
    
    if cont==numero_notas:
        porcentaje=100-porcentaje_total       
    else:
        porcentaje= randint(1,40)        
        
    porcentaje_total=porcentaje_total+porcentaje
    print("la nota ",cont," ca tener el siguiente porcentaje ",porcentaje)
    cont1=0
    while cont1<=10:
        nota= random.uniform(0.0,5.0)
        prom_est_1=nota*(porcentaje/100)
        nota_total_est_1=nota_total_est_1+prom_est_1
        
        print ("el estudiante ",cont1, "saco: ",nota,"/",prom_est_1)
        cont1=cont1+1
   
    cont=cont+1



print ("procnetaje total: ", porcentaje_total)

print ("NOTAS TOTALES")
print("Estudiante 1:", nota_total_est_1)



