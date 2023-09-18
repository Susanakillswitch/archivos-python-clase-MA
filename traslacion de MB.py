import numpy as np
import matplotlib.pyplot as plt

def strong_brownian_path(T, N, c):
    T = 1
    N = 100; dt = c**2*T/N
    dw = np.zeros(N+1)
    w = np.zeros(N+1)
    dw[0] = np.sqrt(dt)*np.random.standard_normal() 
    w[0] = 0
    w[1] = dw[0]
    for i in np.arange(2,N):
        dw[i-1] = np.sqrt(dt)*np.random.standard_normal()
        w[i] = w[i-1]+dw[i-1]
    y = np.linspace(0, T, N+1)
    y1 = c**2*y
    return y1,w
y1, w = strong_brownian_path(1,1, 2)
plt.plot(y1,w)
plt.show()
     
