"""
Como debemos modificar un código existente,
 lo colocamos aquí como muestra

 import numpy as np
import matplotlib. pyplot as plt
from numpy.random import RandomState
prng = RandomState(1234567890)

T = 1.0
L = 64
dt = T / L
W = np.zeros(L + 1)
W_refined = np.zeros(2 * L + 1)
xi = np.sqrt(dt) * prng.normal(size=L)
xi_half = np.sqrt(0.5 * dt) * prng.normal(size=L)
W[1:] = xi.cumsum()
W_ = np.roll(W, -1)
W_half = 0.5 * (W + W_)
W_half = np.delete(W_half, -1) + xi_half
W_refined[1::2] = W_half
W_refined[2::2] = W[1:]
t = np.arange(0, T + dt, dt)
t_half = np.arange(0, T + 0.5 * dt, 0.5 * dt)

plt.plot(t, W, 'b-+')
plt.plot(
    t_half,
    W_refined,
    'ro--',
    alpha=0.5
)
plt.show()

Ya que debemos hacerlo una función. 
"""
import numpy as np
import matplotlib.pyplot as plt
prng = np.random.RandomState(10)

def refined_brownian_2n(T,L):
    dt = T / L
    W = np.zeros(L + 1)
    W_refined = np.zeros(2 * L + 1)
    xi = np.sqrt(dt) * prng.normal(size=L)
    xi_half = np.sqrt(0.5 * dt) * prng.normal(size=L)
    W[1:] = xi.cumsum()
    W_ = np.roll(W, -1)
    W_half = 0.5 * (W + W_)
    W_half = np.delete(W_half, -1) + xi_half
    W_refined[1::2] = W_half
    W_refined[2::2] = W[1:]
    t = np.arange(0, T + dt, dt)
    t_half = np.arange(0, T + 0.5 * dt, 0.5 * dt)
    return t,t_half,W, W_refined
