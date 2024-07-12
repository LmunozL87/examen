import random as rd, csv, statistics

def asignar_sueldos(trabajadores):
    sueldos = {}

    for trabajador in trabajadores:
        sueldo = rd.randint(300000,2500000)
        sueldos[trabajador] = sueldo

    print("\nSueldos asignados correctamente.\n")
    print(sueldos)
    return sueldos

def clasificar_sueldos(sueldos):
    menor_800_mil = {}
    entre_800_2_millones = {}
    mayor_2_millones = {}

    for trabajador,sueldo in sueldos.items():
        if sueldo < 800000:
            menor_800_mil[trabajador] = sueldo
            sueldo_menor_800 = list(menor_800_mil.values())
            total_menor_800 = sum(sueldo_menor_800)
        elif sueldo <= 2000000:
            entre_800_2_millones[trabajador] = sueldo
            sueldo_entre_800_2_millones = list(entre_800_2_millones.values())
            total_entre_800_2_millones = sum(sueldo_entre_800_2_millones)
        else:
            mayor_2_millones[trabajador] = sueldo
            sueldo_mayor_2_millones = list(mayor_2_millones.values())
            total_mayor_2_millones = sum(sueldo_mayor_2_millones)

    total_sueldos = total_menor_800 + total_entre_800_2_millones + total_mayor_2_millones

    print("\n\t**CLASIFICACIÓN**")
    print("\nSueldos menores a $800.000 TOTAL: ",len(menor_800_mil))
    print("\nNombre empleado","\tSueldo")
    for trabajador,sueldo in menor_800_mil.items():
        print(trabajador,"\t$",sueldo)
    
    print("\nSueldos entre $800.000 y $2.000.000\nTOTAL: ",len(entre_800_2_millones))
    print("\nNombre empleado","\tSueldo")
    for trabajador,sueldo in entre_800_2_millones.items():
        print(trabajador,"\t$",sueldo)

    print("\nSueldos superiores a $2.000.000\nTOTAL: ",len(mayor_2_millones))
    print("\nNombre empleado","\tSueldo")
    for trabajador,sueldo in mayor_2_millones.items():
        print(trabajador,"\t$",sueldo)

    print("\nTOTAL SUELDOS: $",total_sueldos)

def estadisticas_sueldos(sueldos):
    sueldo = list(sueldos.values())

    max_sueldo = max(sueldo)
    min_sueldo = min(sueldo)
    promedio_sueldo = sum(sueldo)/len(sueldo)
    media_geometrica = statistics.geometric_mean(sueldo)

    print("\n\t**ESTADISTICAS**")
    print("\nSueldo más alto: \t\t$",max_sueldo)
    print("Sueldo más bajo: \t\t$",min_sueldo)
    print("Promedio de sueldos: \t\t$",promedio_sueldo)
    print("Media geométrica de sueldos: \t$",media_geometrica)

def reporte_sueldos(sueldos):
    for trabajador,sueldo in sueldos.items():
        desc_salud = sueldo * 0.07
        desc_AFP = sueldo * 0.12
        sueldo_líquido = sueldo - desc_salud - desc_AFP

    with open("reporte_sueldos.csv","w",newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Líquido"])

        for trabajador,sueldo in sueldos.items():
            escritor.writerow([trabajador,sueldo,desc_salud,desc_AFP,sueldo_líquido])
    
    print("\nReporte generado correctamente.")



