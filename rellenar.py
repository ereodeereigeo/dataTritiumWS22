from sklearn import linear_model
import numpy as np 
import ext_datos as ext
import pandas as pd
import matplotlib.pyplot as plt
import procesar as pr

def pre_procesamiento(motores, estimador, estimar):
	"""Preprocesamiento de datos de prueba y validacion"""

	#creamos un dataFrame sin los valores perdidos NaN
	motoresTest = motores.dropna()

	#aislamos las variables para trabajar solo con los datos necesarios
	motoresTest=motoresTest[[estimador,estimar]]

	#reordenamos aleatoreamente los datos para obtener dos set de prueba
	#y validacion sin tendencias claras (la mitad de prueba solo rangos altos de voltaje
	# por ejemplo y la mitad de validacion solo con rangos bajos)
	motoresTest=motoresTest.reindex(np.random.permutation(motoresTest.index))

	#separamos los datos entre estimador y variable a estimar
	motor1=motoresTest[estimador]
	motor2=motoresTest[estimar]
	
	#separamos en conjuntos de prueba y validacion
	motor1test=motor1[:len(motor1)/2]
	motor2test=motor2[:len(motor2)/2]
	motor1val=motor1[len(motor1)/2:]
	motor2val=motor2[len(motor2)/2:]
	
	#arreglamos los datos para ajustarse a sklearn linear fit
	motor1test = motor1test.reshape((motor1test.shape[0],-1))
	motor2test = motor2test.reshape((motor2test.shape[0],-1))
	motor1val = motor1val.reshape((motor1val.shape[0],-1))
	motor2val = motor2val.reshape((motor2val.shape[0],-1))

	return motor1test,motor2test,motor1val,motor2val




def regresion_lineal(motores, estimador, estimar):
	motor1test,motor2test,motor1val,motor2val = pre_procesamiento(motores,estimador,estimar)
	regr = linear_model.LinearRegression()
	
	regr.fit(motor1test,motor2test)
	print "la ecuacion de regresion lineal es: %f + %fx" %(regr.intercept_,regr.coef_)
	print "el error cuadratico medio es: %f, (menor valor es mejor ajuste)" %np.mean((regr.predict(motor1val)-motor2val)**2)
	print "la varianza es: %f, (1 significa prediccion perfecta)"%regr.score(motor1val, motor2val)
	plt.scatter(motor1val,motor2val,  color='black')
	plt.plot(motor1val, regr.predict(motor1val), color='blue',linewidth=3)
	plt.show()
	return np.array([regr.intercept_[0], regr.coef_[0]])



