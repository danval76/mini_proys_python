#Ejemplo de remover un elemento de una lista en Python

# Lista inicial
# Creamos una lista con elementos repetidos
colores = ["rojo", "verde", "azul", "rojo"] 
print(f"Inicio: {colores}") # Salida: ['rojo', 'verde', 'azul', 'rojo']

# Eliminar el valor "rojo"
colores.remove("rojo")

print(f"Después de remove(): {colores}") # Salida: ['verde', 'azul', 'rojo']
# Solo eliminó la primera ocurrencia de "rojo".