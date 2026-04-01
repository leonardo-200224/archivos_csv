from functions import *

student=[]
counter =1
while counter ==1:
    print("\n System menu\n ")
    value = int(input("1- Load csv\n"
                        "2- Save csv\n"
                        "3- New student\n"
                        "4- summary the students\n"
                        "5- Exit \n"
                        ": "))


    if value == 1:
        name_ruta_csv = input("Enter name the ruta: ")
        name_ruta_csv += ".csv"
        value_finish = Load_csv(name_ruta_csv)
        
        if value_finish:
            opcion = input("Sobre escribir inventario actual?: yes / no: ").upper()

            if opcion == "SI":
                student = value_finish
                print("\n Inventario reemplazado\n")
            elif opcion == "NO":

                for diccionario in value_finish:
                    encontrado = False

                    for actual in student:
                        if diccionario["ID"] == actual["ID"]:
                            encontrado = True
                            break
            
                if not encontrado:
                    student.append(diccionario)   
        continue

    elif value == 2:
        name_ruta = input("Enter name the ruta: ")
        name_ruta += ".csv"
        save_csv(student, name_ruta)
        continue

    elif value == 3:
        new_student = new_student_def()
        student.append(new_student)
        continue

    elif value == 4:
        summary(student)
        continue

    elif value == 5:
        counter =2
    else:
        print("ERROR: Enter number the (1 - 5) please")