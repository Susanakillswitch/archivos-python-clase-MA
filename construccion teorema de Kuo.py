import numpy as np
import matplotlib.pyplot as plt
N = 10 #numero de puntos
T = 1.0 #hasta que distancia llega
delta = T/N #division
eps = 1.0/np.sqrt(N)
t = np.linspace(0, T, N+1) #te genera una particion de (0,1) con paso de 1/10
b = np.random.binomial(1, .5, N) #bernoulli 0,1
omega = 2.0 * b-1 # bernoulli -1,1
xn = eps *(omega.cumsum()) # bernoulli -h, h
xn = np.concatenate(([0], xn))
M = np.abs(xn).max() + eps
mu = xn.mean()*np.ones(xn.shape)
plt.plot(
    t,
    xn,
    'k-o',
    alpha=0.8,
    lw=1,
    ms=4,
    mfc='green',
    label=r'$RW$'
)
plt.plot(t,
mu,
'r-',
label=r'$E[X_n]$'
)
#para las etiquetas en los ejes
plt.xlabel(r'$\delta$')
plt.ylabel(r'$X_n$')
plt.title(r'Construccion teorema Kuo')
#plt.title(r'caminata del borracho')
plt.grid(True)
plt.legend(shadow=True,loc=0)
plt.show()