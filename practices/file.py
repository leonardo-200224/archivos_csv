# importamos el modulo csv, que python trae en su libreria estandar
import csv

personas= [
    ["Palacio","Rivas","Adan","CDMX"],
    ["Torres","Palacio","Sandra","MORELIA"],
    ["Martinez","Martinez","jose","TIJUANA"],
    ["Perez","Ayala","Leonardo","Barranquilla"]
]

# escritura

with open("personas.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=":")
    writer.writerows(personas)

# abrimos el archivo

with open("personas.csv") as f:
    reader = csv.reader(f, delimiter=":")
    for row in reader:
        print("Ap paterno: {0}, Ap materno: {1}, Nombre: {2}, Ciudad: {3}".format(row[0], row[1], row[2], row[3]))
