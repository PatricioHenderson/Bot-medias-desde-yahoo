#!/usr/bin/env python
'''

Bot de Medias Moviles
---------------------------
Autor: Patricio Henderson Vigil
Version: 1.0

Descripcion:
Programa que analiza si hubo cruce de medias moviles
'''

__author__ = "Patricio Henderson"
__email__ = "patriciohenderson@hotmail.com"
__version__ = "1.3"


import csv
import pandas_datareader as pdr
import statistics

precio_veinte = 0
precio_doce = 0

#Descarga del archivo .csv con la cotización

panel_lider = ["GGAL"]
#Seleccionamos las acciones que queremos descargar por su ticker, en este caso "Galicia"
for i in panel_lider:
    df = pdr.get_data_yahoo(str(i)+".BA","01/01/20",interval = "w") 
    #Seleccionamos la bolsa donde cotizan ".BA" la fecha desde y el intervalo
    df = df[df["Volume"]>0]
    #Eliminamos los dias con volumen de operación 0
    df = df.drop(["Adj Close"], axis = 1)
    #elimnar información sobre los cierres ajustados
    df.to_csv(str(i)+ "BA.csv")
    #Damos nombre y escrbimos el archivo.csv
    
    print(i, "Descargado")


#Procedemos a sacar la media de los últimos 20 períodos

with open ("GGALBA.csv") as fo:
#Abrimos archivo .csv    

    file = list(csv.DictReader(fo))
    #leemos en forma de lista
    len_reader = len(file)
    
    ultimas_veinte = len_reader - 20
    #Restaos para obtener las últimas 20 y poder sacar la media

    for i in range(ultimas_veinte,len_reader):

        row = file[i]
        #arrancamos desde las últimas 20 filas
        precio_cierre = float(row.get("Close"))
        #obtenemos el precio de cierre
        precio_veinte += precio_cierre
        #Vamos sumando el precio de cierre
    promedio_veinte = precio_veinte / 20
    #obtenemos el promedio del cierre de las últimas 20 rondas.
    

    #Ahora sacamos el promedio de las ultimas 12 rondas
    ultimas_doce = len_reader - 12
    #Restaos para obtener las últimas 20 y poder sacar la media

    for i in range(ultimas_doce,len_reader):

        row = file[i]
        #arrancamos desde las últimas 20 filas
        precio_cierre = float(row.get("Close"))
        #obtenemos el precio de cierre
        precio_doce += precio_cierre
        #Vamos sumando el precio de cierre
    promedio_doce = precio_doce / 12
    #obtenemos el promedio del cierre de las últimas 20 rondas.

print (promedio_doce, promedio_veinte)
#Realizamos conclusiones :

if promedio_doce > promedio_veinte :
    print("No mirar esta acción")

if promedio_doce == promedio_veinte :
    print("Observar acción puede ser compra")

if promedio_doce < promedio_veinte:
    print("Esperar esta acción puede dar compra")