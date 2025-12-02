def calcular_promedio_de_notas_simple():
    # Inicializamos la lista donde guardaremos cada nota (el arreglo)
    lista_de_notas = []
    
    print("--- Calculadora de Promedio de Notas ---")
    print("Ingresa cada nota. Escribe 'fin' para terminar.")
    
    # Usamos un ciclo infinito para pedir notas
    while True:
        entrada = input("Ingresa una nota (0-20) o 'fin': ")
        
        # 1. Condicional de salida
        if entrada.lower() == 'fin':
            break  # Salimos del ciclo si el usuario escribe 'fin'
        
        # 2. Conversión directa (sin try, asumiendo que es un número)
        nota = float(entrada)
        
        # 3. Validación simple (Condicional)
        if 0 <= nota <= 20:
            lista_de_notas.append(nota)  # Agregamos la nota a la lista
        else:
            print("⚠️ Nota fuera del rango válido (0 a 20). No se registró.")
            # Continuamos al siguiente ciclo sin registrar la nota inválida

    # --- Una vez fuera del ciclo, procesamos los resultados ---
    
    # len() devuelve el número de elementos de un objeto 
    # con longitud en Python (un entero).
    cantidad_notas = len(lista_de_notas)

    
    if cantidad_notas == 0:
        print("\nNo se ingresó ninguna nota. Proceso terminado.")
        return  # Terminamos la función
        
    # Calculamos la suma total de las notas
    suma_total = 0
    for n in lista_de_notas:
        suma_total = suma_total + n
        
    # Calculamos el promedio
    promedio = suma_total / cantidad_notas
    
    # --- Mostrar Resultados ---
    print("\n--- Resultados Finales ---")
    print(f"Notas ingresadas: {lista_de_notas}")
    print(f"Total de notas contadas: **{cantidad_notas}**")
    print(f"El promedio de las notas es: **{promedio:.2f}**")
    print("-" * 30)

# Llamamos a la función para ejecutar el programa
calcular_promedio_de_notas_simple()