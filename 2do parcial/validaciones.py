def validar_texto(mensaje:str)->str:
    texto = input(mensaje)
    while texto.strip()  == "":
        print("el texto no puede tener espacios vacíos.")
        texto = input(mensaje)
    return texto

def validar_jugadores(mensaje)->int:
    num_str = input(mensaje)
    while num_str.isnumeric() == False or int(num_str) < 1 or int(num_str) > 10:
        print("el numero ingresado no es valido, intente nuevamente")
        num_str = input(mensaje)
    num = int(num_str)
    return num
