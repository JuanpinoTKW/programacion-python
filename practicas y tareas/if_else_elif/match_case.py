'''
x = 3
y = -5
if x + y >= 2:
    x = x + 1
else:
    x = y - 2
print(x)

x = -2
y = 3
if y ** (x+4) == 9:
    w = y + 1
else:
    w = x + 2
print(w)
'''
x = int(input("ingrese un numero: "))
match x:
    case 4:
        print("cuatro")
    case 1:
        print("uno")
    case 3:
        print("tres")
    case _:
        print("no es ninguna de las anteriores")
    


