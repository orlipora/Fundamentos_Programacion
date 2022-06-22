import  requests
import pprint
import json
import os

RUTA = 'http://pad19.com:3030/productos/10?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMiLCJub21icmUiOiJhbHVtbm8ifQ.eC452_kHQbCP4wDVvN6nl5Vx8V6HhQP8D5EljApFXS8'


URL_API_POST = 'http://pad19.com:3030/pedidos/10?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjMiLCJub21icmUiOiJhbHVtbm8ifQ.eC452_kHQbCP4wDVvN6nl5Vx8V6HhQP8D5EljApFXS8'



def main(ruta,formato):
    consulta = requests.get(ruta)

    if consulta.status_code ==200:
        if formato == 'json':
            return consulta.json()
    return False


def pedido():
    global p1,cant
    p1 = []

    for i in range(len(productos)):
        print(productos[i]['nombre'],'--$ ',productos[i]['precio'])
        cant =int(input('Ingrese Cantidad==> '))
        if cant < productos[i]['stock'] and productos[i]['stock'] > 0:
            p1.append(cant)
            productos[i]['stock']= cant
        else:
            cant='No Hay stock'
            p1.append(cant)
        print()

def enviar_pedido(URL,params):
    solicitud = requests.post(URL, json=params)
    
    if (solicitud.status_code == 200):
        return solicitud.json()
    return False


if __name__ == '__main__':
    consulta_prod =main(RUTA,'json')
    os.system('cls')
  
    if consulta_prod == False:
        print('error al recuperar informacion')
    else:
        print('///// Listado de productos con precios y cantidades en stock /////')
        pprint.pprint(consulta_prod['productos'])
    
    print('------------REALIZE SU PEDIDO------------')
    productos = consulta_prod['productos']

    print()
    print(pedido())
    print()
    print('Lista de cantidades pedidas')
    print(p1)
    print()
    print('LISTA DE LOS PRODUCTOS CON SUS CANTIDADES PEDIDAS')
    pprint.pprint(productos)

    pedid = (productos)
    print('.-.-.-.-.-.-.-.-.-.-.-.-.-')
    proceso = enviar_pedido(URL_API_POST, pedid )
    
    if (proceso == False):
        print("Error al conectar con el servidor ")
    else:
        print(proceso["mensaje"])
   