# -*- coding: utf-8 -*-
import os
import glob

def lista_archivos():
    
    lista = glob.glob('*.csv')
    for i in xrange(0,len(lista)-1):
        if not 'WSlog' in lista[i]:
            del lista[i]
        else:
            return lista
        
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
        nombres_archivos.sort()
        return nombres_archivos

    #si no, probamos si está en una carpeta dentro del directorio actual
    elif os.path.exists(directorio): 

        os.chdir(directorio) #y si está entramos a esa carpeta

        #y añadiremos los nombres de los archivos a una lista
        nombres_archivos = lista_archivos()
        nombres_archivos.sort()
        return nombres_archivos
        
    else:
        return '''Error, ingrese el directorio completo:
                
    linux: '/home/user/.../carpeta' 
                
    windows: 'C:\Usuario\Escritorio\Carpeta' '''        
