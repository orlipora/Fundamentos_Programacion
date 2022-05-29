from pip import main
import requests
from datetime import datetime
from datetime import date
import time
import  os


FREC_CONTROL= 5 # SE LLAMA POLLING
LIMITE_TEMP = 20
URL_API = 'http://pad19.com:3030/sensor33'
tiempo = time.time()
alarma_activada = False #flag


def main():
    global alarma_activada
    os.system('cls')
    #while alarma_activada==False:
    while not alarma_activada:
        conexion = requests.get(URL_API)
        if conexion.status_code==200:
            contenido = conexion.json()
            #print(contenido )

            if contenido['estado']=='ok':
                temp=contenido['lectura']
                if temp<LIMITE_TEMP:
                    alarma_activada=True
                    print('/////////////////')
                    print('ADVERTENCIA TEMP=> ',temp,'---',fecha())
                    print('/////////////////')
                else:
                    print('Temperatura rango Normal : ',temp )
                    time.sleep(5)
        alarma_activada = False


def fecha ():
   fecha_act = datetime.now() #da fecha y hora
   #fecha_act=date.today() # da la fecha
   return fecha_act



if __name__ == '__main__':
    main()
    
        



