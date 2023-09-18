import numpy as np
import matplotlib.pyplot as plt
from numpy.random import RandomState

prng = RandomState(1234567890)

T = 1-0
L = 64 #no. puntos
dt = T / L
W = np.zeros(L + 1) #reservar memoria
W_refined = np.zeros(2 * L + 1)
xi = np.sqrt(0.5 * dt) * prng.normal(size=L) # crear la variable aleatoria del generador prng
xi_half = np.sqrt(0.5 * dt) * prng.normal(size=L)
W[1:] = xi.cumsum() #W[1:] para que empiece desde el lugar 1 en adelante
W_ = np.roll(W, -1) # para recorer a la izquierda el vector
W_half = 0.5 * (W + W_)
W_half = np.delete(W_half, -1) + xi_half #np.delete(W_half, -1) me elimina el ultimo elemento del vector
W_refined[1::2] = W_half # acomo los refinamientos nuevos en el punto medio
W_refined[2::2] = W[1:] # acomodo los refinamientos originales 
t = np.arange(0, T + dt, dt)
t_half = np.arange(0, T+0.5 * dt, 0.5 * dt)

plt.plot(t, W, 'b-+')
plt.plot(
    t_half,
    W_refined,
    'ro--',
    alpha = 0.5
)
plt.show()
