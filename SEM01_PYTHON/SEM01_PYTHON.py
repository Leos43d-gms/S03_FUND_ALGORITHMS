def ejer1():
    nombre=input("Ingrese su nombre: ")
    carrera=input("Ingrese su carrera: ")
    
    print(f"\nBienvenido al curso de Fund. de Algoritmos{nombre}, de la carrera {carrera}")

def ejer2():
    print("\"Leonardo\"")

def ejer3():
    N1 = int(input("Ingrese N1: "))
    N2 = int(input("Ingrese N2: "))

    print("\nSuma: ", (N1+N2))
    print("Resta: ", (N1-N2))
    print("Multi: ", (N1*N2))
    print("Divi: ", (N1/N2))

import math
def ejer4():
    num=float(input("Ingrese un num decimal: "))

    raiz2 = math.sqrt(num)
    redo = round(num,0)
    cubo = math.pow(num,3)
    raiz3 = math.pow(num, 1/3)

    print("\nRaiz 2: ",raiz2)
    print("Redondeo: ",redo)
    print("Al cubo: ",cubo)
    print("Raiz 3: ",raiz3)

def ejer5():
    num=input("Ingrese un numero: ")

    entero=int(num)
    deci=float(num)

    print("\nResto: ", entero%2)
    print("Dividido 3: ", deci/3)

ejer5()
