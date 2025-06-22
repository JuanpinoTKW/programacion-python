#1
edad = int (input("ingrese su edad: "))
if edad == 18: 
    print ("usted tiene 18 años")
#2
edad = int(input("ingrese su edad "))
if edad >= 18:
    print("mayor")
else:
    print("menor")
#3
altura = float(input("ingrese su altura "))
if altura >= 1.80:
    print("es pivot")
else:
    print("no es pivot")
#4
edad = int(input("ingrese su edad "))
if edad >= 13 and edad <= 17: 
    print("adolescente")
else:
    print("no es adolescente")
#5
edad = int(input("ingrese su edad "))
if edad < 10:
    print("es niño")
else:
    if edad >= 10 and edad <= 13:
        print("es pre-adolescente")
    else:
        if edad > 13 and edad <= 17:
            print("es adolescente")
        else:
            print("es mayor")
       

    



