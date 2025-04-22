
velociodad= (float) (input("digite la velocida den corrocion en mpy: "))


cpy=velociodad*25/10000

if velociodad<5:
    grado_corrosion="MODERADO" 

if velociodad>5 and velociodad<10:
    grado_corrosion="MEDIO"

if velociodad>=10:
    grado_corrosion="SEVERO"

print ("la velocidad de corrcoion de su material es de nivel:",grado_corrosion, 
"y el valor en cpy es:", cpy)

