#ejemplo Pop
# Muestra cómo usar el método .pop() en listas de Python


# Lista inicial
peliculas = ["Peli A", "Peli B", "Peli C", "Peli D"]
print(f"Inicio: {peliculas}") # Salida: ['Peli A', 'Peli B', 'Peli C', 'Peli D']

# 1. Usar .pop() sin argumento: elimina y devuelve el ÚLTIMO
ultima_vista = peliculas.pop() 

print(f"Eliminada con pop() sin índice: {ultima_vista}") # Salida: Peli D
print(f"Lista restante: {peliculas}") # Salida: ['Peli A', 'Peli B', 'Peli C']

# 2. Usar .pop() con índice: elimina y devuelve el elemento en ese índice
rescatada = peliculas.pop(0) 

print(f"Eliminada con pop(0): {rescatada}") # Salida: Peli A
print(f"Lista restante: {peliculas}") # Salida: ['Peli B', 'Peli C']