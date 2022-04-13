
import random
import  os


temp_test = int(input('Ingrese temperatura de testeo :' ))


while temp_test != 0:
    os.system('cls')
    lis_temp = []
    suma1 = 0
    for i in range(50):
        lis_temp.append (random.randint(300,320))
        suma1 = lis_temp[i] +suma1
        lis_temp.sort()
        
    suma = suma1 /50
    print('Temp_Promedio : ', suma, 'ºC')
    print('tem_test : ', temp_test , 'ºC')
    #print(lis_temp)
    
   
   

    if temp_test < 200:
        print('Encender 2 Quemadores')

    elif temp_test >= 200 and temp_test <300:
        print('Encender 1 Quemadores')
    elif temp_test >= 300  and temp_test <= 320 :
        print('Temperatura Correcta')
    else:
        print('Fuera de rango')

    temp_test = int(input('Ingrese nueva temperatura de testeo :' ))
    
else:
    print('FIN')