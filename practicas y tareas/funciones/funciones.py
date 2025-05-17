def es_primo(num:int)->bool:
    if num <= 1:
        return False
    for i in range(2,int(num**0.5) +1):
        if num % i == 0:
            return False
    return True

def imprimir_tabla(num:int,inicio=1,fin=10)->None:
    for i in range(inicio,fin+1):
        print(f"{num} x {i} = {num*i}")    
