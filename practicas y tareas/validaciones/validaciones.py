def validar_texto(mensaje:str)->str:
    texto = input(mensaje)
    while texto.strip()  == "" or len(texto.strip()) <= 2:
        print("el texto no puede tener espacios vacios o ser menor a 2 caracteres. intente otra vez")
        texto = input(mensaje)
    return texto

def validar_entero(mensaje:str)->int:
    num = input(mensaje)
    while num.isnumeric() == False: # or int(num) < 0:
        print("el numero ingresado no es valido, intente nuevamente")
        num = input(mensaje)
    return int(num)

def validar_entero_pos(mensaje:str)->int:
    num = input(mensaje)
    while num.isnumeric() == False or int(num) < 0:
        print("el numero ingresado no es valido, intente nuevamente")
        num = input(mensaje)
    return int(num)

def validar_acceso(usuario_correcto:str,clave_correcta:int,intentos_max:int)->str:
    while intentos_max > 0:
        usuario = validar_texto("ingrese su usuario: ")
        clave = validar_entero("ingrese su clave: ")
        if usuario == usuario_correcto and clave == clave_correcta:
            return "concedido"
        else:
            intentos_max -= 1
            print(f"usuario y/o clave incorrecta, ingrese nuevamente. tiene {intentos_max} intentos")
    return "denegado"

def validar_sino(mensaje:str)->str:
    texto = input(mensaje)
    while texto.upper() != "S" and texto.upper() != "N":
        print("invalido, debe ingresar 'S' o 'N'")
        texto = input(mensaje)
    return texto

def validar_genero(mensaje:str)->str:
    texto = input(mensaje)
    while texto.upper() != "M" and texto.upper() != "F" and texto.upper() != "X":
        print("invalido, debe ingresar 'M/F/X'")
        texto = input(mensaje)
    return texto
