'''
print("1. Acero al carbono")
print("2. Acero Inoxidable")
print("3. Aluminio")

#Medios
print("1. Oxigeno")
print("2. Cloruros")
print ("3. CO2")
'''

# 0 aq 50 baja
# 50 a 200 moderada
# 200 a 500 alta
# 500  severa

# coneficientes de eqyuilibrio para la correocion
# stabndarmethods



concentracion=(float)(input("Digite la concentracion en partes por muillon"))

if concentracion>=0 and concentracion<=50:
    print("Velocidad Baja")
elif concentracion>50 and concentracion<=200:
    print("Velocidad es moderada")
elif concentracion>200 and concentracion<=500:
    print("Velocidad es alta")
else:
    print("Velocidad es sevrea")








##aluminio cloruro
## Acero al corbaono cloruro





