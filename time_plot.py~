import pandas as pd

def hora(dataframe,hora1, hora2):
    """Ingrese la hora inicial y final en numeros entre comillas
    del 1 al 24, si desea los minutos, ingrese el 
    numero seguido de : , si desea al nivel de segundo
    se coloca la hora:min:seg.fracciondeseg"""
    inf = str(dataframe.head(1).index.values[0])[0:11]
    sup = str(dataframe.tail(1).index.values[0])[0:11]
    if str(hora1) in str(range(0,24)):
        hora1=str(hora1)+':00'
    if str(hora2) in str(range(0,24)):
        hora2=str(hora2)+':00'    
    hora1 = inf+str(hora1)
    hora2 = sup+str(hora2)
    
    return dataframe[hora1:hora2].plot()

def horam(listaDF, hora1,hora2):
    for df in listaDF:
        hora(df,hora1,hora2)
    
