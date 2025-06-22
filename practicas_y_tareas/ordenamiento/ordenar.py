vector = [1,5,8,2,3,6,9]

for i in range(0,len(vector)):
    minimo = i
    for j in range(i+1,len(vector)):
        if vector[minimo] > vector[j]:
            minimo = j

    temp = vector[i]
    vector[i] = vector[minimo]
    vector[minimo] = temp

print(vector)