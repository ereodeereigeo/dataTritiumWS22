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
def extraer_data(archivo, fecha=None, label=listaEnc, time=0.2, values=True):

	#se crea una lista con los nombres de archivos del directorio indicado
	lista = ob.obtener_archivos(archivo, fecha)

	#se leen los archivos csv creandose una lista de tablas
	tablas = []
	for nombres in lista:

		#lee los datos del archivo csv
		datos = pd.read_csv(nombres, names=label, header=0, index_col = 0, parse_dates = True)
		count = 1
		for i in range(0,5):
			if datos.index[i]==datos.index[i+1]:
				count+=1
			else:
				break
		if count==5:
			fecha_indice_inf = nombres[6:16]+' '+nombres[17:19]+':'+nombres[20:22]+':'+nombres[23:25]
		elif count == 4:
			fecha_indice_inf = nombres[6:16]+' '+nombres[17:19]+':'+nombres[20:22]+':'+nombres[23:25]+'.2'
		elif count == 3:
			fecha_indice_inf = nombres[6:16]+' '+nombres[17:19]+':'+nombres[20:22]+':'+nombres[23:25]+'.4'
		elif count == 2:
			fecha_indice_inf = nombres[6:16]+' '+nombres[17:19]+':'+nombres[20:22]+':'+nombres[23:25]+'.6'
		elif count == 1:
			fecha_indice_inf = nombres[6:16]+' '+nombres[17:19]+':'+nombres[20:22]+':'+nombres[23:25]+'.8'
		else:
			print "error"
		periodo = len(datos.index)
		tiempo_nuevo=pd.date_range(fecha_indice_inf,periods=periodo, freq='200ms', name = 'time')
		datos.index = tiempo_nuevo
		datos = datos.convert_objects(convert_numeric=True)
		datos = datos.drop(datos[['miscSP','velocityMs','odometer','busCharge','15v',\
		'1.9v','3.3v','phaseaTemp','phasebTemp','cantranserr', 'canrecerr', 'slipSpeed']],1)
		if fecha == None:
			tablas.append(datos)
		elif str(fecha) == str(nombres[6:16]):
			tablas.append(datos)

	return tablas
