
edad = int(input("ingrese su edad "))
examen_vista = input("aprobo el examen de vista?? si/no: ")

if edad < 20 or examen_vista == "no":
    print("no puede manejar colectivos")
else:
    print("puede manejar colectivos")

