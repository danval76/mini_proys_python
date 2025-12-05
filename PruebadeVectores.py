#Prueba de Vectores

vector = [1, 2, 3, 4, 5, "juan"]

for i in range(6):
    print("El vector es:", vector[i])
# Imprime los elementos del vector


print(vector[0])  # Imprime el primer elemento del vector
print(vector[1])  # Imprime el segundo elemento del vector  
print(vector[2])  # Imprime el tercer elemento del vector
print(vector[3])  # Imprime el cuarto elemento del vector
print(vector[4])  # Imprime el quinto elemento del vector
print(vector[5])  # Imprime el sexto elemento del vector    

vector = [0] * 6  # Crea un vector de tamaño 6 inicializado con ceros
for i in range(5):
    dato = int(input(f"Ingrese Dato No {i+1}: "))
    vector[i]= dato  # Almacena el dato en la posición i del vector
    #vector.append(dato)

print("Vector actualizado:", vector)  # Muestra el vector actualizado






