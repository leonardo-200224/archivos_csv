import csv 

def new_student_def():
    print("\nEnter New Student\n")
    value_ID = int(input("Enter ID the student: "))
    name = input("Enter name the student: ")
    age = int(input("Enter age the studen: "))
    cuorse = input("name the program: ")

    student= {
        "ID"    : value_ID,
        "name"  : name,
        "age"   : age,
        "cuorse": cuorse
    }

    return student

def summary(value):
    if not value:
        print("ERROR: zero students")
    else:
        print("\nSUMMARY\n")

    for student in value:
        print(f"ID: {student["ID"]} | name: {student["name"]} | age: {student["age"]} | cuorse: {student["cuorse"]}\n")
    
    return None

# -------------------------------------------
# CSV 

# save in csv
def save_csv(value, ruta, header=True):
    
    if not value:
        print("ERROR: Zero Students in the file")
        return

    try:
        with open(ruta, mode="w", newline='', encoding="utf-8") as archivo:
            writer = csv.writer(archivo)

            if header:
                writer.writerow(["ID", "name", "age", "cuorse"])
            
            for producto in value:
                writer.writerow([
                    producto["ID"],
                    producto["name"],
                    producto["age"],
                    producto["cuorse"]
                ])

            print(f"\nInventario guardado en: {ruta}\n")
    
    except Exception as e:
        print(f"\n Error al guardar archivo: {e}\n")


# load csv

def Load_csv(ruta):
    inventary = []
    error = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            """
            NEXT() -> Leer la primera fila del CSV
            Guardarla en encabezado
            Y avanzar el cursor (ya no vuelve a leer esa línea)
            """
            encabezado = next(reader)

            if encabezado != ["ID", "name", "age", "cuorse"]:
                print("\nEncabezado invalido\n")
                return []

            for fila in reader:
                if len(fila) != 4:
                    error += 1
                    continue
                try:
                    value_ID = int(fila[0])
                    name = fila[1]
                    age = int(fila[2])
                    cuorse = fila[3]

                    if value_ID  < 0 or age < 0 :
                        error +=1
                        continue
                    
                    producto = {
                        "ID"    :value_ID,
                        "name"  :name,
                        "age"   :age,
                        "cuorse": cuorse
                    }

                    inventary.append(producto)


                except ValueError:
                    error += 1

        print(f"\n Students load: {len(inventary)}")
        print(f"\n ERROR the Students load: {error}\n")
        
        return inventary

    except FileNotFoundError:
        print("\n Archivo no encontrado\n")
        return 

    except Exception:
        print(f"\n Error al leer archivo: {e}\n")
        return


    
