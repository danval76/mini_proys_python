#Ejemplo Insert

# Lista inicial
compra = ["pan", "leche", "huevos"]
print(f"Inicio: {compra}") # Salida: ['pan', 'leche', 'huevos']

# Queremos que "mantequilla" vaya a la posición 1 (antes de "leche")
compra.insert(1, "mantequilla")

print(f"Después de insert(): {compra}") # Salida: ['pan', 'mantequilla', 'leche', 'huevos']