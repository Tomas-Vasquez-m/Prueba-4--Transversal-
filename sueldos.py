
import csv
import random

trabajadores = ["Juan Perez", "Carlos lopez", "Ana martinez", "Maria Garcia", "Pedro Rodriguez", 
                "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elena Fernandez"]

sueldo = 'sueldos.csv()'


def menu():
    print("    Bienvenido al Progama de sueldos    ")
    print("1- Asignar sueldos aleatorio")
    print("2- Clasificar sueldos")
    print("3- Ver estadisticas")
    print("4- reporte sueldos")
    print("5- Salir del programa")

def sueldos_aleatorios():
    sueldos = []
    for e in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldo.append(sueldo)
    return sueldo

def sueldos_clasificados():
    print("Clasificación del sueldo")
    for i, sueldo in enumerate(sueldo):
        if sueldo < 800000:
            print(f"{trabajadores [i]} : Sueldo Bajo: {sueldo [i]}")
        elif 800000 <= sueldo <= 2500000:
            print(f"{trabajadores [i]} : Sueldo Medio: {sueldo [i]}")
        elif sueldo > 2500000:
            print(f"{trabajadores [1]} : Sueldo Alto: {sueldo [1]}")
        else:
            print(f"{trabajadores} : Meida Geomterica {sueldo[1]}")

 
def reporte_sueldos():
    print("Reporte de sueldos")
    for i, trabajador in enumerate(trabajadores):
        sueldo_base = sueldo[i]
        print(f"{trabajadores} : {sueldo_base}")




with open ('sueldo_csv', 'w') as sueldo_csv:
    write = csv.writer(sueldo_csv)
    write.writerow(['trabajadores', 'sueldo'])
    for i, trabajadores in enumerate(trabajadores):
        sueldo_base = sueldo[i]
        write.writerow([trabajadores, sueldo_base])

print("El archivo fue guardado en 'sueldos.csv' =) ")
