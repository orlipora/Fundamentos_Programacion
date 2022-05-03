
import json
import os
RUTA = 'sem11/form1.json'
lis = []

os.system('cls')

def leer_arch (RUTA):
    archiv = open(RUTA,'r')
    archivo = json.load(archiv)
    archiv.close()
    return archivo

def main():
    ARCHIVO = leer_arch (RUTA)

    for i in range(3):
        puntos = ARCHIVO["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["points"]
        victoria = ARCHIVO["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["wins"]

        nombre = ARCHIVO["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["Driver"]["givenName"]
        apellido = ARCHIVO["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][i]["Driver"]["familyName"]
        datos = f'El corredor  {nombre} {apellido}  tiene  {victoria}  victorias y acumulo  {puntos}  puntos .'
        lis.append(datos)
    return lis



if __name__ == '__main__':
     main()
     for i in lis:
         print(i )
     