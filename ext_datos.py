# -*- coding: utf8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import obtener as ob
#Se crea una lista de encabezados que servirá para extraer las col
listaEnc = ['time', 'errors', 'limiters', 'currentSP', \
'velocitySP', 'idcSP', 'miscSP', 'busVoltage','busCurrent',\
'velocityMs', 'motorRpm', 'pcCurrent', 'pbCurrent', 'odometer',\
'busCharge', 'bemf','voutD', 'voutQ', 'ioutD', 'ioutQ', '15v',\
'1.9v', '3.3v', 'motorTemp', 'dspTemp', 'phaseaTemp', 'phasebTemp',\
'phasecTemp', 'cantranserr', 'canrecerr', 'slipSpeed']

#definimos label como opción oculta para acotar los datos extraidos
def extraerData(archivo, fecha=None, label=listaEnc, time=0.2, values=True):

    #se crea una lista con los nombres de archivos del directorio indicado
    lista = ob.obtener_archivos(archivo, fecha)

    #se leen los archivos csv creandose una lista de tablas
    tablas = []
    for x in archivo:
        datos = pd.read_csv(x, names=label, header=0,)
        tablas.append(datos)
    return tablas
