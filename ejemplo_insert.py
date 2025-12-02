#Ejemplo Insert

# Creamos la Lista inicial
compra = ["pan", "leche", "huevos"]
# Imprimimos el contenido inicial
print(f"Inicio: {compra}") # Salida: ['pan', 'leche', 'huevos']

# Queremos que "mantequilla" vaya a la posición 1 (antes de "leche")
compra.insert(1, "mantequilla")

# Imprimimos el contenido después de usar insert
print(f"Después de insert(): {compra}") # Salida: ['pan', 'mantequilla', 'leche', 'huevos']