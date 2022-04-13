from math import fabs


print("CONTRASEÑA :")
print("Debe tener al menos un número.\nDebe tener al menos un carácter en mayúscula y uno en minúscula.\nDebe tener al menos un símbolo especial.\nDebe tener  minimo 8 caracteres y no contener espacios.")




largo = False
espacio = False #.isspace()
minuscula = False # .islower()
numero = False #.isdigit()
alfanum = False # .isalnum()
mayuscula = False # .isupper()

password = input("Ingrese la Contraseña ==>  ")

for i in range(2):
  
    for carat in password:           #12qwertyu12
        if len(password) < 8 :
            largo = True             #si
        if carat.isspace()== True:
            espacio = True           #no
        if carat.isupper()==True:
            mayuscula = True         #no
        if carat.islower()==True:
            minuscula = True         #si
        if carat.isdigit()==True:    
            numero = True            #si
        if carat.isalnum()==True:
            alfanum = True           #no
        
    if  espacio == True or largo == True:  # no  si
           print()
           print(len(password),"largo incorrecto o contiene espacios")
           print(" le quedan =>",3-(i+1)," intentos")
           password = input("Ingresela Nuevamente  :")
           print()
    if mayuscula == True and minuscula == True and numero == True and alfanum == True:
           
           print("Contraseña Correcta")
           break

    else:
           print()
           print("ERROR")
           print(" le quedan =>",3-(i+1)," intentos")
           password = input("Ingresela Nuevamente  :")
           print()

    
    print("Contraseña Incorrecta")
    break

    
