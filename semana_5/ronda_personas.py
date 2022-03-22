"""
EJERCICIO RONDA DE PERSONAS

Tareas realizadas:
- Contar en ronda de 1 en 1.
- Controlar límite de personas en ronda.
-La que comienza se decide al azar,
- Detectar cuenta divisible por 8 y cambiar en ese momento sentido de giro ronda

Tareas pendientes:
- Detectar cuenta divisible por 11 y saltar 1 persona, siguiendo mismo sentido de giro
Ej, si está contando horario la persona 8, la siguiente en contar deberá ser la 10; si es antihorario, la 6

- Permitir ingresar ctd de personas en ronda y límite de cuenta por consola, en lugar de indicarlos de forma fija
Ej: int(input("Personas en la ronda: "))

- Si el límite de cuenta es menor a la cantidad de personas en la ronda, no efectuar la cuenta, solo mostrar
en su lugar un mensaje de error con print
"""
import random

PERSONAS= int(input( "Cantidad de personas => "))
LIMITE_CONTAR = int( input( "Limite-Contar => "))

persona = random.randint(1,PERSONAS-1) 
# debo poner persona-1 , porque si no en el for me agrega 1 persona
# y si tengo PERSONAS = 4 , aparece persona 5 que no existe

contar = 0
giro = "horario"

if LIMITE_CONTAR < PERSONAS:
    print("ERROR - Aumentar limite Contar")
else:
    print("Comienza la persona => ",persona+1) # +1 para que coincida
    # con la que comienza a contar
    
    for cuenta in range(LIMITE_CONTAR):
        contar = contar + 1

        if giro == "horario":
            if persona == PERSONAS:
                persona = 0
            persona = persona + 1

        else:
             if persona == 1:
                persona = PERSONAS +1
             persona = persona - 1
              
        print(persona,contar)
    
        if contar % 8 == 0:
            if giro == "horario":
               giro = "antihorario"
            else:
                giro = "horario"

        if  contar % 11 == 0:
            if giro == "horario":
                persona = persona + 1  

            else :
                
                persona = persona - 1  
             
    
    
    
