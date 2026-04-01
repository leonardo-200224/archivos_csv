import csv

# abrimos el archivo con su dirrecion de archivo
# INDICAMOS cuando incia una nueva linea "newline"
notes = ''
average = []
with open("notes.csv", newline='') as f:# f es una especie de variable para ingresar a nuestro archivo
    # leer el archivo
    data = csv.reader(f, delimiter=',')
    notes = list(data)

# print(notes)

# Elemento por elemento ordenado
def getData(notes):
    print(len(notes))
    for i in range(1, len(notes)):
        for j in range(len(notes[i])):
            print(notes[0][j] + ': ' + notes[i][j])
        print('')

def getAverage(notes):
    for i in range(1, len(notes)):
        sum = 0
        med = 0
        print(notes[0][0]+ ':'+ notes[i][0])
        for j in range(1, len(notes[i])):
            sum += float(notes[i][j])
            med = round(sum/3, 2)
        average.append(med)
        print('Media: ' + str(med))


getData(notes)
getAverage(notes)

# Escribir en el archivo datos de media
notes[0].append('Media')
for i in range(1, len(notes)):
    notes[i].append(average[i-1])

with open("notes.csv", 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(notes)
