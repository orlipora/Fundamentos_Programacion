

import re 

print("CONTRASEÑA :")
print("Debe tener al menos un número.\nDebe tener al menos un carácter en mayúscula y uno en minúscula.\nDebe tener al menos un símbolo especial.\nDebe tener  minimo 8 caracteres y no contener espacios.")
print("----TIENE 3 INTENTOS----")
print()

def clave(): 
    
    passwd = input("Ingrese Contraseña : ")
    regg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
    patt = re.compile(regg) 
    matt = re.search(patt, passwd) 
    
    if matt: 
        print("Password valido.") 
        
    else: 
        print("Password invalido") 
        return["Password invalid !!-------"]
     
x =clave()

i = 0
for i in range(2):
    i = i+1
    
    if x == ["Password invalid !!-------"]:
        print("INTENTO =======>  ",i+1)
        def clave1(): 
    
            passwd = input("Ingrese nuevamente Contraseña : ")
            regg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            patt = re.compile(regg) 
            matt = re.search(patt, passwd) 
            
            if matt: 
                print("Password valido.") 
                exit()
            else: 
                print("Password invalido") 
    else:
        break
                
    clave1()



      
