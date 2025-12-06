def calcularNotas():
    suma_total_notas = 0.0
    contador_notas = 0
    
    print("--- Analizador de Notas por Estudiante ---")
    print("Ingresa las notas una por una. Escribe 'fin' para ver el resumen.")
    
    while True:
        entrada = input("\nIngresa la nota (0-20) o 'fin': ")
        
        if entrada.lower() == 'fin':
            break  # Rompe el ciclo while para ir a calcular el promedio
            
        nota = float(entrada)
        
        literal = ""
        
        if nota >=16 and nota <=20: #otra manera de escribirlo: if 16 <= nota <= 20:
            literal = "A"
        elif 13 <= nota <= 15:
            literal = "B"
        elif 10 <= nota <= 12:
            literal = "C"
        elif 0 <= nota <= 9:
            literal = "D"
        else:
            print("⚠️ Nota fuera del rango 0-20. Esta nota no será contada.")
            continue # Vuelve al inicio del ciclo, sin contar ni acumular

        contador_notas += 1       # contador_notas = contador_notas + 1
        suma_total_notas += nota  # suma_total_notas = suma_total_notas + nota
        
        print(f"-> Nota registrada: {nota:.2f} | Literal Obtenido: {literal}")
        
    # --- Fin del ciclo While ---
    
    print("\n--- RESUMEN FINAL ---")
    
    if contador_notas == 0:
        print("No se ingresó ninguna nota válida para calcular el promedio.")
        return 
        
    promedio_final = suma_total_notas / contador_notas
    
    print(f"Total de notas introducidas: **{contador_notas}**")
    print(f"Promedio de las notas: **{promedio_final:.2f}**")
    print("-" * 30)

calcularNotas()