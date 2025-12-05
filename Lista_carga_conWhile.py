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
        
        nuevo_producto = input("Producto a añadir: ")
        if nuevo_producto.lower() == 'fin':
            break  # Detiene el ciclo   
        lista_productos.append(nuevo_producto)      
        print(f"'{nuevo_producto}' añadido.")
    
    total_items = len(lista_productos)
    
    print("\n--- Resultados ---")
    print(f"Se ingresaron {total_items} productos en total.")
    print(f"Tu lista de compras final es: {lista_productos}")


agregar_productos_a_lista()
