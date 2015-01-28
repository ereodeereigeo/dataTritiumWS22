# -*- coding: utf8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Se crea una lista de encabezados que servirá para extraer las col
listaEnc = ['time', 'errors', 'limiters', 'currentSP', \
'velocitySP', 'idcSP', 'miscSP', 'busVoltage','busCurrent',\
'velocityMs', 'motorRpm', 'pcCurrent', 'pbCurrent', 'odometer',\
'busCharge', 'bemf','voutD', 'voutQ', 'ioutD', 'ioutQ', '15v',\
'1.9v', '3.3v', 'motorTemp', 'dspTemp', 'phaseaTemp', 'phasebTemp',\
'phasecTemp', 'cantranserr', 'canrecerr', 'slipSpeed']

file = '/home/rodrigo/ownCloud/Software/Software/WSlog_2014-11-17_15-16-21.csv'

#definimos label como opción oculta para acotar los datos extraidos
def extraerData(archivo, label=listaEnc, time=0.2, values=True):

    #se lee el archivo csv
    datos = pd.read_csv(archivo, names=label, header=0)

    #Se genera una lista vacía de vectores
    listVect = []

    #creación de vector de tiempo
    tiempo = datos.index * time
    #time es el tiempo de muestreo en segundos

    #iteración
    for name in label:
        listVect.append(datos[name].values)

    #se crea un diccionario para acceder a los vectores
    dicVect = dict(zip(label,listVect))
    if values:
        return dicVect
    else:
        return tiempo

def extraerValor(nombre):
    dicc=extraerData(file)
    return dicc[nombre]

def extraerTiempo():
    tiempo = extraerData(file, values=False)
    return tiempo

tiempo = extraerTiempo()
busVoltage = extraerValor('busVoltage')
#plt.plot(tiempo,busVoltage)
busCurrent = extraerValor('busCurrent')
#plt.plot(tiempo,busCurrent)
#plt.show()
