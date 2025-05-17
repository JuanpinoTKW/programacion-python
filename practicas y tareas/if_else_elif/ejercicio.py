'''
Para ingresar al concierto de la Banda “Pop Estelar” , se requiere tener al menos 10 años de edad 
y medir más de 1,40 metros. El programa debe permitir ingresar la edad y la estatura de y determinar 
si pueden ingresar o no a la atracción.
'''
edad = int(input("ingrese su edad: "))
estatura = float(input("ingrese su estatura: "))
if edad <= 10 or estatura < 1.40:
    print(f"usted no puede entrar al concierto")
else:
    print(f"bienvenido al concierto de pop estelar!")
