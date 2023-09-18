import numpy as np
import random as r
import matplotlib.pyplot as plt
T = 1
N = 500; dt = T/N
dw = np.zeros(N)
w = np.zeros(N)

dw[0] = np.sqrt(dt)*np.random.standard_normal() 
w[0] = 0
w[1] = dw[0]
for in np.arrange(2,N-1):
    dw[i-1] = np.sqrt(dt)*np.random.standard_normal()
    w[i] = w[i-1]+dw[i-1]

plt.plot(np.arange(0, T, dt),w)
plt.show()