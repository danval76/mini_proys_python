def contar_y_sumar_pares(limite):
    """
    Calcula la cantidad y la suma de números pares en el rango de 0 hasta el límite dado.
    """
    contador_pares = 0
    acumulado_pares = 0
    
    # El rango debe incluir el número límite, por eso usamos limite + 1
    for numero_actual in range(limite + 1):
        
        # Operador módulo (%): Si el resto de dividir por 2 es 0, el número es par.
        if numero_actual % 2 == 0:
            contador_pares += 1       # Equivalente a contador_pares = contador_pares + 1
            acumulado_pares += numero_actual # Equivalente a acumulado_pares = acumulado_pares + numero_actual

    return contador_pares, acumulado_pares # Devolvemos ambos resultados

def contarPares():
    """
    Función principal que controla el flujo y la interacción con el usuario.
    """
    print("--- Analizador de Números Pares ---")
    
    # Ciclo 'while True' para que el programa funcione continuamente
    while True:
        entrada = input("\nIngresa un número positivo (o escribe 'salir' para terminar): ")
        
        # Condicional de salida
        if entrada.lower() == 'salir':
            print("Programa finalizado. ¡Hasta pronto!")
            break
          
  
        numero_limite = int(entrada)
        
        if numero_limite < 0:
            print("Por favor, ingresa un número POSITIVO.")
            continue # Vuelve al inicio del ciclo
            
        # Llamamos a la función para realizar el cálculo
        conteo, suma = contar_y_sumar_pares(numero_limite)
        
        # Mostrar resultados
        print(f"Rango analizado: 0 hasta {numero_limite}")
        print(f"-> Cantidad de números pares: **{conteo}**")
        print(f"-> Sumatoria de números pares: **{suma}**")
        

# Ejecutar el programa
contarPares()
