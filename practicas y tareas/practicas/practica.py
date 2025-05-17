"""
palabra = input("ingrese la palabra ")
palabra_mayusculas = palabra.upper() 
if (palabra_mayusculas == "DANIEL"):
    print(palabra)
"""
producto = int(input("ingrese el precio: "))
cliente = input("que tipo de cliente es, premium/regular/nuevo? ")
if cliente == "premium":
    precio = producto - (producto*20/100)
    print("el precio es: ",precio)
    if cliente == "regular":
        precio >= producto - (producto*10/100)
        print("el precio del producto es: ",producto)
        
    

    


