## File csv
- "r" → leer
Solo lectura
Error si no existe

- "w" → escribir
Escribe desde cero
BORRA todo lo anterior

- "a" → append (agregar)
Agrega al final
No borra nada

- "x" → crear
Crea archivo nuevo
Error si ya existe

# EXTRA
- "a+"  # leer + escribir
- "r+"  # leer + escribir (no crea archivo)
- newline="" -> Evita líneas en blanco extra

with open(ruta, mode="a", newline="", encoding="utf-8") as archivo:
  
  if incluir_header and not os.path.exists(ruta):
      writer.writerow(["nombre", "precio", "cantidad"])
