
import math


def Menu():
    """Funcion que Muestra el Menu"""
    print("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Exponente
6) Division Modular
7) Salir""")


def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc > 0 and opc < 7):

        x = int(input("Ingrese numero y luego presione enter\n"))
        y = int(input("Ingrese Otro Numero y luego enter para obtener el resultado\n"))
        if (opc == 1):
            print("La Suma es:", x+y)
            print("--------------------------------\n")
            Menu()
            opc = int(input("Selecione Opcion\n"))
        elif(opc == 2):
            print("La Resta es:", x-y)
            print("--------------------------------\n")
            Menu()
            opc = int(input("Selecione Opcion\n"))
        elif(opc == 3):
            print("La Multiplicacion es:", x*y)
            print("--------------------------------\n")
            Menu()
            opc = int(input("Selecione Opcion\n"))
        elif(opc == 4):
            try:
                print("La Division es:", x/y)
                print("--------------------------------\n")
                Menu()
                opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
                print("No se Permite la Division Entre 0")
                print("--------------------------------\n")
                opc = int(input("Selecione Opcion\n"))
        elif(opc == 5):
            print("El numero ", x, "elevado al exponente: ", y, "es: ", x**y)
            print("--------------------------------\n")
            opc = int(input("Selecione Opcion\n"))
        elif(opc == 6):
            print("El resultado modular de  ", x,
                  "mod de  : ", y, "es: ", x % y)
            print("--------------------------------\n")
            opc = int(input("Selecione Opcion\n"))


Calculadora()
