import funciones as fn

trabajadores = [
    "Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez",
    "Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"
    ]

sueldos = {}

while True:

    print("\n\t****MENU****\n")
    print("1. Asignar sueldos aleatorios.")
    print("2. Clasificar sueldos.")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos.")
    print("5. Salir del programa.")

    opcion = int(input("Seleccione una opcion entre 1 y 5. "))

    if opcion == 1:
        sueldos = fn.asignar_sueldos(trabajadores)

    elif opcion == 2:
        if sueldos:
            fn.clasificar_sueldos(sueldos)
        else:
            print("Primero debe asignar sueldos.\n")

    elif opcion == 3:
        if sueldos:
            fn.estadisticas_sueldos(sueldos)
        else:
            print("Primero debe asignar sueldos.\n")

    elif opcion == 4:
        if sueldos:
            fn.reporte_sueldos(sueldos)
        else:
            print("Primero debe asignar sueldos.\n")

    elif opcion == 5:
        print("\nFinalizando programa...\nDesarrollado por Luis Muñoz\nRUT 16.753.743-K\n")
        break
    else:
        print("Seleccione una opcion entre 1 y 5.\n")