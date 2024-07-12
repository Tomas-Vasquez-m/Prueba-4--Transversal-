
from sueldos import menu, sueldos_aleatorios, sueldos_clasificados, reporte_sueldos

sueldo = []
def main():
    menu()
    num = int(input("Ingrese una opción: "))
    while True:
        try:
            if num == 1:
                sueldos = sueldos_aleatorios()
            elif num == 2:
                sueldos  = sueldos_clasificados()
            elif num == 3:
                sueldos 
            elif num == 4: 
                sueldos = reporte_sueldos()
            elif num == 5:
                print("Usted a salido del programa \nCreado por: Tomas Vasquez \nRUT: 21.467.019-4")
                break
        except ValueError:
            print("Ingrese una opción valida")
            

if __name__ == "__main__":
     main()