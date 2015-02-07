# -*- coding: utf8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import obtener as ob

def sep(data):
    motor1 = []
    motor2 = []
    for tablas in data:
        motor = tablas[tablas['errors']<' 0x40']
        if len(motor.values) != 0:
            motor1.append(motor)

            motor = tablas[tablas['errors']>=' 0x40']
        if len(motor.values) != 0:
            motor2.append(motor)

    return motor1, motor2

def concatenar(motor1,motor2):
    motor1total = pd.concat(motor1)
    motor1total = motor1total.resample('200ms')
    motor2total = pd.concat(motor2)
    motor2total = motor2total.resample('200ms')
    return motor1total,motor2total

def juntar(motor1total, motor2total):
    motores = None
    if motor1total.index[-1]>motor2total.index[-1]:
        motores = motor1total.join(motor2total,how='outer',lsuffix = '_m1', rsuffix = '_m2')
    else:
        motores = motor2total.join(motor1total,how='outer',lsuffix = '_m2', rsuffix = '_m1')
    return motores
