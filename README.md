### Bot de alerta de Cruces de medias 

#### Descripción :

El siguiente bot realiza un analisis del cruce de medias de 9 y 18 de las empresas del panel lider de MERVAL, en dos períodos temporales, mensual y diario.

Surje un alerta cuando la diferencia entre la media de 9 y la de 18 es menor a $1,00.

### Funcionamiento :

-1 : Lo primero que hace es bajar los datos en compresion diaria desde yahoo finance en archivos .csv

-2 : Una vez que tenemos estos archivos analiza si la diferencia entre los precios es menor a $1.

-3 : Si la diferencia es menora  $1, realiza un alerta que también se replica en twitter.

-4 : Si la diferencia es mayora a $1, no realiza nada, continua ejecutando el programa.

-5 : Si existe un error realiza un alerta por pantall y también se deja por escrito en un archivo llamado "reporte_errores.txt"

-6 : Realiza nuevamente los pasos 1 a 5 pero en compresion semanal.

### Requerimientos:

Para poder correr el programa es necesario tener instalado pandas_datareader y pandas, para ello debemos:

-1 : Abrir la consola y tipear pip3 install pandas-datareader 

-2 : Abrir la consola y tipear pip3 install pandas

Si se tiene instalado una versión anterior a python 3.0 el proceso es igual pero en vez de pip3 se debe tipear pip 

En caso de tener más de una versión de python instalada, es posible que las librerias se instalen en otra version del programa que estamos intentando correr.


