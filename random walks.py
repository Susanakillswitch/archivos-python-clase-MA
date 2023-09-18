import numpy as np
import matplotlib.pyplot as plt

def brownian_path(N, T):
    delta = T / N
    h = 1.0 / N
    t = np.linspace(0, T, N+1)
    b = np.random.binomial(1, 0.5, N)
    omega = 2.0 * b-1 #bernoulli -1, 1
    xn = h * (omega.cumsum()) #bernoulli -h, h
    xn = np.concatenate(([0], xn))
    M = np.abs(xn).max()+ h
    mu = xn.mean() * np.ones(xn.shape)
    return t, xn
t,x = brownian_path(1000, 1)
plt.plot(t,x)
plt.show()

n_paths = 100
n_points = 1000
T = 1.0
mean = np.zeros(n_points+1)
X_t = np.zeros(n_points)
for i in np.arange(n_paths):
    t, X_t = brownian_path(n_points, T)
    plt.plot(
        t,
        X_t,
        'g-',
        alpha=0.5,
        lw=1
    )
    mean = mean + X_t
mean = n_paths**(-1)* mean
plt.plot(
    t,
    mean,
    'r--',
    lw=1
)
# plt.savefig(
    #"sample_100_paths_weakBr.png".
#) para guardar una figura
plt.show()