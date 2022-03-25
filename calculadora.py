'''   
solicitar el ingreso de un número y mostrar un menu de operaciones disponibles (seno, coseno, tangente, elevado al cuadrado y raíz cuadrada). Imprimir debajo el resultado luego de elegir la operación, repitiendo indefinidamente mientras el número ingresado para el cálculo sea distinto de 0. Generar mensaje de error si el número de operación elegida no está en la lista.
'''
import math
import os

numero = int(input("Ingrese un Numero :" ))
  
if  numero != 0:
    os.system('cls')   # limpia la pantalla
    print("Numero elegido es ==> ",numero)
    coseno = math.cos(numero)
    seno = math.sin(numero)
    tangente = math.tan(numero)
    cuadrado = numero*numero
    raiz = math.sqrt(numero)

    operacion = input("ingrese operacion a realizar \n\t1 - seno\n\t2 - coseno\n\t3 - tangente\n\t4 - cuadrado\n\t5 - raiz cuadrada \n\tLa opcion es ==> ")
   
    if operacion == "1":
        print("seno = " ,seno)
    elif operacion == "2":
        print("coseno = ", coseno)
    elif operacion == "3":
        print("tangente = ", tangente)
    elif operacion == "4":
        print("cuadrado = ", cuadrado)
    elif operacion == "5":
        print("raiz = ", raiz)
    else:
        print("ERROR opcion no contemplada")
else:
    print("FIN")
    exit()

#os.system('cls') # NOTA para windows tienes que cambiar clear por cls
'''
print(" coseno = ",coseno ,"\n","seno = ",seno,"\n","tangente = ",tangente,"\n","cuadrado = ",cuadrado,"\n","raiz cuadrada = ",raiz)


dato = []
cantidad = 2

for i in range(cantidad):
  dato.append(float(input("Dígame su peso en kg: ")))
print(dato)
'''