
from ctypes import wstring_at


print("CONTRASEÑA :")
print("Debe tener al menos un número.\nDebe tener al menos un carácter en mayúscula y uno en minúscula.\nDebe tener al menos un símbolo especial.\nDebe tener  minimo 8 caracteres y no contener espacios.")
print("----TIENE 3 INTENTOS----")
print()

largo = False
espacio = False #.isspace()
minuscula = False # .islower()
numero = False #.isdigit()
alfanum = True # .isalnum()
mayuscula = False # .isupper()

password = input("Ingrese la Contraseña ==>  ")

for i in range(2):
  
    for carat in password:          
        if len(password) >= 8 :
            largo = True 
                       
        if carat== ' ':
            espacio = True 
                   
        if carat.isupper()==True:
            mayuscula = True 
                   
        if carat.islower()==True:
            minuscula = True 
                  
        if carat.isdigit()==True:    
            numero = True 
                      
        if carat.isalnum()==False:
            alfanum = False 
           

        
    if  espacio == True or largo == False:  
           print()
           print(len(password),"largo incorrecto o contiene espacios")
           print(" le quedan =>",3-(i+1)," intentos")
           password = input("Ingresela Nuevamente  :")
           print()
    elif mayuscula == True and minuscula == True and numero == True and alfanum == False:
           
           print("Contraseña Correcta")
           exit()

    else:
           print()
           print("ERROR")
           print(" le quedan =>",3-(i+1)," intentos")
           password = input("Ingresela Nuevamente  :")
           print()

    

print("Contraseña Incorrecta")
   
'''
El método str. isalnum() devuelve True si los caracteres son alfanuméricos, lo que significa que no hay caracteres especiales en la cadena. Si hay caracteres especiales en la cadena, devolverá False 
'''
    

