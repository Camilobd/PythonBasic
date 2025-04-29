edad=(int)(input("Digite su edad"))
documento=(bool) (input("Digite si tiene el documento con ud(True/False):  "))
puesto=(int) (input("digite el puesto de votacion: "))
inavilidad= input("Ud tien alguna inavilidad(S/N): ")#usar una funcion aleatoria para comprobar


if edad>=18 and documento==True and puesto==3 and inavilidad=="N":
    print("Puede votar")
else:
    print("No cumple con los requisitos para votar")
