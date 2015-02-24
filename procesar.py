# -*- coding: utf8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import obtener as ob

def sep(data):
	"""Separa los datos entre el motor 1 y el motor 2
	se debe ingresar una lista de dataframes creados con el modulo
	ext_datos.py"""
	motor1 = []
	motor2 = []
	for tablas in data:

		'''explora los dataframes guardados y evalua
		si corresponde al motor 1 o al motor2
		esto se obtiene por la id de los errores
		el motor 1 muestra mensajes con un codigo
		de 0x0 hasta 0x10 y de 0x40 a 0x50 muestra
		el del otro motor y entrega dos listas de
		dataframes'''
		motor = tablas[tablas['errors']<' 0x40']
		if len(motor.values) != 0:
			motor1.append(motor)

			motor = tablas[tablas['errors']>=' 0x40']
		if len(motor.values) != 0:
			motor2.append(motor)

	return motor1, motor2

def concatenar(motor1,motor2):
	"""concatena las listas separadas en un solo dataframes
	y resamplea cada 200 ms tomando un promedio de los datos
	repetidos"""
	motor1total = pd.concat(motor1)

	motor1total = motor1total.resample('200ms')

	motor2total = pd.concat(motor2)

	motor2total = motor2total.resample('200ms')

	return motor1total,motor2total

def juntar(motor1total, motor2total):
	motores = None
	motores = motor1total.join(motor2total,how='outer',lsuffix = '_m1', rsuffix = '_m2')
	return motores

def procesar(data):
	motor1 , motor2 = sep(data)
	motor1total , motor2total = concatenar(motor1 , motor2)
	motores = juntar(motor1total , motor2total)
	return motores
