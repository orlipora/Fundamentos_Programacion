
import json
import os
RUTA = 'sem11/form1.json'
os.system('cls')

def leer_arch (RUTA):
    archiv = open(RUTA,'r')
    archivo = json.load(archiv)
    archiv.close()
    return archivo

def main():
    ARCHIVO = leer_arch (RUTA)
    print(["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"][0]["points"])



if __name__ == '__main__':
     main()
     