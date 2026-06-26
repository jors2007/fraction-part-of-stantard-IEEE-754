
__author__ = "Jordy Andrade (https://github.com/jors2007)"
__version__ = "1.0"

# parte fraccionaria
fraccion = float(input("Ingresa la parte fraccionaria de tu numero: "))
operacion = 0
i = 0
cadenaBinaria = ""
while(i < 24):
    operacion = fraccion * 2
    operacion = round(operacion, 10) 
    if i < 23:
        print(f"{fraccion} x 2 = {operacion}")
    if (operacion >= 1):
        cadenaBinaria += "1"
        fraccion = round(operacion-1,10)
    else:
        cadenaBinaria += "0"
        fraccion = operacion

    i += 1    
bits_23 = cadenaBinaria[:23]
bits_24 = cadenaBinaria[23]

# esta parte del codigo se encarga de redondear el numero binario
# suponga que tiene como 5 ultimos bits 10111 y el 24 bit es 1
# entonces para redonder a 23 bits quedaria 11000 porque ese 1 se reparte para la izquierda
if (bits_24 == "1"):
    redondeado = bin(int(bits_23,2) + 1)[2:]
    bits_23 = redondeado.zfill(23)

print(bits_23)