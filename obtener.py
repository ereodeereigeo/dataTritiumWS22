# -*- coding: utf-8 -*-
import os
import glob

def lista_archivos():

    #crear una lista con los nombres de los archivos
    #ubicados en el directorio actual
    lista = glob.glob('*.csv')

    #creamos una nueva lista para no mutar la lista al iterar y borrar
    #lo que creó el bug que al haber 2 elementos no generaba la lista
    #correctamente
    lista_nueva = []

    #iteramos dentro de la lista para ver si posee la palabra
    # 'WSlog' que generan todos los archivos guardados con el
    #programa del controlador WaveSculptor 22, si no la posee
    #no se incluye el archivo posteriormente
    for i in xrange(len(lista)):
        if 'WSlog' in lista[i]:
            lista_nueva.append(lista[i])
    lista_nueva.sort()
    return lista_nueva

def obtener_archivos(directorio , fecha=None):

    #obtenemos el path completo actual
    directorio_actual = os.getcwd()

    #el directorio es una cadena
    #con / si esta en linux y con
    # \ si esta en windows
    if '/' in directorio_actual:
        lista_dir_act = directorio_actual.split('/')
    elif directorio_actual.find('\ '):
        lista_dir_act = directorio_actual.split('\ ')
    else:
        lista_dir_act = [directorio]

    #verificamos si los archivos están en el mismo directorio del módulo
    if directorio == lista_dir_act[-1]:

        #añadimos los nombres de los archivos a una lista
        nombres_archivos = lista_archivos()
        return nombres_archivos

    #si no, probamos si está en una carpeta dentro del directorio actual
    elif os.path.exists(directorio):

        os.chdir(directorio) #y si está entramos a esa carpeta

        #y añadiremos los nombres de los archivos a una lista
        nombres_archivos = lista_archivos()
        return nombres_archivos

    else:
        return '''Error, ingrese el directorio completo:

    linux: '/home/user/.../carpeta'

    windows: 'C:\Usuario\Escritorio\Carpeta' '''
