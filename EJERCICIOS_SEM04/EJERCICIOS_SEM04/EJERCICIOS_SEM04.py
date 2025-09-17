def ejer1():
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        print("Menor de edad")
    else:
        if edad >= 18 and edad <=64:
            print("Adulto")
        else:
            print("Adulto mayor")

def ejer2():
    an = int(input("Ingrese el anio actual: "))
    if (an % 4 == 0 and an % 100 != 0) or (an % 400 == 0):
        print("Es un anio bisiesto")
    else:
        print("Anio no bisiesto")

    if an % 2 == 0:
        print("Anio par")
    else:
        print("Anio impar")

def ejer3():
    mont = float(input("Ingrese el monto en soles(S/): "))
    opcion = int(input("\n1. Dolares\n2. Euros\nSelecciones una opcion: "))

    match opcion:
        case 1: print("Dolares: ", mont/3.75)
        case 2: print("Euros: ", mont/4.05)
        case _: print("Opcion no valida")

import math
def ejer4():
    print("Bienvenido al sistema de resolucion de areas")
    opcion = int(input("1. Cuadrado\n2. Rectangulo\n3. Triangulo\n4. Circulo\nSeleccione opcion: "))
    match opcion:
        case 1:
            lado = int(input("Ingrese el lado: "))
            print("Area cuadrado: ", lado * lado)
        case 2:
            bse = int(input("Ingrese la base: "))
            alt = int(input("Ingrese la altura: "))
            print("Area rectangulo: ", bse * alt)
        case 3:
            bse1 = int(input("Ingrese la base: "))
            alt1 = int(input("Ingrese la altura: "))
            print("Area triangulo: ", (bse1 * alt1) / 2)
        case 4:
            radio = float(input("Radio: "))
            print("Area circulo: ", round(math.pi * radio * radio, 2))
        case _:
            print("Valor ingresado incorrecto")

ejer4()
