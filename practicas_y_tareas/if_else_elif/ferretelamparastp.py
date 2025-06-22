cantidad = int(input("ingrese la cantidad de lámparas "))
marca = input("ingrese la marca de las lámparas, (argenluz o felipe lamparas) ")
if cantidad >= 6:
    descuento = 60
elif cantidad == 5 and marca == "argenluz":
    descuento = 40
elif cantidad == 5 and marca != "argenluz":
    descuento = 30
elif cantidad == 4 and marca == "argenluz" or marca == "felipe lamparas":
    descuento = 25
elif cantidad == 4 and marca != "argenluz" and  marca != "felipe lamparas":
    descuento = 20
elif cantidad == 3 and marca == "argenluz":
    descuento = 15
elif cantidad == 3 and marca == "felipe lamparas":
    descuento = 10
elif cantidad == 3 and marca != "argenluz" and marca != "felipe lamparas":
    descuento = 5
importe_total = cantidad * 800
importe_descuento = importe_total * descuento / 100
importe_con_descuento = importe_total - importe_descuento
if importe_con_descuento > 4000:
    descuento_adicional = 5
    importe_descuento_adicional = importe_con_descuento * descuento_adicional / 100
    importe_final = importe_con_descuento - importe_descuento_adicional
else:
    importe_final = importe_con_descuento 
print(f"la marca es: {marca}, la cantidad de lamparas: {cantidad}, total a pagar sin descuento: {importe_total}, el importe del descuento: {importe_descuento} y el total a pagar con descuento es: {importe_final}")