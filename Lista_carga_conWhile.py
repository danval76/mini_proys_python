# ...existing code...
def agregar_productos_a_lista():
    """
    Crea una lista de compras interactiva:
    - Pide productos al usuario hasta que escriba 'fin'.
    - Añade cada producto a una lista y muestra el total al final.
    """
    # 1. Lista vacía para almacenar los datos
    lista_productos = []

    # Mensajes iniciales para el usuario
    print("--- Creador de Lista de Compras ---")
    print("Ingresa los productos uno por uno. Escribe 'fin' para terminar.")
    
    # 2. Ciclo infinito para la interacción: se rompe cuando el usuario escribe 'fin'
    while True:
        # 3. Pedir la entrada del usuario
        nuevo_producto = input("Producto a añadir: ")
        
        # 4. Condicional para salir del ciclo: compara en minúsculas para mayor robustez
        if nuevo_producto.lower() == 'fin':
            break  # Detiene el ciclo
        
        # 5. Agregar el elemento a la lista con append (añade al final)
        lista_productos.append(nuevo_producto)
        # Confirmación para el usuario
        print(f"'{nuevo_producto}' añadido.")
    
    # 6. Mostrar resultados: contar elementos y mostrar la lista final
    total_items = len(lista_productos)
    
    print("\n--- Resultados ---")
    print(f"Se ingresaron {total_items} productos en total.")
    print(f"Tu lista de compras final es: {lista_productos}")

# Ejecutar la función
agregar_productos_a_lista()
