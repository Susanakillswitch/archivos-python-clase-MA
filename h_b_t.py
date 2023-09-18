"""
Importamos las librerias necesarias 
"""
import numpy as np
import matplotlib.pyplot as plt


"""
Comenzaremos simulando el movimiento browniano fuerte.
"""
prng = np.random.RandomState(10)  # Fijamos la semilla. 

t_final = 1  # Extremo derecho del intervalo [0,T]
n_points = 64  # No olvidemos que aquí se incluye el 0 y t.
dt = 1 / (n_points - 1)  # Ajuste al delta t

dw = np.sqrt(dt) * prng.standard_normal(n_points - 1)  # Calculamos los incrementos.
w = np.concatenate(([0],dw.cumsum()))

time = np.linspace(0,t_final, n_points)  # Vector de tiempo. 

#plt.plot(time, w)        # Graficamos el browniano base.
# plt.show()

"""
Ahora, comenzamos con el browniano escalado. 
"""
c = 0.2  # 1/5


"""
Esto tiene dos interpretaciones. 
Sin embargo, para este ejercicio debemos partir de una trayectoria dada, entonces haremos la transformación. 
"""

c_time = c**2 * time  # Transformamos el intervalo del tiempo
c_w = c**(-1) * w  # Escalamos el browniano. 

# plt.plot(c_time,c_w)
# plt.show() 

#punto 2 de la tarea 4
fig, browniano_escalado = plt.subplots(2)
browniano_escalado[0].plot(time, w)
browniano_escalado[1].plot(c_time, c_w)
browniano_escalado[0].set_title('Movimiento browniano')
browniano_escalado[1].set_title('Moviemiento browniano escalado')
plt.show()