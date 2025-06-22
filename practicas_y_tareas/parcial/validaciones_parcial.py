def validar_num_proyecto(mensaje:str)->int:
    num = int(input(mensaje))
    while num < 0 or num > 20:
        print("[*]el numero ingresado no es valido, intente nuevamente")
        num = int(input(mensaje))
    return num

def validar_resta_suma(mensaje:str)->str:
    resta_o_suma = input(mensaje)
    while resta_o_suma != "restar" and resta_o_suma != "sumar":
        print("[*]valor denegado, debe ingresar 'sumar' o 'restar'")
        resta_o_suma = input(mensaje)
    return resta_o_suma

def validar_dias(mensaje:str)->int:
    dia = int(input(mensaje))
    while dia <= 0:
        print("[*]el numero ingresado no es valido, intente nuevamente")
        dia = int(input(mensaje))
    return dia