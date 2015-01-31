# -*- coding: utf-8 -*-
import os

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
        return 'está'

    #si no, probamos si está en una carpeta dentro del directorio actual
    elif os.path.exists(directorio): 

        os.chdir(directorio) #y si está entramos a esa carpeta

        return os.getcwd()
    else:
        return '''Error, ingrese el directorio completo:
                
    linux: '/home/user/.../carpeta' 
                
    windows: 'C:\Usuario\Escritorio\Carpeta' '''

        
        
